from django import forms
from . import models, parser_book


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('books', 'books'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'books':
            books_pars = parser_book.parsing()
            for i in books_pars:
                models.Book.objects.create(**i)
