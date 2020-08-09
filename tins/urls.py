from django.urls import path
from . import views
urlpatterns = [
    path('tweet/<int:tweet_id>',views.tweet_detail_view, name='tweet'),
]