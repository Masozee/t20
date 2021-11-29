from django.shortcuts import render
from datetime import datetime, timedelta, time
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView, ListView, TemplateView
from django.shortcuts import render, redirect


from .models import *

# Create your views here.
def home(request):
    Events = event.objects.all().order_by('-mulai').distinct()[:4]
    News = berita.objects.filter(publish=True)
    context = {
        "events": Events,
        "Berita": News,
    }

    return render(request, "index.html", context)

def Acara(request):
    Events = event.objects.all()
    context = {
        "events": Events,
    }

    return render(request, "event.html", context)