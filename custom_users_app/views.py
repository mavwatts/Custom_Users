from django.shortcuts import render, HttpResponseRedirect, reverse
from custom_users_app.models import MyUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from custom_users_app.forms import LoginForm, SignupForm
from custom_users_main.settings import AUTH_USER_MODEL


@login_required
def index_view(request):
    return render(request, 'index.html', {'Auth': AUTH_USER_MODEL})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get('username'), password=data.get('password')) 
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
  
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = MyUser.objects.create_user(
                username=data.get('username'), 
                password=data.get('password'), 
                displayname=data.get('displayname')
            )
            if new_user:
                login(request, new_user)
                return HttpResponseRedirect(reverse('homepage'))

    form = SignupForm()
    return render(request, "generic_form.html", {'form': form})
