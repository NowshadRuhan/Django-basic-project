from django.conf.urls import url
from django.urls import path

from first_app import views


#app name added for relative urls
app_name = "first_app"


urlpatterns = [
    path('', views.index, name='home'),#this name='home' use for relative urls
    path('add_album/', views.albumForm, name='album_Form'),
    path('add_musician/', views.musicianForm, name='musician_Form'),
    path('album_list/<int:artist_id>/', views.albumList, name='album_list'),
    path('edit_artist/<int:id>/', views.editArtist, name='edit_artist'),
    path('edit_album/<int:album_id>/', views.editAlbum, name='edit_album'),
    path('delete_album/<int:album_id>/', views.deleteAlbum, name='delete_album'),
    path('delete_artist/<int:artist_id>/', views.deleteArtist, name='delete_artist')
]
