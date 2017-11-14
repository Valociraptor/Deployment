# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.


class UserManager(models.Manager):
    def validate(self, postData):
        errors = []
        if len(postData['name']) < 2:
            errors["name"] = "Name should be more than 2 characters"
        if len(postData['email']) < 8:
            errors["email"] = "Email must be at least 9 characters"
        if postData["password"]  != postData["cpassword"]:
            errors["password"] = "Passwords must match!" 

        if not "email" in errors and not re.match(EMAIL_REGEX, postData['email']):
            errors['email'] = "invalid email"
        
        # if email is valid check db for existing email
        else:
            if len(self.filter(email=postData['email'])) > 1:
                errors['email'] = "email already in use"

        return errors


    def loginvalidate(self, postData):
        errors = []
        # check DB for post_data['email']
        if len(self.filter(email=postData['email'])) > 0:
            # check this user's password
            user = self.filter(email=postData['email'])[0]
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors.append('email/password incorrect')
        else:
            errors.append('email/password incorrect')

        if errors:
            return errors
        return user           







class User(models.Model):
    
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    

    def __str__(self):
        return self.name