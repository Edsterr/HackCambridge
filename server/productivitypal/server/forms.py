from django import forms
from django.contrib.auth.models import User

from server import models


class UserForm(forms.ModelForm):
    username = forms.EmailField(label="Email", help_text="Please enter your e-mail address.",
                                widget=forms.EmailInput(attrs={'class': "form-control"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': "form-control"}), max_length=100, min_length=10,)
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class': "form-control"}), max_length=100, min_length=10)

    class Meta:
        model = User
        fields = ("username", "password")

    def clean_email(self):
        email = self.cleaned_data['username']
        return email

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if not confirm_password:
            raise forms.ValidationError("You must confirm your password")
        if password != confirm_password:
            raise forms.ValidationError("Your passwords do not match")

        return self.cleaned_data

class ProfileForm(forms.ModelForm):

    class Meta:
        model = models.UserProfile
        fields = ()
