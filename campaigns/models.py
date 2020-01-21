from django.db import models

class Campaign(models.Model):
    title=models.CharField(max_length=120)
    date=models.CharField(max_length=120)
    price=models.CharField(max_length=120)
    link=models.CharField(max_length=120)
    organizer=models.CharField(max_length=120, default=None)


def __unicode__(self):
    return self.title

def __str__(self):
    return self.title