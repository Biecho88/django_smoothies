# Generated by Django 3.2.25 on 2024-04-03 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smoothies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='smoothie',
            name='nutrition',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
