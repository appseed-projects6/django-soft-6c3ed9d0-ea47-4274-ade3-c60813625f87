# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Cats(models.Model):

    #__Cats_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    hide = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)

    #__Cats_FIELDS__END

    class Meta:
        verbose_name        = _("Cats")
        verbose_name_plural = _("Cats")


class Cuser(models.Model):

    #__Cuser_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Cuser_FIELDS__END

    class Meta:
        verbose_name        = _("Cuser")
        verbose_name_plural = _("Cuser")



#__MODELS__END
