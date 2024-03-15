from django import forms
from .models import ShortenedURL

class ShortenURLForm(forms.ModelForm):
    class Meta:
        model = ShortenedURL
        fields = ['long_url', 'slug']