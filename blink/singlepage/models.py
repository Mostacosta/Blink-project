from django.db import models

# Create your models here.
class philosophy(models.Model):
    image = models.ImageField(upload_to='media')
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class strategy(models.Model):
    image = models.ImageField(upload_to='media')
    title = models.CharField(max_length=100)
    sub_title= models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

class services (models.Model):
    image = models.ImageField(upload_to='media')
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    services = models.CharField(max_length=1000,help_text="put %* between each service")

    def __str__(self):
        return self.title
