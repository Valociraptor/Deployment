# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors["name"] = "Name should be more than 2 characters"
        if len(postData['email']) < 10:
            errors["email"] = "Email should be more than 5 characters"
        return errors


class User(models.Model):
    
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    

    def __str__(self):
        return self.name