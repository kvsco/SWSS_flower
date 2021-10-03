from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    print(" .. loading ..  ")

    return HttpResponse("index")
