from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(max_length=500, blank=True,default='Details')


def get_image_path(instance, filename):
    return '/'.join(['product_images', str(instance.name), filename])


class Product(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    url = models.CharField(max_length=200)
    product_type = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images', blank=True, null=True)
    image_url = models.CharField(max_length=200, blank=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index', kwargs={})
