from django import forms
from datetime import date

#validation library import
from django.core import validators


#import Models induvitual
#from first_app.models import Album, Musician

#import all model
from first_app import models

#get today date
today = date.today()


class MusicianForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs=
        {'placeholder': 'First Name', 'style':'width:300px; height:33px; border: 1px solid gray; border-radius:2px;'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs=
        {'placeholder': 'Last Name', 'style':'width:300px; height:33px; border: 1px solid gray; border-radius:2px;'}))
    instrument = forms.CharField(widget=forms.TextInput(attrs=
        {'placeholder': 'Instrument', 'style':'width:300px; height:33px; border: 1px solid gray; border-radius:2px;'}))

    class Meta:
        model = models.Musician
        fields = "__all__"

class AlbumForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs=
        {'placeholder': 'Album Name', 'style':'width:300px; height:33px; border: 1px solid gray; border-radius:2px;'}))

    release_date = forms.DateField(widget= forms.DateInput(attrs=
        {'type':'date' ,'style':'width:300px; height:33px; border: 1px solid gray; border-radius:2px;'}))
    class Meta:
        model = models.Album
        fields = "__all__"
