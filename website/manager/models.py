from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
	user = models.ForeignKey(User, default=1)
	name = models.CharField(max_length=200)
	number = models.IntegerField()

	def __str__(self):
		return self.name + ' - ' + str(self.number)

	class Meta:
		ordering = ['pk']	