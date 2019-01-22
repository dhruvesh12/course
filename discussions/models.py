from django.db import models
from api.models import lession

# Create your models here.


class discus(models.Model):

	name=models.CharField(max_length=100)
	text=models.CharField(max_length=100)
	lessions=models.ForeignKey(lession, related_name='cat_subject', on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.name
