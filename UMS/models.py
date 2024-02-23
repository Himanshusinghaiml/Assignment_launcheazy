
from django.db import models
from django.contrib.auth.models import AbstractUser

class Organization(models.Model):
    name = models.CharField(max_length=100)
    billing_group = models.CharField(max_length=50, choices=[('free', 'Free'), ('pro', 'Pro'), ('premium', 'Premium')])
    # Other organization fields...

class Role(models.Model):
    name = models.CharField(max_length=50)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    # Other role fields...

# class User(AbstractUser):
#     organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
#     roles = models.ManyToManyField(Role)
#     # Other user fields...

# class MembershipRequest(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
#     is_approved = models.BooleanField(default=False)
#     # Other membership request fields...
# class himanshu(models.Model):
#     name=models.CharField()
