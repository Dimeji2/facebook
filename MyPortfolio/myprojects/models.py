from django.db import models
from django.utils import timezone
class Project(models.Model):
	title=models.CharField(max_length=100)
	description=models.TextField()
	date_uploaded=models.DateField(default=timezone.now().strftime('%y-%m-%d'))
	technology=models.CharField(max_length=50)
	image=models.FilePathField(path='/img')
# Create your models here.
