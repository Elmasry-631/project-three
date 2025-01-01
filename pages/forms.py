from django import forms
from .models import *


class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=20,initial="user name", label="user name")
    user_email = forms.EmailField(max_length=30, initial="Email", label="Email")
    password = forms.CharField()
    
    
class test(forms.ModelForm):
    test_name = forms.CharField()