from django.shortcuts import render
from django.http import HttpResponse

from guide.models import Exhibition

def collections_list(request):
    collss = Exhibition.objects.filter(is_live=True)
    context = {'collections': colls}
    return render(request, 'collections.html', context)

def collection(request, uuid):
    coll = Exhibition.objects.filter(uuid=uuid)
    context = {'collection': coll}
    if coll:
        return render(request, "collection.html" , context)
    else:
        return HttpResponse("Not Found")
