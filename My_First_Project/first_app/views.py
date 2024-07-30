from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.db.models import Avg
from django.conf import settings
from first_app import forms
from first_app import views


# Models import
from first_app.models import Musician, Album
# Import forms
from first_app import forms


def index(request):
    """Render the home page with a list of musicians."""
    musician_list = Musician.objects.order_by('id')
    context = {
        'title': "Home Page",
        'musician_list': musician_list
    }
    return render(request, 'first_app/index.html', context=context)


def album_list(request, artist_id):
    """Render a list of albums for a specific artist."""
    artist_info = get_object_or_404(Musician, pk=artist_id)
    album_list = Album.objects.filter(artist=artist_info.id).order_by('release_date', 'name')
    artist_rating = Album.objects.filter(artist=artist_info.id).aggregate(Avg('num_stars'))
    context = {
        'title': "Album Page",
        'artist_info': artist_info,
        'album_list': album_list,
        'artist_rating': artist_rating,
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'first_app/album_list.html', context=context)


def musician_form(request):
    """Handle form for creating or updating a musician."""
    if request.method == "POST":
        form = forms.MusicianForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Form is valid and data is saved.")
            return HttpResponseRedirect(reverse('first_app:home'))
        else:
            print("Form is not valid.")
    else:
        form = forms.MusicianForm()

    context = {
        'title': "Add Musician",
        'musician_form': form
    }
    return render(request, 'first_app/musician_form.html', context=context)



def album_form(request):
    """Handle form for creating a new album."""
    if request.method == "POST":
        form = forms.AlbumForm(request.POST, request.FILES)  # Include uploaded image if applicable
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('first_app:home'))
    else:
        form = forms.AlbumForm()

    context = {
        'title': "Add Album",
        'album_form': form
    }
    return render(request, 'first_app/album_form.html', context=context)


def edit_artist(request, id):
    """Handle form for editing an existing musician."""
    artist_info = get_object_or_404(Musician, pk=id)
    if request.method == "POST":
        form = forms.MusicianForm(request.POST, request.FILES, instance=artist_info)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('first_app:album_list', args=[id]))
    else:
        form = forms.MusicianForm(instance=artist_info)

    context = {
        'title': "Edit Musician",
        'musician_form': form
    }
    return render(request, 'first_app/edit_artist.html', context=context)


def edit_album(request, album_id):
    """Handle form for editing an existing album."""
    album_info = get_object_or_404(Album, pk=album_id)
    if request.method == "POST":
        form = forms.AlbumForm(request.POST, instance=album_info)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('first_app:album_list', args=[album_info.artist_id]))
    else:
        form = forms.AlbumForm(instance=album_info)

    context = {
        'title': "Edit Album",
        'album_form': form,
        'album_id': album_id
    }
    return render(request, 'first_app/edit_album.html', context=context)


def delete_album(request, album_id):
    """Handle the deletion of an album."""
    try:
        album = Album.objects.get(pk=album_id)
        album.delete()
        context = {
            'title': 'Delete View',
            'success_text': 'Successfully Deleted this Album!'
        }
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'first_app/delete_album.html', context=context)


def delete_artist(request, artist_id):
    """Handle the deletion of a musician."""
    try:
        artist = Musician.objects.get(pk=artist_id)
        artist.delete()
        context = {
            'title': 'Delete View',
            'success_text': 'Successfully Deleted this Artist!'
        }
    except Musician.DoesNotExist:
        raise Http404("Artist does not exist")
    return render(request, 'first_app/delete_artist.html', context=context)
