from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

CHOICES = (
    ('Junior', 'Junior'),
    ('Middle', 'Middle'),
    ('Senior', 'Senior'),
)

class CustomRegistrationForm(UserCreationForm):
    level = forms.ChoiceField(choices=CHOICES, required=True)

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