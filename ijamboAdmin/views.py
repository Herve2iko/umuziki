from django.shortcuts import render
from django.contrib.auth.models import User
from ijambo.models import *
from .forms import *
# Create your views here.

def home(request):
	try:
		profile = Profil.objects.get(user=request.user)
		return render(request, 'simple_user.html', locals())
	except Exception as e:
		err_msg = "You must login first to access this page !"
		return render(request, '404.html', locals())

@login_required(login_url='connect')
def MusicRegester(request):
	usr = request.user
	InputMusic = MusicForm(request.POST or None, request.FILES)
	if (request.method == 'POST'):
		if (InputMusic.is_valid()):
			ff = InputMusic.save(commit=False)
			ff.author = usr
			ff.save()
	InputMusic = MusicForm()
	return render(request, "forms.html",locals())