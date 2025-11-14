from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
  path("",views.home_view, name="home_view"),
  path("add-post/", views.add_post_view, name="add_post_view"),
  path("create-post/", views.create_post, name="create_pos" ),
  path('set-language/<str:lang>/', views.set_language, name='set_language'),
  path('set-theme/<str:mode>/', views.set_theme, name='set_theme'),
]