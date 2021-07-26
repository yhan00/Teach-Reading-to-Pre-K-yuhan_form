from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Forms for Users created here

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'username', 'password1', 'password2']    


