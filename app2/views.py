from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def college(request):
    return HttpResponse('<h1><marquee>BPUT<marquee/><h1>')
def language(request):
    return HttpResponse('<h1><marquee>python<marquee/><h1>')