from django.shortcuts import render
from .models import BandMember, Album, Concert
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required



def home(request):
    albums = Album.objects.all()
    members = BandMember.objects.all()
    concerts = Concert.objects.all()
    context = {
        'albums': albums,
        'members': members,
        'concerts': concerts
    }
    return render(request, 'band/home.html', context)

def band_members(request):
    members = BandMember.objects.all()
    return render(request, 'band/members.html', {'members': members})

def concerts(request):
    concerts = Concert.objects.all()
    return render(request, 'band/concerts.html', {'concerts': concerts})

def home(request):
    return render(request, 'band/home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def listen_now(request):
    return render(request, 'band/listen_now.html')



