# Generated by Django 3.0.2 on 2020-02-06 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Article',
            new_name='Articles',
        ),
    ]
