from django import forms
from list.models import search

class UploadForm(forms.ModelForm):
    img = forms.ImageField(label='')
    class Meta:
        model = search
        fields = ['img']
                