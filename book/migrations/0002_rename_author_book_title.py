# Generated by Django 4.0.1 on 2022-01-10 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Author',
            new_name='title',
        ),
    ]
