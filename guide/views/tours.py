from django.shortcuts import render
from django.http import HttpResponse

from guide.models import Exhibition, Tour, Artwork

def tours(request, collection):
    coll_set = Exhibition.objects.filter(slug=collection, is_live=True)
    if coll_set:
        coll = coll_set.first()
        tours = Tour.objects.filter(exhibition=coll)
        context = {'c': coll, 'tours': tours}
        return render(request, "tours/index.html" , context)
    else:
        return HttpResponse("Not Found")

def tour(request, collection, tour):
    request.session['object-mode'] = 'tours/' + tour
    coll_set = Exhibition.objects.filter(slug=collection, is_live=True)
    tour_set = Tour.objects.filter(slug=tour)
    if coll_set and tour_set:
        coll = coll_set.first()
        tour = tour_set.first()
        art = Artwork.objects.filter(exhibition=coll, tour=tour).order_by('tourartwork__position')
        context = {'c': coll, 'tour': tour, 'art': art}
        return render(request, "tours/tour.html" , context)
    else:
        return HttpResponse("Not Found")
