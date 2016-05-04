from django.shortcuts import render
from django.http import HttpResponse
import requests, re

news_url = "http://guide-cms-prod.s3.amazonaws.com/feeds/news.html"

def news_show(request):
    r = requests.get(news_url)
    s = re.search('(<style type="text/css">[\s\S]+)(</body>)', r.text)
    if s:
        context = {'news_text': s.group(0)}
    else:
        content = {}
    return render(request, 'news.html', context)
