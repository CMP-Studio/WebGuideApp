from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Prefetch

from guide.models import Exhibition, Artwork, Media, Category

def object_photos(request, slug):
    coll = Exhibition.objects.filter(slug=slug, is_live=True)
    if coll:
        media = Media.objects.filter(kind='image', position='0', artwork__exhibition=coll).order_by('artwork__title')
        context = {'c': coll.first(), 'media': media}
        return render(request, "objects/photos.html" , context)
    else:
        return HttpResponse("Not Found")

def object_list(request, slug):
    coll = Exhibition.objects.filter(slug=slug, is_live=True)
    if coll:
        art = Artwork.objects.filter(exhibition=coll).order_by('title')
        context = {'c': coll.first(), 'art': art}
        return render(request, "objects/list.html" , context)
    else:
        return HttpResponse("Not Found")

def object_cats(request, slug):
        coll = Exhibition.objects.filter(slug=slug, is_live=True)
        if coll:
            cats = Category.objects.filter(artwork_set__exhibition=coll)
            context = {'c': coll.first(), 'cats': cats}
            return render(request, "objects/categories.html" , context)
        else:
            return HttpResponse("Not Found")

def object(request, collection, object):
    coll = Exhibition.objects.filter(slug=collection, is_live=True)
    if coll:
        art = Artwork.objects.filter(slug=object)
        context = {'c': coll.first(), 'art': art.first()}
        return render(request, "objects/object.html" , context)
    else:
        return HttpResponse("Not Found")
