from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['username']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, you've logged in")

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))

                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'authorization',
        'form': form
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username}, you've successfully created an account")

            return HttpResponseRedirect(reverse('user:login'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'registration',
        'form': form,
    }
    return render(request, 'users/registration.html', context)


@login_required()
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.files)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated')

            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'title': 'profile',
        'form': form,
    }
    return render(request, 'users/profile.html', context)


def users_cart(request):
    return render(request, 'users/users_cart.html')


@login_required()
def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))
