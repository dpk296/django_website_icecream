# Generated by Django 3.2.3 on 2021-06-28 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_name_form_first_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='form',
            new_name='register',
        ),
    ]