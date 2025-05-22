from django.urls import path
from . import views
urlpatterns = [
    path('posts/',views.post_lists, name='post_lists'),
    path('posts/drafts',views.post_lists, name='post_drafts'),
    path('posts/new',views.post_create, name='post_create'),
    path('posts/<int:id>',views.post_detail, name='post_detail'),
    path('posts/<int:id>/edit',views.post_update, name='post_update'),
]