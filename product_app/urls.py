from django.conf.urls import include, url
from django.contrib import admin
import main_app.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(main_app.urls)),
]
