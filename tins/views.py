from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Tins
import random
# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request,"pages/home.html", context={}, status = 200)

def tin_detail_view(request, tweet_id, *args, **kwargs):
    data = {
        "id":tweet_id,
    }
    status = 200
    try:
        obj = Tins.objects.get(id = tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not Found"
        status = 404
    return JsonResponse(data, status= status)

def tin_list_view(request, *args, **kwargs):
    qs = Tins.objects.all()
    tins_list = [{"id":x.id, "content": x.content, "likes":random.randint(0,100)} for x in qs]

    data = {
        "response":tins_list
    }

    return JsonResponse(data)
