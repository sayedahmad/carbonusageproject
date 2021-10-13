from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)+" "+self.name
