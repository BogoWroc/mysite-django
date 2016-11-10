import datetime

from django.core.mail import send_mail
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.timezone import now

from basic.forms import ContactForm
from .util.time_calculation import add_hours


# Create your views here.

# view as function
def hello(request):
    return HttpResponse("Hello world")


def current_datetime(request):
    now = datetime.datetime.now()
    message = "It is now %s." % now
    return HttpResponse(message)


def hours_ahead(request, offset):
    offset = int(offset)
    date_time = add_hours(datetime.datetime.now(), offset)
    message = "In %s hour(s), it will be  %s." % (offset, date_time)
    return HttpResponse(message)


def order_report(request):
    # Defines context of template
    context = {
        "person": {"first_name": "Bogumil", "sure_name": "Zebek"},
        "company": "Pythonic",
        "ship_date": now(),
        "item_list": ['Car', 'Bike', 'Motorcycle'],
        "ordered_warranty": True,
    }

    # Render template as page
    return render(request, "order-report.html", context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request,
                  'contact-form.html', {'form': form}
                  )
