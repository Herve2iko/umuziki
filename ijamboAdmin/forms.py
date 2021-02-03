from django import forms
from django.contrib.auth.models import User
from ijambo.models import *
from .views import * 


class MusicForm(forms.ModelForm):
	title = forms.CharField(
		label='titre',
		widget = forms.TextInput(
		    attrs={
		        'class':'form-control p_input'
		    }
		))
	featuring = forms.CharField(
		label='featuring',
		widget = forms.TextInput(
		    attrs={
		        'class':'form-control p_input',
		    }
		))
	composer=forms.CharField(
	    label='le composeur',
	    widget = forms.TextInput(
	        attrs={
	            'class':'form-control p_input',
	        }
	    ))

	producer=forms.CharField(
	    label='producteur',
	    widget = forms.TextInput(
	        attrs={
	            'class':'form-control p_input',

	        }
	    ))
	cover=forms.FileField(
	    label='Cover',
	    widget = forms.FileInput(
	        attrs={
	        'class':'form-control-file',
	        'placeholder':'cover'
	        }
	    ))

	audio=forms.FileField(
	    label='Audio',
	    widget = forms.FileInput(
	        attrs={
	            'class':'form-control-file',
	            'placeholder':'audio'
	        }
	    ))
	release=forms.DateField(
	    label='Release',
	    widget = forms.TextInput(
	        attrs={
	            'class':'form-control p_input',
	            'type':'date',
	        }
	    ))

	class Meta : 
		model = Music
		exclude = ['author',]

class AlbumForm(forms.ModelForm):
    title = forms.CharField(
        label='Titre',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'title'
            }))

    cover =forms.FileField(
        label='cover',
        widget = forms.FileInput(
            attrs={
                'class':'form-control-file',
                'placeholder':'coversong'
            }
        ))
    class Meta:
        model = Album
        exclude = ['author']
    def __init__(self, user, *args, **kwargs):
    	super(AlbumForm, self).__init__(*args, **kwargs)
    	self.fields['music'].queryset = Music.objects.filter(author = user)

class MonthSongForms(forms.ModelForm):

    channel = forms.CharField(
        label='RadioName',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'station'
            }))
    auteur = forms.CharField(
        label='Auteur',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'author'
            }))

    audio = forms.FileField(
        label='SongMonth',
        widget = forms.FileInput(
            attrs={
                'class':'form-control',
                'placeholder':'Song Of The Month'
            }
        ))

    class Meta:
        model = MonthSong
        fields = '__all__'
        
class EventForm(forms.ModelForm):

    title = forms.CharField(
        label='Titre',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'title'
            }))

    cover = forms.FileField(
        label='Cover',
        widget = forms.FileInput(
            attrs={
            'class':'form-control-file',
            'placeholder':'cover'
            }
        ))
    organizer = forms.CharField(
        label='Organisateur',
        widget = forms.TextInput(
            attrs={
            'class':'form-control',
            'placeholder':'organizer'
            }
        ))
    place = forms.CharField(
        label='Place',
        widget = forms.TextInput(
            attrs={
            'class':'form-control',
            'placeholder':'place'
            }
        ))
    entry_prices = forms.CharField(
        label='Droit_Entree',
        widget = forms.TextInput(
            attrs={
            'class':'form-control',
            'placeholder':'entry_prices'
            }
        ))
    class Meta : 
        model=Event
        exclude = ['author','paid']