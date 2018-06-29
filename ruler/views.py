from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hey, world")


def test(request):
    return HttpResponse("Hey, test ")
