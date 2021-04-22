from django.shortcuts import render

def index(request):
    return render(request, 'breakNews/index.html', {'title': 'Главная'})

def news(request):
    return render(request, 'breakNews/news.html', {'title': 'Новости'})

def addNews(request):
    return render(request, 'breakNews/add.html', {'title': 'Добавить новость'})

