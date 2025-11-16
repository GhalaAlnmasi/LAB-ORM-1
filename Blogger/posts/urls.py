from django.urls import path
from . import views


app_name = "posts"

urlpatterns = [
  path("add/", views.add_post_view, name="add_post_view"),
    path("create/", views.create_post, name="create_post"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    path("<int:pk>/edit/", views.edit_post, name="edit_post"),
    path('<int:pk>/delete/', views.delete_post_confirm, name='delete_post_confirm'),
    path("my-posts/", views.my_posts_view, name="my_posts_view"),
]