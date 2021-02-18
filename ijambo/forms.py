from django import forms
from . models import *
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField( widget=forms.TextInput(
    	attrs={
    		'placeholder':'Username or A.K.A',
    		'class':'form-control'
    		}),
    	label='Username')
    first_name = forms.CharField( widget=forms.TextInput(
    	attrs={
    		'placeholder':'Firstname',
    		'class':'form-control'
    		}),
    	label='Firstname')
    last_name = forms.CharField( widget=forms.TextInput(
    	attrs={
    		'placeholder':'Lastname',
    		'class':'form-control'}),
    	label='Lastname')
    password = forms.CharField( widget=forms.PasswordInput(
    	attrs={
    		'placeholder':'password ',
    		'class':'form-control'}),
    	label='password')
    password2 = forms.CharField( widget=forms.PasswordInput(
    	attrs={
    		'placeholder':'confirm password ',
    		'class':'form-control'}),
    	label='confirm password')
    email = forms.EmailField( widget = forms.TextInput(
    	attrs = {
    		'placeholder':'email adress ',
    		'class':'form-control'}),
    	label='your email adress')
    avatar = forms.ImageField(widget=forms.FileInput(
    	attrs={'class':'form-control'}),
    	label='your profile picture')
 

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Username',
            'class':'form-control'}),
        label='Username(A.K.A)')
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder':'password ',
            'type':'password',
            'class':'form-control'}))

class ContactForm(forms.ModelForm):
    sender = forms.CharField(widget = forms.TextInput(
        attrs = {
                'placeholder':'Izina',
                'type':'text',
                'class':'form-control',
                'id':'name'}))
    email = forms.CharField(widget = forms.TextInput(
        attrs = {
                'placeholder':'Email yawe',
                'type':'email',
                'class':'form-control',
                'id':'email'}))
    message = forms.CharField(widget = forms.TextInput(
        attrs = {
                'placeholder':'Message yawe',
                'type':'textarea',
                'class':'form-control',
                'id':'message',
                'cols':'30',
                'rows':'10'}))
    class Meta:
        model = Contact
        fields = '__all__'
