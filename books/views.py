# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from books.models import Book


def browser_information(request):
    ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    return HttpResponse("Your browser is %s" % ua)


def search_form(request):
    return render(request, 'search-form.html')


def search(request):
    if 'fsearch' in request.GET and request.GET['fsearch']:
        fsearch = request.GET['fsearch']
        books = Book.objects.filter(title__icontains=fsearch)
        return render(request, 'search-results.html',
                      {'books': books, 'query': fsearch})
    else:
        return HttpResponse('Please submit a search term.')
