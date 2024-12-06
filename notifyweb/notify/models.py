from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(auto_created=True, primary_key=True)
    subscribers = models.ManyToManyField('Address', blank=True)

    def __str__(self):
        return self.name


class Address(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    id = models.AutoField(
        auto_created=True,
        primary_key=True
    )
    subscriptions = models.ManyToManyField('Device', blank=True)

    def __str__(self):
        return self.name
