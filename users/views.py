from django.shortcuts import render, redirect
from .forms import UserReg
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = UserReg(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} был успешно создан')
            return redirect('blog-home')

    else:
        form = UserReg()
    return render(request, 'users/registration.html', {'form': form, 'title': 'Регистрация пользователя'})
