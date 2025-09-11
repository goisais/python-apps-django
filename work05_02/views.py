from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

from django.shortcuts import render

def index(request):
    context = {
        "name": "hukumoto ryosuke"
    }
    return render(request, "index.html", context)
