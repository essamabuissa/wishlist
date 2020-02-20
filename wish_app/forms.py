from django.contrib.auth.models import User
from django import forms
from .models import Item
class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username' , 'password' ,'first_name','last_name', 'email']
        widgets={
        'password': forms.PasswordInput(),
        }


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'image', 'url']



class SigninForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
