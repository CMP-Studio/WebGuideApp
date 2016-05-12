from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from guide.models import Exhibition

def collections_list(request):
    colls = Exhibition.objects.filter(is_live=True)
    context = {'collections': colls}
    return render(request, 'collections.html', context)

def collection(request, collection):
    coll = Exhibition.objects.filter(slug=collection)
    if coll:
        context = {'c': coll.first()}
        return render(request, "collection.html" , context)
    else:
        raise Http404("Not Found")
