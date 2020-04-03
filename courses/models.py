from django.db import models

# Create your models here.

class Courses(models.Model):
	name = models.CharField(max_length = 200)
	language = models.CharField(max_length = 200)
	price = models.FloatField()


	def __str__(self):
		return self.name