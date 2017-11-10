from django.conf.urls import include, url
from django.contrib import admin
import products.urls

from django.utils.translation import ugettext_lazy as _


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(products.urls)),
]

# Change admin site title
admin.site.site_header = _("Product App Administration")
admin.site.site_title = _("My Site Admin")
