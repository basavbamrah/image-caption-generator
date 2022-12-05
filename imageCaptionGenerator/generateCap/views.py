from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm
from .models import ImageModel
import os
from django.conf import settings
import joblib
import tensorflow as tf
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.applications.xception import Xception


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

def extract_feature(path,model):
    # print(path)
    img=Image.open(path)

    img=img.resize((300,300))
    img=np.array(img)
    if img.shape[2]==4:
        img=img[...,:3]
    img=np.expand_dims(img, axis=0)
    print(img.shape)
    img=img/127.5-1.0
    features=model.predict(img,verbose=0)
    return features
    

def test_word_of_id(idx, tokenizer):
    for word, index in tokenizer.word_index.items():
        if index == idx:
            return word
    return None

def test_generate_caption(model, tokenizer, feature, max_len):
    in_text='start'
    print(max_len)
    for i in range(max_len):
        print(i)
        sequence=tokenizer.texts_to_sequences([in_text])[0]
        sequence=pad_sequences([sequence],maxlen=max_len)
        prediction=model.predict([feature,sequence],verbose=0)
        prediction=np.argmax(prediction)
        word=test_word_of_id(prediction,tokenizer)
        print(word)
        if word is None:
            print("True")
            break
        in_text+=" "+word
        if word=='end':
            break

        # print(in_text)
    return in_text

def pred(path):
    # print(path)

    path = settings.MEDIA_ROOT + '/images/' + str(path)
    print(path)
    max_len=35
    tokenizer = joblib.load(settings.MEDIA_ROOT +'/models/tokenizer.joblib')
    model_lstm = load_model(settings.MEDIA_ROOT + '/models/model_lstm.h5')
    xception=Xception(include_top=False,pooling='avg')
    test_feature=extract_feature(path,xception)
    # print(test_feature.shape)
    print("*******features done***********")
    print(test_feature)
    print("*******features done***********")
    image=Image.open(path)
    caption=test_generate_caption(model_lstm,tokenizer,test_feature,33)
    print(caption)
    # plt.imshow(image)
    return caption
    