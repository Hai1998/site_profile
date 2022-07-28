from django.db import models


# Create your models here.
class Commercials(models.Model):
    first_text = models.CharField(max_length=15)
    second_text = models.CharField(max_length=50)
    thirst_text = models.CharField(max_length=50)
    image_name = models.CharField(max_length=100)
    commercials_image = models.ImageField(upload_to='images/')
