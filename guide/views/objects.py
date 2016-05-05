from django.shortcuts import render
from django.http import HttpResponse

from guide.models import Exhibition, Artwork

def object_photos(request, slug):
    coll = Exhibition.objects.filter(slug=slug)
    if coll:
        art = Artwork.objects.filter(exhibition=coll)
        context = {'c': coll.first(), 'art': art}

        return render(request, "objects/photos.html" , context)
    else:
        return HttpResponse("Not Found")
