from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('C', 'Custom'),
    )
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    user_name = models.CharField(blank=True, max_length=255)
    profile_photo = models.ImageField(blank=True)
    website = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    email = models.CharField(blank=True, max_length=255)
    photo_number = models.CharField(blank=True, max_length=255)
    gender = models.CharField(blank=True, choices=GENDER_CHOICES,max_length=255)
    followers = models.ManyToManyField("self")
    following = models.ManyToManyField("self")

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
