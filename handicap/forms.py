from django import forms
from .models import Round, Course



class EntryForm(forms.ModelForm):
  class Meta:
    model = Round
    fields = ['tee','score','differential','date_played','used']

class UrlForm(forms.Form):
  url= forms.URLField()
  
class CourseForm(forms.ModelForm):
  class Meta:
    model = Course
    fields = ['name','street','city','region','zip_Code']