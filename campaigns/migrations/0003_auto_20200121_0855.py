# Generated by Django 2.2.6 on 2020-01-21 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0002_campaign_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='link',
            field=models.CharField(max_length=120),
        ),
    ]