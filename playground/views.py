from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# a view takes in a request and returns a response

def sey_Hello(request):
    return HttpResponse('Hey hey its Wainaina')
