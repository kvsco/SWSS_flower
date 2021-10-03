from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    print("----"*20)

    return HttpResponse("<h1>index</h1>")
