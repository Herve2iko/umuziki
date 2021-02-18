from django.urls import path
from ijamboAdmin import views
urlpatterns = [
    path('', views.home, name='homeAdmin'),
    path('addMusic/', views.MusicRegester, name='music'),
    path('ddMusic/', views.MusicRegester, name='mus'),
    path('addAlbum/', views.AlbumRegester, name='album'),
    path('addEvent/', views.EventRegester, name='addevent'),
    path('listMusic/', views.MusicListe, name='lsMusic'),
    path('UpdateMusic/<int:ms_id>', views.UpdateMusic, name='upMusic'),

]
