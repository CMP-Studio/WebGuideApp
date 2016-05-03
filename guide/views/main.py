from django.shortcuts import render
from django.http import HttpResponse

from guide.update_data import update_from_CMS
from guide.models import Exhibition

def index(request):
    exhibs = Exhibition.objects.filter(is_live=True)
    r_exhib = Exhibition.objects.filter(is_live=True).order_by('?').first() #get a random exhibitions
    r_img = r_exhib.bg_ipad_retina
    context = {'bg_img': r_img}
    return render(request, 'index.html', context)

def update_data(request):
    update_from_CMS()
    return HttpResponse("Data has been updated!")
