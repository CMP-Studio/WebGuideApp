from django.shortcuts import render
from django.http import HttpResponse

from guide.models import Exhibition, Tour

def tours(request, collection):
    coll_set = Exhibition.objects.filter(slug=collection, is_live=True)
    if coll_set:
        coll = coll_set.first()
        tours = Tour.objects.filter(exhibition=coll)
        context = {'c': coll, 'tours': tours}
        return render(request, "tours/index.html" , context)
    else:
        return HttpResponse("Not Found")
