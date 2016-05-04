from django.shortcuts import render
from django.http import HttpResponse

news_url = "http://guide-cms-prod.s3.amazonaws.com/feeds/news.html"

def news_show(request):
    r = requests.get(news_url)
    context = {'news_text': r.text}
    return render(request, 'news.html', context)
