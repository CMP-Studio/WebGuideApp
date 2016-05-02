from django.shortcuts import render
from django.http import HttpResponse

from guide.update_data import update_from_CMS


def index(request):
    return render(request, 'index.html')

def update_data(request):
    update_from_CMS()
    return HttpResponse("Data has been updated!")
