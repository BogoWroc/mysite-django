import datetime

from django.http import HttpResponse

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
