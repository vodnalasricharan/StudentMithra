from django import forms
from .models import *

class NoteForm(forms.ModelForm):
    data=forms.CharField(widget=forms.Textarea(attrs={
'style': 'height: 200px;width:700px'}))
    class Meta:
        model = Note
        fields = [
            "title",
            "data",
        ]