from django.shortcuts import render
from django.http import HttpResponse

from guide.models import Exhibition

def exhibition_list(request):
    exhibs = Exhibition.objects.filter(is_live=True)
    context = {'collections': exhibs}
    return render(request, 'collections.html', context)
