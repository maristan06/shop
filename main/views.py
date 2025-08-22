from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context: dict = {
        'title': 'Aleteia Jewelry homepage',
        'content': 'Aleteia Jewelry store',
    }

    return render(request, 'main/index.html', context)


def about(request):
    context: dict = {
        'title': 'about us',
        'content': 'About Aleteia Jewelry',
        'text_on_page': """Eye-catching jewelry
            that is hand-crafted from the highest quality
            Japanese glass beads and hypoallergenic stainless steel findings,
            something you will enjoy wearing for a stroll in the city,
            to the office, on a date or a special event -
            the variety of Aleteia creations has no limit!
            Bead by bead with care and attention to detail
            we create jewelry specially for YOU!"""
    }

    return render(request, 'main/about.html', context)
