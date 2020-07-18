from django.shortcuts import render
from django.http import HttpResponse

#Models import
from first_app.models import Musician, Album
#import forms
from first_app import forms
#datbase function Added
from django.db.models import Avg


def index(request):
    Musician_list = Musician.objects.order_by('id')
    diction = {
        'title': "Home Page",
        'Musician_list':Musician_list
    }
    return render(request, 'first_app/index.html', context=diction)

def albumList(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    album_list = Album.objects.filter(artist=artist_info.id).order_by('release_date', 'name')
    artist_rating = Album.objects.filter(artist=artist_info.id).aggregate(Avg('num_stars'))
    diction = {
        'title': "Album Page",
        'artist_info':artist_info,
        'album_list':album_list,
        'artist_rating':artist_rating
    }
    return render(request, 'first_app/album_list.html', context=diction)


def musicianForm(request):
    new_form = forms.MusicianForm()
    if request.method == "POST":
         new_form = forms.MusicianForm(request.POST)
         if new_form.is_valid():
             new_form.save(commit=True)
             return index(request)

    diction = {
        'title': "Add Musician",
        'Musician_Form' : new_form
    }
    return render(request, 'first_app/musician_form.html', context=diction)



def albumForm(request):
    album_form = forms.AlbumForm()

    if request.method == "POST":
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save(commit=True)
            return index(request)
    diction = {
        'title': "Add Album",
        'album_form': album_form
    }
    return render(request, 'first_app/album_form.html', context=diction)

def editArtist(request, id):
    artist_info = Musician.objects.get(pk=id)
    new_form = forms.MusicianForm(instance=artist_info)

    if request.method == "POST":
        new_form = forms.MusicianForm(request.POST, instance=artist_info)
        if new_form.is_valid():
            new_form.save(commit=True)
            return albumList(request, artist_info.id)

    diction = {
        'title': "Edit Musician",
        'Musician_Form' : new_form
    }
    return render(request, 'first_app/edit_artist.html', context=diction)

def editAlbum(request, album_id):
    album_info = Album.objects.get(pk=album_id)
    album_form = forms.AlbumForm(instance=album_info)
    diction={'title': "Edit Album",}
    if request.method == "POST":
        album_form = forms.AlbumForm(request.POST, instance=album_info)
        if album_form.is_valid():
            album_form.save(commit=True)
            diction.update({
                'success_text':'Successfully Updated'
            })
            # return albumList(request, album_info.artist_id)

    diction.update({
        'album_form':album_form,
        'album_id':album_id
    })
    return render(request, 'first_app/edit_album.html', context=diction)

def deleteAlbum(request, album_id):
    album = Album.objects.get(pk=album_id).delete()
    diction = {
        'title':'Delete View',
        'success_text':'Successfully Deleted this Album!'
    }
    return render(request, 'first_app/delete_album.html', context=diction)


def deleteArtist(request, artist_id):
    aritist = Musician.objects.get(pk=artist_id).delete()
    diction = {
        'title':'Delete View',
        'success_text':'Successfully Deleted this Aritist!'
    }
    return render(request, 'first_app/delete_album.html', context=diction)
