from django.shortcuts import render
from django.http import HttpResponse

from guide.models import Exhibition, Artwork, Media

def object_photos(request, slug):
    coll = Exhibition.objects.filter(slug=slug)
    if coll:
        img = Media.objects.filter(kind='image', position='0')
        art = Artwork.objects.filter(exhibition=coll).order_by('title').prefetch_related(Prefetch('media', queryset=img, to_attr='cover_img'))
        context = {'c': coll.first(), 'art': art}

        return render(request, "objects/photos.html" , context)
    else:
        return HttpResponse("Not Found")
