# Generated by Django 3.2.3 on 2021-07-01 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210628_1932'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='first_name',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='password',
            new_name='phonenumber',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='last_name',
            new_name='quantity',
        ),
        migrations.RemoveField(
            model_name='register',
            name='email',
        ),
        migrations.RemoveField(
            model_name='register',
            name='username',
        ),
    ]
