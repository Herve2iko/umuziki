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
	title = models.CharField(max_length=50)
	author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	featuring = models.CharField(null=True, blank=True, max_length=50)
	composer =  models.CharField(max_length=50)
	producer = models.CharField(max_length=50)
	cover = models.ImageField(upload_to="music/covers/")
	audio = models.FileField(upload_to="music/audios/")
	release = models.DateField()


	def __str__(self):
		return f"{self.title} by {self.author}"

class Album(models.Model):
	author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	title = models.CharField(max_length=30)
	cover =  models.ImageField(upload_to="album/covers/")
	music = models.ManyToManyField(
        Music,
        through ='AlbumMusic',
        through_fields =('albumSong', 'music'),
    )
	def __str__(self):
		return f"Album : {self.title}"

class AlbumMusic(models.Model):
	albumSong = models.ForeignKey(Album, on_delete = models.CASCADE)
	music = models.ForeignKey(Music, on_delete = models.CASCADE)

class MonthSong(models.Model):
	channel = models.CharField(max_length=30)
	audio = models.ForeignKey(Music, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.channel} : {self.audio.title} by {self.audio.author}"

class Contact(models.Model):
	sender = models.CharField(max_length = 50, null = True)
	email = models.EmailField()
	message = models.TextField()

	def __str__(self):
		return f"{self.message} {self.sender} adresse {self.email}"

class Event(models.Model):
	author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	title = models.CharField(max_length=30)
	cover = models.ImageField(upload_to="events/cover/")
	organizer = models.CharField(max_length=30)
	place = models.CharField(max_length=30)
	entry_prices = models.CharField(max_length=40)
	paid = models.BooleanField(default = False)

	def __str__(self):
		return f"{self.title}- place : {self.place} - Entry : {self.entry_prices}"

class paiemment(models.Model):
	codesender = models.IntegerField()
	codeverifier = models.IntegerField()

	def __str__(self):
		return f"{self.codesender} verifie {self.codeverifier}"
