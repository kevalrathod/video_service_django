from django.db import models

from membership.models import Membership


# Create your models here.

class Courses(models.Model):
	slug=models.SlugField()
	title=models.CharField(max_length=50)
	description=models.TextField(max_length=100)
	allowed_memberships=models.ManyToManyField(Membership)

	def __str__(self):
		return self.title


class Lession(models.Model):
	slug= models.SlugField()
	title=models.CharField(max_length=120)
	course=models.ForeignKey(Courses,on_delete=models.CASCADE)
	poition=models.IntegerField()
	video_url=models.CharField(max_length=200)
	thumbnail=models.ImageField()

	def __str__(self):
		return self.title