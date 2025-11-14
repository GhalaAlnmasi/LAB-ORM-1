from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.utils.translation import gettext_lazy as _
from .models import Post
# Create your views here.

def home_view(request: HttpRequest):
  latest_post = Post.objects.last()
  return render(request, "main/index.html", {"latest_post":latest_post})

def add_post_view(request:HttpRequest):
  return render(request, "main/add-post.html")

def create_post(request:HttpRequest):

  title = request.POST.get("title")
  content = request.POST.get("content")

  post = Post.objects.create(title=title,content=content) 

  messages.success(request, _("Post Created Successfully"))

  return redirect(request.META.get("HTTP_REFERER", "/"))



def set_theme(request:HttpRequest, mode):
    response = redirect(request.GET.get('HTTP_REFERER', '/'))
    if mode in ['dark', 'light']:
      response.set_cookie('theme', mode, max_age=60*60*24) 
    return response


def set_language(request: HttpRequest, lang):
    referer = request.GET.get('HTTP_REFERER', request.META.get('HTTP_REFERER', '/'))
    response = redirect(referer)
    if lang in ['en', 'ar']:
      response.set_cookie('django_language', lang, max_age=60*60*24*30)
    return response