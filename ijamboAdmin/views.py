from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from ijambo.models import *
from .forms import *
# Create your views here.
@login_required(login_url='connect')
def currentUser(request):
	return request.user

def home(request):
	try:
		profile = Profil.objects.get(user=request.user)
		return render(request, 'simple_user.html', locals())
	except Exception as e:
		err_msg = "You must login first to access this page !"
		return render(request, '404.html', locals())

@login_required(login_url ='connect')
def MusicRegester(request):
	usr = request.user
	profile = Profil.objects.get(user=usr)
	InputMusic = MusicForm(request.POST or None, request.FILES)
	if (request.method == 'POST'):
		if (InputMusic.is_valid()):
			print(InputMusic)
			ff = InputMusic.save(commit=False)
			ff.author = usr
			ff.save()
	InputMusic = MusicForm()
	return render(request, "forms.html",locals())

@login_required(login_url ='connect')
def AlbumRegester(request):
	usr = request.user
	profile = Profil.objects.get(user=usr)
	InputAlbum = AlbumForm(request.user, request.POST or None, request.FILES)
	if(request.method == 'POST'):
		if(InputAlbum.is_valid()):
			aa = InputAlbum.save(commit=False)
			aa.author = request.user
			aa.save()
	InputAlbum = AlbumForm(request.user)
	return render(request, "forms.html", locals())

@login_required(login_url ='connect')
def EventRegester(request):
	usr = request.user
	profile = Profil.objects.get(user=usr)
	InputEvent = EventForm(request.POST or None, request.FILES)
	if(request.method == 'POST'):
		if(InputEvent.is_valid()):
			ee = InputEvent.save(commit = False)
			ee.author = request.user
			ee.save()
	InputEvent = EventForm()
	return render(request, "forms.html", locals())

@login_required(login_url ='connect')	
def MusicListe(request):
	usr = request.user
	profile = Profil.objects.get(user=usr)
	msics = Music.objects.filter(author = usr)
	return render(request, "liste.html", locals())

@login_required(login_url ='connect')	
def UpdateMusic(request, ms_id):
	ms = Music.objects.get(id = ms_id)
	ModiMusic = MusicForm(request.POST or None, request.FILES, instance= ms)
	if (request.method == 'POST'):
		if (ModiMusic.is_valid()):
			print(ModiMusic)
			ff = ModiMusic.save(commit=False)
			ff.author = request.user
			ff.save()
			return redirect(MusicListe)
	ModiMusic = MusicForm(instance = ms)
	return render(request,"forms.html" , locals())