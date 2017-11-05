from django.conf.urls import include, url
from django.contrib import admin
import product_app.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(product_app.urls)),
]
