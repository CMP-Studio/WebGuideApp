from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Prefetch

from guide.models import Exhibition, Artwork, Media

def object_photos(request, slug):
    coll = Exhibition.objects.filter(slug=slug)
    if coll:

        media = Media.objects.filter(kind='image', position='0', artwork__exhibition=coll).order_by(artwork__title)
        context = {'c': coll.first(), 'media': media}

        return render(request, "objects/photos.html" , context)
    else:
        return HttpResponse("Not Found")
