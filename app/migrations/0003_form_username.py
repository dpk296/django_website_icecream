# Generated by Django 3.2.3 on 2021-06-28 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_form_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='username',
            field=models.CharField(default=0, max_length=254),
            preserve_default=False,
        ),
    ]
