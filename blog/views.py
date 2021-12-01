from django.shortcuts import render
from .models import News

news = [
    {
        'title': 'First news',
        'text': 'ВОЗ назвала новый штамм коронавируса вызывающим беспокойство.'
                'У него больше мутаций, чем известно науке о других вариантах, пояснили в организации',
        'date': ' 26.11.2021',
        'autor': 'https://www.kp.ru/online/news/'


    },
    {
        'title': 'Second news',
        'text': 'Some big 2 text',
        'date': ' 23.11.2021'

    }
]

def home(request):
    data = {
        'news': News.objects.all(),
        'title':'Главная страница блога'
    }
    return render(request,'blog/home.html', data)

def contacts(request):
    return render(request,'blog/contacts.html',{'title': 'О нас'})
