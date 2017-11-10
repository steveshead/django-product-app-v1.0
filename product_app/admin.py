from django.contrib import admin
from .models import Product #, HashTag

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Biography

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class BiographyInline(admin.StackedInline):
    model = Biography
    can_delete = False
    verbose_name_plural = 'biography'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (BiographyInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register your models here.
admin.site.register(Product)
