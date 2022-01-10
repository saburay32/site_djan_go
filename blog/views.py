from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import News


class ShowNewsView(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'news'
    ordering = ['-date']

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


class CreateNewsView(CreateView):
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
