# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from books.models import Book


def browser_information(request):
    ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    return HttpResponse("Your browser is %s" % ua)


def search(request):
    error = False
    if 'fsearch' in request.GET:
        fsearch = request.GET['fsearch']
        if not fsearch:
            error = True
        else:
            books = Book.objects.filter(title__icontains=fsearch)
            return render(request, 'search-results.html',
                          {'books': books, 'query': fsearch})

    return render(request, 'search-form.html', {'error': error})
