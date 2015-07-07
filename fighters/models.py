from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class Fighter(models.Model):
	name = models.CharField(max_length=100)	
	created = models.DateTimeField(auto_now_add=True)
	user = models.OneToOneField('auth.User', null=True)
	is_newbie = models.BooleanField(default=True)
	is_fighter = models.BooleanField(default=False)
	is_archer = models.BooleanField(default=False)
	is_trainer = models.BooleanField(default=False)
	can_post_notifications = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)



class PracticeSession(models.Model):
	description = models.CharField(max_length=200, blank=True)
	date = models.DateField()
	session_type = models.CharField(max_length=20)
	full_attendance = models.ManyToManyField(Fighter, related_name='full_attendance')
	half_attendance = models.ManyToManyField(Fighter, related_name='half_attendance')

#Add token to users as they are created
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
