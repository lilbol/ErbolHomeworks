from django.db import models

class Book(models.Model):
    GENRE_CHOICE = (
        ('Detective', 'Detective'),
        ('Romantic', 'Romantic'),
        ('Fantasy', 'Fantasy'),
        ('Manga', 'Manga')
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    genre = models.CharField(choices=GENRE_CHOICE, max_length=100)
    created_day = models.DateTimeField(auto_now_add=True)
    updated_day = models.DateTimeField(auto_now=True)
