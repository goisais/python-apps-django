from django.shortcuts import render


def work05_index(request):
    return render(request, "work05_02/templates/index.html")


def work06_index(request):
    return render(request, "work06/templates/index.html")


def work07_index(request):
    return render(request, "work07/templates/index.html")


def facebank_index(request):
    return render(request, "bankapp/templates/index.html")
