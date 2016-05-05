from django.shortcuts import render
from django.http import HttpResponse

def tours(request, slug):
    return HttpResponse(slug)
