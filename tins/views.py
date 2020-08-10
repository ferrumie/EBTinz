from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Tins
from .forms import TinsForm
import random
# Create your views here.
def tin_create_view(request, *args, **kwargs):
    form = TinsForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url != None:
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
    tins_list = [{"id":x.id, "content": x.content, "likes":random.randint(0,100)} for x in qs]

    data = {
        "response":tins_list
    }

    return JsonResponse(data)
