from django.db import models

# Create your models here.

class Note(models.Model):
	id = models.IntegerField(primary_key=True)
	title = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	dueDate =  models.CharField(max_length=10,blank=True)

	def _str_(self):
		return self.title