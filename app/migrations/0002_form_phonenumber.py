# Generated by Django 3.2.3 on 2021-06-28 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='phonenumber',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]