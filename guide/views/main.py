from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

import datetime
from itertools import chain

from guide.update_data import update_data_CMS
from guide.update_hours import update_hours_CMS
from guide.models import Exhibition, Artwork, Hour
from guide.forms import CodeForm

def get_dow():
    today = datetime.datetime.today()
    wkday = today.weekday()
    wkday += 2
    if wkday > 7:
        wkday -= 7
    return wkday

def index(request):
    r_exhib = Exhibition.objects.filter(is_live=True).order_by('?').first() #get a random exhibitions
    r_img = r_exhib.bg_ipad_retina
    context = {'bg_img': r_img}
    return render(request, 'index.html', context)

def search(request):
    msg = None
    if request.method == 'POST':
        #Do something
        form = CodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            obj = Artwork.objects.filter(code=code)
            if obj:
                obj = obj.first()
                return HttpResponseRedirect(reverse('object_search', args=[obj.slug]))
            else:
                msg = "Unfortunately, we cannot find that object"
        else:
            msg = "Please enter an object code"

    form = CodeForm()
    return render(request, 'search.html', {'form': form, 'message' : msg})

def visit(request):
    hours = Hour.objects.all()
    if hours:
        dow = get_dow()
        today = Hour.objects.filter(dow_i=dow).first()
        after = Hour.object.filter(dow_i__gt=dow).order_by('dow_i')
        before = Hour.object.filter(dow_i__lt=dow).order_by('dow_i')
        other_days = list(chain(after, before))
        context={'today': today, 'other_days': other_days}
        return render(request, 'hours.html', context)

    return HttpResponse("Hours not found")


def update_data(request):
    update_data_CMS()
    update_hours_CMS()
    return HttpResponse("Data has been updated!")
