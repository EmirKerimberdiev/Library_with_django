from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    level = forms.CharField(max_length=100, required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'level',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super(CustomRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.level = self.cleaned_data['level']
        if commit:
            user.save()
        return user


