from django.http import HttpResponse
from django.shortcuts import render
# from .models import ImageForm


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return HttpResponse("This is the contact page.")


def generate(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            path = form.cleaned_data['image']
            pred(path)
            return HttpResponse("Image uploaded successfully.")
    # return render(request, "generate.html")


def faq(request):
    return render(request, "faqs.html")


def pred(path):
    pass

# Path: imageCaptionGenerator/imageCaptionGenerator/urls.py
