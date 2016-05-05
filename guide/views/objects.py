from django.shortcuts import render
from django.http import HttpResponse

from guide.models import Exhibition

def object_photos(request, slug):
    coll = Exhibition.objects.filter(slug=slug)
    if coll:
        context = {'c': coll.first()}
        return render(request, "objects/photos.html" , context)
    else:
        return HttpResponse("Not Found")
