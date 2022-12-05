""" 
    A model for the image caption generator. 
    A model is the single, definitive source of information about your data.
    Each model is represented by a class that subclasses django.db.models.Model. Each model has a number of class variables, each of which represents a database field in the model.
"""

from django.db import models


class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.caption
