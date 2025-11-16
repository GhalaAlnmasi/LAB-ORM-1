from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.utils.translation import gettext_lazy as _
from .models import Post
from django.views.decorators.http import require_POST

# Create your views here.

def add_post_view(request:HttpRequest):
  return render(request, "posts/add-post.html")

# View all Posts
def my_posts_view(request):
    posts = Post.objects.all()
    return render(request, "posts/my_posts.html", {"posts": posts})

# Creating Post
def create_post(request:HttpRequest):

  title = request.POST.get("title")
  content = request.POST.get("content")
  image = request.FILES.get("image")

  post = Post.objects.create(title=title, content=content, image=image) 

  messages.success(request, _("Post Created Successfully"))

  return redirect(request.META.get("HTTP_REFERER", "/"))


# View Ppst Details
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "posts/post_detail.html", {"post": post})


# Edit Post
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")

        if request.FILES.get("image"):
            post.image = request.FILES.get("image")

        post.save()
        messages.success(request, "Post updated successfully")
        return redirect("posts:edit_post", pk=pk)

    return render(request, "posts/edit_post.html", {"post": post})
    


# Delete Post
@require_POST
def delete_post_confirm(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect("posts:my_posts_view")