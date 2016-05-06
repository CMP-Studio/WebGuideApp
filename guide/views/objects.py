from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Prefetch

from guide.models import Exhibition, Artwork, Media, Category

def object_photos(request, collection):
    request.session['object-mode'] = 'photos';
    coll = Exhibition.objects.filter(slug=collection, is_live=True)
    if coll:
        media = Media.objects.filter(kind='image', position='0', artwork__exhibition=coll).order_by('artwork__title')
        #Split media into two arrays (one for each column)
        left = []
        right = []
        leftH = 0
        rightH = 0
        for m in media:
            if leftH <= rightH:
                left.append(m)
                leftH += (m.height / m.width)
            else:
                right.append(m)
                rightH += (m.height / m.width)

        mediaCol = {'left' : left, 'right' : right}
        context = {'c': coll.first(), 'media': mediaCol}
        return render(request, "objects/photos.html" , context)
    else:
        return HttpResponse("Not Found")

def object_list(request, collection):
    request.session['object-mode'] = 'list';
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
    request.session['object-mode'] = 'category/' + category;
    coll = Exhibition.objects.filter(slug=collection, is_live=True)
    cat = Category.objects.filter(slug=category)
    if coll and cat:
        art = Artwork.objects.filter(exhibition=coll, category=cat)
        context = {'c': coll.first(), 'cat': cat.first(), 'art': art}
        return render(request, "objects/category.html" , context)
    else:
        return HttpResponse("Not Found")

def object(request, collection, object):
    if 'object-mode' not in request.session:
        back_url = 'photos'
    else:
        back_url = request.session['object-mode']
    coll = Exhibition.objects.filter(slug=collection, is_live=True)
    if coll:
        obj = Artwork.objects.filter(slug=object)
        art = Artwork.objects.filter(exhibition=coll).order_by('title')
        info = get_art_bar_info(art, obj)
        context = {'c': coll.first(), 'object': obj.first(), 'art_info':info, 'back': back_url}
        return render(request, "objects/object.html" , context)
    else:
        return HttpResponse("Not Found")

def object_w_category(request, collection, category, object):
    if 'object-mode' not in request.session:
        back_url = 'photos'
    else:
        back_url = request.session['object-mode']
    coll = Exhibition.objects.filter(slug=collection, is_live=True)
    cat =  Category.objects.filter(slug=category)
    if coll and cat:
        obj = Artwork.objects.filter(slug=object)
        art = Artwork.objects.filter(exhibition=coll, category=cat).order_by('title')
        info = get_art_bar_info(art, obj)
        context = {'c': coll.first(), 'object': obj.first(), 'art_info':info, 'back': back_url}
        return render(request, "objects/object.html" , context)
    else:
        return HttpResponse("Not Found")

def get_art_bar_info(art, obj):
    indx = -1
    for counter, a in art:
        if a.uuid == obj.uuid:
            indx = counter
            break

    info = {}
    count = art.count()
    info['count'] = count
    if indx > 0:
        info['prev'] = art[indx-1]
    if indx < count - 1
        info['next'] = art[indx+1]

    indx++
    info['current'] = indx
    return info
