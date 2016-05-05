from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Prefetch

from guide.models import Exhibition, Artwork, Media, Category

def object_photos(request, collection):
    coll = Exhibition.objects.filter(slug=collection, is_live=True)
    if coll:
        media = Media.objects.filter(kind='image', position='0', artwork__exhibition=coll).order_by('artwork__title')
        context = {'c': coll.first(), 'media': media}
        return render(request, "objects/photos.html" , context)
    else:
        return HttpResponse("Not Found")

def object_list(request, collection):
    coll = Exhibition.objects.filter(slug=collection, is_live=True)
    if coll:
        art = Artwork.objects.filter(exhibition=coll).order_by('title')
        context = {'c': coll.first(), 'art': art}
        return render(request, "objects/list.html" , context)
    else:
        return HttpResponse("Not Found")

def object_cats(request, collection):
        coll = Exhibition.objects.filter(slug=collection, is_live=True)
        if coll:
            cats = Category.objects.filter(artwork__exhibition=coll).distinct().order_by('title')
            context = {'c': coll.first(), 'cats': cats}
            return render(request, "objects/categories.html" , context)
        else:
            return HttpResponse("Not Found")

def object_category(request, collection, category):
    coll = Exhibition.objects.filter(slug=collection, is_live=True)
    cat = Category.objects.filter(slug=category)
    if coll && cat:
        art = Artwork.objects.filter(exhibition=coll, category=cat)
        context = {'c': coll.first(), 'cat': cat.first(), 'art': art}
        return render(request, "objects/category.html" , context)
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
