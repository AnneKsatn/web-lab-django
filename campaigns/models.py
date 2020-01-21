from django.db import models

class Campaign(models.Model):
    title=models.CharField(max_length=120)
    start_date=models.DateField()
    end_date=models.DateField()
    price=models.CharField(max_length=120)
    link=models.CharField(max_length=120)
    organizer=models.CharField(max_length=120)


def __unicode__(self):
    return self.title

def __str__(self):
    return self.title

