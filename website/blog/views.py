from django.shortcuts import render

# zhouxiangxiang 2015.08.30
from django.template import loader, Context
from django.http import HttpResponse
from blog.models import BlogPost

# Create your views here.

# zhouxiangxiang 2015.08.30
def archive(request):
	posts = BlogPost.objects.all()
	t     = loader.get_template("html/archive.html")
	c     = Context({'posts' : posts})
	return HttpResponse(t.render(c))


