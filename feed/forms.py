from django import forms
from .models import Feed
# Reordering Form and View


class PositionForm(forms.Form):
    position = forms.CharField()


class FeedForm(forms.ModelForm):
    class Meta:
        model = Feed
        fields = ['caption', 'image']