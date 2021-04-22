from django.shortcuts import render

def index(request):
    return render(request, 'breakNews/index.html')
