

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('smart_card.urls')),
    url(r'^smart_card/', include('smart_card.urls')),
    url(r'^admin/', admin.site.urls),
]
