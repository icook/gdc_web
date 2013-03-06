from django.db import models
from django.template.context import Context
from django.http import HttpResponse
from django.template import loader
from models import Content

def index(request):
    nav_items = Content.objects.filter(main_nav=True)
    template = loader.get_template('main/pages.html')
    content = Content.objects.get(url_key='home')
    if content:
        content_ret = content.body
    else:
        content_ret = "<h2>Coming Soon</h2>"
    context = Context({
        'links': nav_items,
        'content_val': content_ret
        
    })
    return HttpResponse(template.render(context))

def page_render(request, url_key):
    nav_items = Content.objects.filter(main_nav=True)
    content = Content.objects.get(url_key=url_key)
    template = loader.get_template('main/pages.html')
    context = Context({
        'links': nav_items,
        'content_val': content.body,
    })
    return HttpResponse(template.render(context))