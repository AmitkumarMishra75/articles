from django.db import models

# Create your models here.
class Articles(models.Model):
    heading = models.CharField(max_length=256)
    content = models.CharField(max_length=1024)

    def __str__(self):
        return self.heading