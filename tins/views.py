from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from .models import Tins
from .forms import TinsForm
import random
from django.conf import settings
from django.utils.http import is_safe_url
# Create your views here.

ALLOWED_HOSTS = settings.ALLOWED_HOSTS
def tin_create_view(request, *args, **kwargs):
    print("ajax",request.is_ajax())
    form = TinsForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if request.is_ajax():
            return JsonResponse(obj.serialize(), status=201) 
        if next_url != None and is_safe_url(next_url,ALLOWED_HOSTS):
            return redirect(next_url)
        form = TinsForm()
    return render(request, 'components/form.html', context={"form":form})
    

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
    tins_list = [x.serialize() for x in qs]

    data = {
        "response":tins_list
    }

    return JsonResponse(data)
