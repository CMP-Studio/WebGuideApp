from django.shortcuts import render
from django.http import HttpResponse

from guide.update_data import update_from_CMS
from guide.models import Exhibition

def index(request):
    exhibs = Exhibition.objects.filter(is_live=True)
    return render(request, 'index.html')

def update_data(request):
    update_from_CMS()
    return HttpResponse("Data has been updated!")
