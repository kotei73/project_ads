from django.shortcuts import render
from django.http import HttpResponse
from .models import Ads

def index(request):
    s = "Список объявлений <br><br>"
    ad = Ads.objects.all()
    for i in ad:
        s += f'{i.title}<br>{i.content}, {i.price} <br><br>'
    return HttpResponse(s)
