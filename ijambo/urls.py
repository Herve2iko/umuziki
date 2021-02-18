from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contare/', views.contactrecever, name ='conta'),
    path('register/', views.register, name='register'),
    path('login/', views.connexion, name='login'),
    path('logout/', views.deconexion, name='logout'),
    path('albums/', views.albums, name='albums'),
    path('album-details/', views.albumDetails, name='albumdetail'),
    path('events/', views.events, name='events'),
    path('event-details/', views.eventDetails, name='eventdetail'),
    path('contact/', views.contact, name='contact'),
    path('musics/', views.musics, name='musics'),
    path('musics-categories/', views.musicsCategories, name='musicscategories'),
    path('music-details/<int:id>', views.musicDetails, name='musicdetails'),
]
