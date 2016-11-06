import datetime

from django.http import HttpResponse


# Create your views here.

# view as function
def hello(request):
    return HttpResponse("Hello world")


def current_datetime(request):
    now = datetime.datetime.now()
    message = "It is now %s." % now
    return HttpResponse(message)
