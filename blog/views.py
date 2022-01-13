from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import News


class ShowNewsView(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 1

    def get_context_data(self, **kwards):
        ctx = super(ShowNewsView,self).get_context_data(**kwards)
        ctx['title'] = 'Главная страница блога'
        return ctx

class UserAllNewsView(ListView):
    model = News
    template_name = 'blog/user_news.html'
    context_object_name = 'news'
    paginate_by = 1

    def get_queryset(self):
        user = get_object_or_404(User,username = self.kwargs.get('username'))
        return News.objects.filter(autor=user).order_by('-date')

    def get_context_data(self, **kwards):
        ctx = super(ShowNewsView,self).get_context_data(**kwards)
        ctx['title'] = 'Главная страница блога'
        return ctx


class NewsDetailView(DetailView):
    model = News
    context_object_name = 'post'

    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView,self).get_context_data(**kwards)
        ctx['title'] = News.objects.filter(pk=self.kwargs['pk']).first()
        return ctx

class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.autor:
            return True
        return False


class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.autor:
            return True
        return False

class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.autor=self.request.user
        return super().form_valid(form)


def home(request):
    data = {
        'news': News.objects.all(),
        'title': 'Главная страница сайта'
    }
    return render(request,'blog/home.html', data)

def contacts(request):
    return render(request, 'blog/contacts.html', {'title': 'О нас'})
