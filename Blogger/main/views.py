from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.utils.translation import gettext_lazy as _
from posts.models import Post
# Create your views here.

def home_view(request: HttpRequest):
  latest_post = Post.objects.last()
  posts = Post.objects.all().order_by("-id")
  return render(request, "main/index.html", {"latest_post": latest_post, "posts": posts})


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