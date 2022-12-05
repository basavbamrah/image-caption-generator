from django.db import models


class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.caption
