from django.db import models
from localflavor.us.forms import USStateField

import re

class AppointmentManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        if len(postData['fname']) < 2:
            errors["fname"] = "Your first name should be at least 2 characters."
        if len(postData['lname']) < 2:
            errors["lname"] = "Your last name should be at least 2 characters."
        if len(postData['pname']) < 2:
            errors["pname"] = "Your pet's name should be at least 2 characters."
        # if len(postData['pname_two']) < 2:
        #     errors["pname"] = "Your pet's name should be at least 2 characters."
        if len(postData['phone']) > 10:
            errors["phone"] = "A 10-digit number is required."

        if len(postData['preferred_date']) == 0:
            errors['preferred_date'] = "Please specify a date."
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Please enter a valid email address."

        PHONE_REGEX = re.compile(r'[0-9]')
        if not PHONE_REGEX.match(postData['phone']):
            errors['phone'] = "Please enter a valid phone number."

        return errors

    def mod_validator(self,postData):
        errors = {}
        if len(postData['preferred_date']) == 0:
            errors['preferred_date'] = "Please specify a date."
        if postData['preferred_time'] == "1":
            errors['preferred_time'] = "Please specify a time."
        return errors

class Appointment(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    pname = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    preferred_date = models.DateField(auto_now_add=False)
    preferred_time = models.CharField(max_length=30)
    confirmation = models.CharField(max_length=6, default="CONFIR")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AppointmentManager()


class UserPet(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    address = models.EmailField(max_length=100)
    address2 = models.EmailField(max_length=100)
    city = models.EmailField(max_length=50)
    state = USStateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)