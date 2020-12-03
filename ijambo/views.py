from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from . forms import *
from django.contrib import messages

class HomeView(View):
	template_name = 'index.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, locals())

def register(request):
	if request.method == "POST" :
		register_form = RegisterForm(request.POST or None, request.FILES)
		if register_form.is_valid():
			username = register_form.cleaned_data['username']
			first_name = register_form.cleaned_data['first_name']
			last_name = register_form.cleaned_data['last_name']
			password = register_form.cleaned_data['password']
			password2 = register_form.cleaned_data['password2']
			email = register_form.cleaned_data['email']
			avatar = register_form.cleaned_data['avatar']
			if password==password2:
				try:
					user = User.objects.create_user(
						username=username,
						first_name=first_name,
						last_name=last_name,
						email=email, 
						password=password)
					Profil(user=user, avatar=avatar).save()
					if user:
						login(request, user)
						return redirect('home')
				except Exception as e:
					messages.error(request, "Username Already Taken")
	register_form = RegisterForm()
	return render(request, 'register.html', locals())


def connexion(request):
	login_form = LoginForm(request.POST)
	try:
		next_p = request.GET["next"]
	except:
		next_p = ""
	if request.method == "POST":
		if login_form.is_valid():
			username = login_form.cleaned_data['username']
			password = login_form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user:  # Si l'objet renvoyé n'est pas None
				login(request, user)
				if next_p:
					return redirect(next_p)
				else:
					return redirect('home')
		else : 
			error_message='Username Or PassWord Incorect !'
		login_form = LoginForm()
	return render(request, 'login.html', locals())

def deconexion(request):
	logout(request)
	return redirect('home')

def albums(request):
	return render(request, 'albums.html', locals())

def albumDetails(request):
	return render (request, 'album-details.html', locals())

def events(request):
	return render(request, 'events.html', locals())

def eventDetails(request):
	return render(request, 'event-details.html', locals())


def contact(request):
	return render(request, 'contact.html', locals())

def musics(request):
	return render(request, 'musics.html', locals())

def musicsCategories(request):
	return render(request, 'musics-categories.html', locals())

def musicDetails(request):
	return render(request, 'music-details.html', locals())
	
