from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from login.forms import SignUpForm


def login_inicio(request):
    if request.user.is_authenticated:
        return redirect('participantes')
    return render(request, 'login.html')


def login_hackaton(request):
    if request.user.is_authenticated:
        return redirect('participantes')

    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            #request.session.set_expiry(300)
            login(request, user)
            return redirect('participantes')
        else:
            return render(request, 'login.html',{'error':'Usuario no válido'})
    return render(request, 'login.html')

def logout_hackaton(request):
    logout(request)
    return redirect('login')

def registrar_participante(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('participantes')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})