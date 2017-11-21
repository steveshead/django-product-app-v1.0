from django import forms
from .models import Product
from .models import UserProfile
from django.contrib.admin import widgets
from django.forms import Textarea

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'url', 'product_type', 'price', 'image', 'image_url']
        labels = {
            'name': 'Product Name',
            'url': 'Product URL',
            'product_type': 'Product Type',
            'description': 'Product Description',
            'image': 'Product Image',
            'image_url': 'Product Image URL',
            'price': 'Product Price',
        }
        widgets = {
            'description': Textarea(attrs={'rows': 5}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=64)
    password = forms.CharField(required=False, widget=forms.PasswordInput())

class EditProfileForm(forms.Form):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    biography = forms.CharField(label='Biography', widget=Textarea(attrs={'rows': 5}))
    tagline = forms.CharField(label='Tagline', required=False)
    image = forms.ImageField(required=False)


class SubscribeForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)


class ContactForm(forms.Form):
    contact_name = forms.CharField(label="Name", required=True)
    contact_email = forms.EmailField(label="Email", required=True)
    content = forms.CharField(label="Message", required=True, widget=forms.Textarea)
