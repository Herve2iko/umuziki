from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name='homeAdmin'),
    path('addMusic/', views.MusicRegester, name='music'),
    path('addAlbum/', views.AlbumRegester, name='album'),
]
