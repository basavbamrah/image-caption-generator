from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")
    

def about(request):
    return HttpResponse("This is the about page.")
def contact(request):
    return HttpResponse("This is the contact page.")


# Path: imageCaptionGenerator/imageCaptionGenerator/urls.py