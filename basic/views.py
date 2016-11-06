from django.http import HttpResponse


# Create your views here.

# view as function
def hello(request):
    return HttpResponse("Hello world")
