from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    print(" .. loading ..  ")

    return render(request, 'index.html')
