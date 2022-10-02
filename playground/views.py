from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# a view takes in a request and returns a response
def calculate():
    x=1
    y=2
    return x

def sey_Hello(request):
    x=calculate()
    return render(request, 'hello.html', {'name':''})