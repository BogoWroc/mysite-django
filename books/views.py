# Create your views here.
from django.http import HttpResponse


def browser_information(request):
    ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    return HttpResponse("Your browser is %s" % ua)
