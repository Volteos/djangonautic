# Generated by Django 3.0.2 on 2020-02-06 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200206_0539'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Articles',
            new_name='Article',
        ),
    ]