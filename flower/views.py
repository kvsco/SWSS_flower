from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    # print(" .. loading ..  ")
    # return HttpResponse("index")
    return render(request, "flower/index.html")

def generic(request):
    return render(request, "flower/generic.html")

def elements(request):
    return render(request, "flower/elements.html")