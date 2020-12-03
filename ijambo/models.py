from django.db import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from . models import *

class Profil(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, upload_to="profil/avatars/")
    
    def __str__(self):
        return f"{self.user.username}"

class Music(models.Model):
	title = models.CharField(max_length=30)
	author = models.ForeignKey(Profil, null=True, blank=True, on_delete=models.CASCADE)
	featuring = models.CharField(null=True, blank=True, max_length=30)
	composer =  models.CharField(max_length=30)
	producer = models.CharField(max_length=30)
	cover = models.ImageField(upload_to="music/covers/")
	audio = models.FileField(upload_to="music/audios/")
	release = models.DateField()

	def __str__(self):
		return f"{self.title} by {self.author}"

class Album(models.Model):
	title = models.CharField(max_length=30)
	cover =  models.ImageField(upload_to="album/covers/")
	music = models.ForeignKey(Music, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return f"Album : {self.title}"

class MonthSong(models.Model):
	channel = models.CharField(max_length=30)
	audio = models.ForeignKey(Music, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.channel} : {self.audio.title} by {self.audio.author}"

class Contact(models.Model):
	email = models.EmailField()
	messsage = models.TextField()

	def __str__(self):
		return f"{self.email}"

class Event(models.Model):
	title = models.CharField(max_length=30)
	cover = models.ImageField(upload_to="events/cover/")
	organizer = models.CharField(max_length=30)
	place = models.CharField(max_length=30)
	entry_prices = models.CharField(max_length=40)
	about = models.CharField(max_length=1000)
	paid = models.BooleanField(False)

	def __str__(self):
		return f"{self.title}- place : {self.place} - Entry : {self.entry_prices}"
