from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm
from .models import ImageModel
import os
from django.conf import settings
import joblib

# Create your views here.
def index(request):
    return render(request, "generateCap/index.html")
    # return HttpResponse("This is the home page.")

def generate(request):
    '''' Accepts the image and returns the caption'''
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        print('yes')
        print(form.is_valid())
        if form.is_valid():
            print('yes')
            form.save()
            path = form.cleaned_data['image']
            cap=pred(path)
            # return HttpResponse("Image uploaded successfully.")

    return render(request, "generateCap/index.html")

def pred(path):
    # print(path)

    path=settings.MEDIA_ROOT + '/images/' + str(path)
    # print(path)
    


    