from django.shortcuts import render
from django.http import HttpResponse

from guide.update_data import update_data


def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def update_data(request):
    update_data()
    return HttpResponse("Data has been updated!")
