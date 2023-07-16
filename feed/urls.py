from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('',home,name='feed'),
    path('create-feed/',create_feed,name='create-feed'),
    path('<int:feed_id>/',delete_feed,name='delete-feed'),
    path('feed/<int:feed_id>',get_feed_by_id,name='feed-id')
]