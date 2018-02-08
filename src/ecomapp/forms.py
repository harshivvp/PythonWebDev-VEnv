from django import forms
from .models import Product
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'desc', 'category', 'images', 'price', 'quantity']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
