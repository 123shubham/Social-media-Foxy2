from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length = 64)
    last_name = forms.CharField(max_length = 64)
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email', 'password1', 'password2',)