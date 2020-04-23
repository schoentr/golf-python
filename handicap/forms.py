from django import forms
from .models import Round



class EntryForm(forms.ModelForm):
  class Meta:
    model = Round
    fields = ['tee','score','differential','date_played','used']

class UrlForm(forms.Form):
  url= forms.URLField()
  