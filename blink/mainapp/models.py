from django.db import models

# Create your models here.
class home_cover(models.Model):

 image = models.ImageField(upload_to="media")
 title=models.CharField(max_length=100)
 description=models.CharField(max_length=500)

 def __str__(self):
  return self.title

class project (models.Model):
 title = models.CharField(max_length=100)
 sub_title = models.CharField(max_length=100)
 description = models.CharField(max_length=1000)
 client = models.CharField(max_length=100,blank=True)
 location = models.CharField(max_length=100,blank=True)
 sector = models.CharField(max_length=100, blank=True)
 essence = models.CharField(max_length=100, blank=True)
 stories = models.CharField(max_length=500, blank=True,help_text="put *% between each story")
 home_image = models.ImageField(upload_to="media")
 project_cover = models.ImageField(upload_to="media")

 def __str__(self):
  return self.title

class project_image (models.Model):
 project_images = models.ForeignKey(project,on_delete=models.CASCADE)
 image = models.ImageField(upload_to="project_image")

 def __str__(self):
  return self.project_images.title
