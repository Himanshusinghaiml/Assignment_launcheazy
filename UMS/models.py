from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    name = models.CharField(max_length=100)
    billing_group = models.CharField(max_length=20, choices=[('free', 'Free'), ('pro', 'Pro'), ('premium', 'Premium')])

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=50)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

class MembershipRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)

class BillingGroup(models.Model):
    name = models.CharField(max_length=20)
    organization = models.OneToOneField(Organization, on_delete=models.CASCADE, related_name='billing_group_information')
