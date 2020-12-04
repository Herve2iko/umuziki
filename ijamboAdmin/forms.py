from django import forms
from ijambo.models import *

class MusicForm(forms.ModelForm):
	class Meta:
		model = Music
		exclude =['author',]