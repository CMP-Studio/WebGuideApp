from django.shortcuts import render
from django.http import HttpResponse

from guide.models import Exhibition

def collections_list(request):
    exhibs = Exhibition.objects.filter(is_live=True)
    context = {'collections': exhibs}
    return render(request, 'collections.html', context)

def collection(request, uuid):
    return HttpResponse(uuid)
