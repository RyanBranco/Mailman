from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.urls import reverse
from django.db import models

class Package(models.Model):
    origination = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    is_fragile = models.BooleanField()
    destination_length = models.IntegerField(blank=True, null=True)
    cost_of_delivery = models.IntegerField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    users = models.ManyToManyField(User)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pkg_id': self.id})

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    deliveries = models.ForeignKey(Package, on_delete=models.CASCADE, blank=True, null=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()