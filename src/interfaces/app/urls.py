from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from .views import views


urlpatterns = [
    path("", views.home, name="home"),
    path("download/", views.download, name="download"),
    path("download_info/", views.download_info, name="download_info"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
