from django.db import models
from django.conf import settings

from django.db.models.signals import post_save
# Create your models here.

MEMBERSHIP_CHOICE=(
	('Free','free'),
	('Proffesional','Pro'),
	('Enterprise','Entpr'),
)

#Model for Membership
class Membership(models.Model):
	slug=models.SlugField()
	membership_type=models.CharField(
				choices=MEMBERSHIP_CHOICE,
				default='free',
				max_length=30)
	price=models.IntegerFeild(default=0)
	stripe_plan_id=models.CharFeild(max_length=40)

	def __str__(self):
		return self.membership_type


#Model for UserMembership
class UserMemberShip(models.Model):
	user=OnetoOneFeild(settings.AUTH.USER_MODEL,on_delete=models.CASCADE)
	strip_cust_id=CharFeild(max_length=40)
	membership=ForeignKey(Membership,on_delete=models.SET_NULL,null=True)

	def __str__(self):
		return self.user.username

def user_membership_created(sender,instance,created, *args,**kwargs):
	

class Subscription(models.Model):
	user_membership=models.ForeignKey(UserMembership,on_delete=models.CASCADE)
	stripe_subscription_id=models.CharFeild(max_length=40)
	acive=models.BooleanField(default=True)

	def __str__(self):
		return self.user_membership.user.username