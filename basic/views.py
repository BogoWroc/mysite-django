import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.timezone import now

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
