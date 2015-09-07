from django.shortcuts import render

# zhouxiangxiang 2015.08.30
from django.template import loader, Context
from django.http import HttpResponse
from blog.models import BlogPost

# Create your views here.

# zhouxiangxiang 2015.08.30
# @param  HttpRequest Object.
# @return HttpResponse Object.
def archive(request, num="1"): 
	posts = BlogPost.objects.all()
	t     = loader.get_template("html/archive.html")
	c     = Context({'posts' : posts})
	return HttpResponse(t.render(c))
def pages(request, name=''):
	if name:
		#posts = BlogPost.objects.all()
		posts = BlogPost.objects.get(title = name)
		t     = loader.get_template("html/pages.html")
		c     = Context({'posts' : posts})
		return HttpResponse(t.render(c))
	else:
		posts = BlogPost.objects.get(title='test')
		t     = loader.get_template("html/pages.html")
		c     = Context({'posts' : posts})
		if posts.title:
			return HttpResponse(t.render(c))

