from django.shortcuts import render, redirect
from .forms import UserReg, ProfileImage, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = UserReg(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Акаунт {username} был успешно создан,введите логин и пароль для авторизации')
            return redirect('user')

    else:
        form = UserReg()
    return render(request, 'users/registration.html', {'form': form, 'title': 'Регистрация пользователя'})


@login_required()
def profile(request):
    img_profile = ProfileImage()
    update_user = UserUpdateForm()

    data = {
        'img_profile': img_profile,
        'update_user': update_user
    }

    return render(request, 'users/profile.html', data)