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


class UserRecordForm(forms.ModelForm):
    time_start = forms.DateTimeField()
    time_end = forms.DateTimeField()

    class Meta:
        model = models.UserRecord
        fields = ("time_start", "time_end",)


# An interval of time and an associated interval of productive time
class ProductivityIntervalForm(forms.ModelForm):
    time_productive = forms.DurationField()
    time_total = forms.DurationField()

    class Meta:
        model = models.ProductivityInterval
        fields = ("time_productive", "time_total",)


#Represents a git repository
class RepositoryForm(forms.ModelForm):
    url = forms.CharField(max_length=200)

    class Meta:
        model = models.Repository
        fields = ("url",)


#Represents work done on a repository over a productivity interval
class RepositoryIntervalForm(forms.ModelForm):
    lines = models.IntegerField()
    words = models.IntegerField()

    class Meta:
        model = models.RepositoryInterval
        fields = ("lines", "words")


#Represents time spent productively browsing done over a productivity interval
class WindowIntervalForm(forms.ModelForm):
    class Meta:
        model = WindowIntervalForm
        fields = ()