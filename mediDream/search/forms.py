from django import forms
from list.models import search

class UploadForm(forms.ModelForm):
    class Meta:
        model = search
        fields = [
            'img',
        ]
                