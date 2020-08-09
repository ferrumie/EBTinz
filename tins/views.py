from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request, *args, **kwargs):
    print(args ,kwargs)
    return HttpResponse("Hi")

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    print(args ,kwargs)
    return HttpResponse(f"Hi,{tweet_id}")
