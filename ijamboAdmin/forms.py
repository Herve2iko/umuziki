from django import forms
from django.contrib.auth.models import User
from ijambo.models import *
from .views import * 


class MusicForm(forms.ModelForm):
	class Meta:
		model = Music
		exclude =['author',]

class AlbumForm(forms.ModelForm):

	class Meta:
		model = Album
		exclude =['author',]

		def __init__(self,request, *args, **kwargs):
			super(AlbumForm,self).__init__(*args, **kwargs)
			self.fields['music'].queryset = Music.objects.filter(author=request.user)

class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		exclude =['author','paid',]