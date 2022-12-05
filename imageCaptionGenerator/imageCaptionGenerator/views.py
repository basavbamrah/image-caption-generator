from django.http import HttpResponse
from django.shortcuts import render
# from .models import ImageForm


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return HttpResponse("This is the contact page.")




def faq(request):
    return render(request, "faqs.html")


def pred(path):
    pass

# Path: imageCaptionGenerator/imageCaptionGenerator/urls.py
