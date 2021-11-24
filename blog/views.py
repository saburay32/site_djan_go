from django.shortcuts import render
from django.http import HttpResponse

news = [
    {
        'title': 'First news',
        'text': 'Some text',
        'date': '23.11.2021',
        'autor': 'Georgiy'

    },
    {
        'title': 'Second news',
        'text': 'Some big 2 text',
        'date': '23.11.2021'

    }
]

def home(request):
    data = {
        'news': news,
        'title':'Главная страница блога'
    }
    return render(request,'blog/home.html', data)

def contacts(request):
    return render(request,'blog/contacts.html',{'title': 'О нас'})
