from django.db import models
from django.conf import settings

from django.db.models.signals import post_save

import stripe
stripe.api_key=settings.STRIPE_SECRET_KEY
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
    price=models.IntegerField(default=0)
    stripe_plan_id=models.CharField(max_length=40)

    def __str__(self):
        return self.membership_type


#Model for UserMembership
class UserMembership(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    stripe_cust_id=models.CharField(max_length=40)
    membership=models.ForeignKey(Membership,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.user.username

#post_save signals implement method to send to the sender as a instance of cust_id if not then it will create new
def user_membership_created(sender,instance,created, *args,**kwargs):
    if created:
        UserMembership.objects.get_or_create(user=instance)

    user_membership, created = UserMembership.objects.get_or_create(user=instance)

    if user_membership.stripe_cust_id is None or user_membership.stripe_cust_id=='':
        new_cust_id = stripe.Customer.create(email=instance.email)
        user_membership.stripe_cust_id=new_cust_id['id']
        user_membership.save()

post_save.connect(user_membership_created,sender=settings.AUTH_USER_MODEL)


#Subscription model
class Subscription(models.Model):
    user_membership=models.ForeignKey(UserMembership,on_delete=models.CASCADE)
    stripe_subscription_id=models.CharField(max_length=40)
    acive=models.BooleanField(default=True)

    def __str__(self):
        return self.user_membership.user.username
        