# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def browser_information(request):
    ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    return HttpResponse("Your browser is %s" % ua)


def search_form(request):
    return render(request, 'search-form.html')


def search(request):
    if 'fsearch' in request.GET and request.GET['fsearch']:
        message = 'You searched for: %r' % request.GET['fsearch']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
