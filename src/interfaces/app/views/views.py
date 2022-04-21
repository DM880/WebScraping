from django.conf import settings
from django.shortcuts import render, redirect, reverse

from src.domain.bot import scrape_bot


def home(request):
    return render(request, "home.html")


def get_url(request):
    if request.method == "POST":

        url = request.POST.get('url')
        datas = scrape_bot(url)

        return render(request, 'base.html')

    else:
        return render(request, "base.html")

