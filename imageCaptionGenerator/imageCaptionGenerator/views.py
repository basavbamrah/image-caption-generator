from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")
    

def about(request):
    return render(request, "about.html")
def contact(request):
    return HttpResponse("This is the contact page.")
def generate(request):
    return render(request, "generate.html")
def faq(request):
    return render(request, "faqs.html")

# Path: imageCaptionGenerator/imageCaptionGenerator/urls.py