from django.shortcuts import render
from django.http import HttpResponse

def tours(request, slug):
    HttpResponse(slug)
