# Generated by Django 4.0.1 on 2022-01-14 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_rename_author_book_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('Detective', 'Detective'), ('Romantic', 'Romantic'), ('Fantasy', 'Fantasy'), ('Manga', 'Manga')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]
