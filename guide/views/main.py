from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from guide.update_data import update_from_CMS
from guide.models import Exhibition, Artwork
from guide.forms import CodeForm

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
                HttpResponseRedirect(reverse('object_search', object=obj.slug))
            else:
                msg = "Unfortunately, we cannot find that object"
        else:
            msg = "Please enter an object code"
    else:
        form = CodeForm()

        return render(request, 'search.html', {'form': form, 'message' : msg})


def update_data(request):
    update_from_CMS()
    return HttpResponse("Data has been updated!")
