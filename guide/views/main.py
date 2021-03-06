from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

import pytz
import datetime
from itertools import chain

from guide.services.update_data import update_data_CMS
from guide.services.update_hours import update_hours_CMS
from guide.models import Exhibition, Artwork, Hour
from guide.forms import CodeForm

def get_dow():
    today = datetime.datetime.today()
    wkday = today.weekday()
    wkday += 2
    if wkday > 7:
        wkday -= 7
    return wkday

def is_open():
    dow = get_dow()
    today = Hour.objects.filter(dow_i=dow)
    if today:
        td = today.first()
        est = pytz.timezone('US/Eastern')
        now = datetime.datetime.now(est)
        if td.day_open and td.day_close:
            if td.day_open <= now.time() <= td.day_close:
                #open
                return {'class':'open', 'info':'The museums are open now!'}


        #closed
        return {'class':'closed', 'info':'The museums are currently closed'}

    return None


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
        after = Hour.objects.filter(dow_i__gt=dow).order_by('dow_i')
        before = Hour.objects.filter(dow_i__lt=dow).order_by('dow_i')
        other_days = list(chain(after, before))
        mus_open = is_open()
        context={'today': today, 'other_days': other_days, 'is_open': mus_open}
        return render(request, 'hours.html', context)

    raise Http404("Hours")

def connect(request):
    return render(request, 'connect.html')


def update_data(request):
    update_data_CMS()
    update_hours_CMS()
    return HttpResponse("Data has been updated!")
