from django.db import models

class City(models.Model):
    name = models.CharField(max_length=30)

    def __srt__(self):
        return self.name
# Create your models here.


class UserEvent(models.Model):
     title = models.CharField(max_length=50)
     time = models.DateTimeField

     def __srt__(self):
        return self.title
