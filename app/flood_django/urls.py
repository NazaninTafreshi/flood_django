from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from flood.views import main_page,station_page

urlpatterns = [
    path("", main_page, name="home"),
    path("station/", station_page, name="station"),
    path("admin/", admin.site.urls),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
