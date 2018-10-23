from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm): #Inheritence
    #adding addition fields to UsercreationForm Form
    email = forms.EmailField() #by default this field is required=True

    class Meta:
        model = User
        fields = ['username','email','password1','password2'] #fields and their order

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField() #by default this field is required=True

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
