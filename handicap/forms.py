from django import forms
from .models import Round

class EntryForm(forms.ModelForm):
  class Meta:
    model = Round
    fields = ['course','tee','score','differential','date_played']