from django.shortcuts import render
from django.http import HttpResponse
import requests, re

#TODO: Move these to a settings field
news_url = "http://guide-cms-prod.s3.amazonaws.com/feeds/news.html"
videos_url = "http://guide-cms-prod.s3.amazonaws.com/feeds/videos.html"

def news_show(request):
    r = requests.get(news_url)
    s = re.search('(<style type="text/css">[\s\S]+</ul>)', r.text)
    if s:
        context = {'news_text': s.group(0)}
    else:
        content = {'news_text':'<p>Sorry, we can\'t retrieve news at the moment, please try again later.</p>'}
    return render(request, 'news.html', context)

def videos_show(request):
    r = requests.get(videos_url)
    s = re.search('(<style type="text/css">[\s\S]+</ul>)', r.text)
    if s:
        context = {'videos_text': s.group(0)}
    else:
        content = {'videos_text':'<p>Sorry, we can\'t retrieve videos at the moment, please try again later.</p>'}
    return render(request, 'videos.html', context)
