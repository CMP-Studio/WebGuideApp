from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import requests, re


def news_show(request):
    r = requests.get(settings.NEWS_URL)
    s = re.search('(<ul>[\s\S]+</ul>)', r.text)
    if s:
        context = {'news_text': s.group(0)}
    else:
        content = {'news_text':'<p>Sorry, we can\'t retrieve news at the moment, please try again later.</p>'}
    return render(request, 'news.html', context)

def videos_show(request):
    r = requests.get(settings.VIDEOS_URL)
    s = re.search('(<ul>[\s\S]+</ul>)', r.text)
    if s:
        context = {'videos_text': s.group(0)}
    else:
        content = {'videos_text':'<p>Sorry, we can\'t retrieve videos at the moment, please try again later.</p>'}
    return render(request, 'videos.html', context)
