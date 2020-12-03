from django.shortcuts import render
from django.contrib.auth.models import User
from ijambo.models import *
# Create your views here.

def home(request):
	try:
		profile = Profil.objects.get(user=request.user)
		return render(request, 'simple_user.html', locals())
	except Exception as e:
		err_msg = "You must login first to access this page !"
		return render(request, '404.html', locals())
	