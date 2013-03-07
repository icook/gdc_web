from django.db import models
from django.template.context import Context
from django.http import HttpResponse
from django.template import loader
from models import Content, News

def index(request):
    return page_render(request, 'home')

def simple_news(request, nav_items):
    posts = News.objects.all().order_by('-posted')[:5]
    template = loader.get_template('main/news.html')
    context = Context({
	'posts': posts,
    'links': nav_items,
    })
    return HttpResponse(template.render(context))

def page_render(request, url_key):
    """
    Always make sure this is defined last!!!!!
    Otherwise symbolic links will break...
    """
    nav_items = Content.objects.filter(main_nav=True)
    content = Content.objects.get(url_key=url_key)
    
    # Run some logic to do our symbolic link
    if content.symbolic != "no":
        try:
            return globals()[content.symbolic](request, nav_items)
        except KeyError:
	        return HttpResponse(loader.get_template('main/sym_error.html').render(Context({'links': nav_items})))
    
    template = loader.get_template('main/pages.html')
    context = Context({
        'links': nav_items,
        'content_val': content.body,
    })
    return HttpResponse(template.render(context))