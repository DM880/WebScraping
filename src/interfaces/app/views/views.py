from django.conf import settings
from django.shortcuts import render, redirect, reverse
from django.views.decorators.csrf import csrf_exempt
from pathlib import Path

from src.domain.bot import scrape_bot


from src.interfaces.app.views.tasks import data_download


def home(request):
    return render(request, "home.html")


def download(request):
    if request.method == "POST":

        url = request.POST.get('url')

        return render(request, 'download.html', {'url':url})

    return redirect('home')


def download_info(request):

    if request.method == "POST":

        url = request.POST.get('url')

        datas = scrape_bot(url)

        # downloads_path = str(Path.home() / "Downloads")

        datas.to_excel("url_scraped.xlsx", sheet_name="url_scraped")

        return redirect('home')



