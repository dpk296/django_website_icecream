# Generated by Django 3.2.3 on 2021-06-27 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('item_name', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]