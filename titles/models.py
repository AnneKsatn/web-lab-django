from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=120, verbose_name='Заголовок')

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

