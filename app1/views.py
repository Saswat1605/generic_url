from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_name(request):
    return HttpResponse('<h1><marquee>I am saswat<marquee/><h1>')
def addres(request):
    return HttpResponse('<h1><marquee>bengaluru<marquee/><h1>')
