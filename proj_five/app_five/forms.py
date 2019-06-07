from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo


class UserForm(forms.ModelForm):
    '''
        form for django user model
    '''

    # edit password field in User model
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    '''
        form for UserProfileInfo model
    '''

    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
