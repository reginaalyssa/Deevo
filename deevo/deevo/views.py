from django.contrib import messages
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import login
from django.shortcuts import render, redirect

from .forms import SignUpForm

def user_is_not_logged_in(user):
    return not user.is_authenticated()

def deevo_login(request):
    if request.user.is_authenticated():
        return redirect('/')
    else:
        return login(request)

@user_passes_test(user_is_not_logged_in, login_url='/')
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        if request.user.is_authenticated():
            return redirect('/')
        else:
            form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def view_profile(request):
    return render(request, 'account/profile.html', {'profile_user': request.user})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {'form': form})