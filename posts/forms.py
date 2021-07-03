from django import forms

from pagedown.widgets import PagedownWidget

from .models import Post
from django.contrib.admin import widgets

class PostForm(forms.ModelForm):
    title=forms.CharField(widget=forms.Textarea(attrs={'style': 'height:40px;width:700px'}))
    # publish = forms.DateField(widget=forms.SelectDateWidget())
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            # "publish",
        ]