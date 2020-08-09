from django.urls import path
from . import views
urlpatterns = [
    path('tin/<int:tweet_id>',views.tin_detail_view, name='tin..'),
    path('',views.home_view, name='home'),
    path("tins/", views.tin_list_view, name= "tinslist")
]