from django.shortcuts import render
from django.http import HttpResponse

def tours(request, collection):
    return HttpResponse(collection)
