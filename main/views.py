from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context: dict = {
        'title': 'Home',
        'content': 'main page HOME',
    }

    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('about page')
