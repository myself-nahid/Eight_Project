from django.shortcuts import render, redirect
from . forms import RegisterForm, ChangeUserData
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Create your views here.


def home(request):
    return render(request, './first_app/home.html')


def signup(request):
    if request.method == 'POST':
        forms = RegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
            print(forms.cleaned_data)
    else:
        forms = RegisterForm()
    return render(request, './first_app/signup.html', {'forms': forms})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            forms = AuthenticationForm(request=request, data=request.POST)
            if forms.is_valid():
                name = forms.cleaned_data['username']
                userpass = forms.cleaned_data['password']
                # check kortesi user database ashe kina
                user = authenticate(username=name, password=userpass)
                if user is not None:
                    login(request, user)
                    return redirect('profile')  # profile page redirect korbe
        else:
            forms = AuthenticationForm()
        return render(request, './first_app/login.html', {'forms': forms})

    else:
        return redirect('profile')


def profile(request):
    if request.method == 'POST':
        forms = ChangeUserData(request.POST, instance=request.user)
        if forms.is_valid():
            forms.save()
            print(forms.cleaned_data)
    else:
        forms = ChangeUserData(instance=request.user)
    return render(request, './first_app/profile.html', {'forms': forms})



def user_logout(request):
    logout(request)
    return redirect('login')


def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            # password update korbe
            update_session_auth_hash(request, form.user)
            return redirect('profile')

    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, './first_app/passchange.html', {'forms': form})


def pass_change2(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            # password update korbe
            update_session_auth_hash(request, form.user)
            return redirect('profile')

    else:
        form = SetPasswordForm(user=request.user)
    return render(request, './first_app/passchange.html', {'forms': form})


def change_user_data(request):
    if request.method == 'POST':
        forms = ChangeUserData(request.POST, instance=request.user)
        if forms.is_valid():
            forms.save()
            print(forms.cleaned_data)
    else:
        forms = ChangeUserData()
    return render(request, './first_app/profile.html', {'forms': forms})
