from django.urls import path
from first_app import views
from django.conf import settings
from django.conf.urls.static import static

# App name added for namespaced URLs
app_name = "first_app"

urlpatterns = [
    path('', views.index, name='home'),#Home page
    path('add_album/', views.album_form, name='album_form'),  # Form to add a new album
    path('add_musician/', views.musician_form, name='musician_form'),  # Form to add a new musician
    path('album_list/<int:artist_id>/', views.album_list, name='album_list'),  # List albums for a specific artist
    path('edit_artist/<int:id>/', views.edit_artist, name='edit_artist'),  # Edit musician details
    path('edit_album/<int:album_id>/', views.edit_album, name='edit_album'),  # Edit album details
    path('delete_album/<int:album_id>/', views.delete_album, name='delete_album'),  # Delete an album
    path('delete_artist/<int:artist_id>/', views.delete_artist, name='delete_artist')  # Delete a musician
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)