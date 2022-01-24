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
    created_day = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class BookComment(models.Model):
    books = models.ForeignKey(Book, on_delete=models.CASCADE,
                              related_name="book_comment")
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.books.title


class BookExpert(models.Model):
    ACTIVITY_CHOICE =(
        ('Teacher', "Teacher"),
        ('Student', 'Student'),
        ('Writer', 'Writer'),
        ('Mangaka', 'Mangaka'),
        ('Journalist', 'Journalist'),
        ("IT Developer", "IT Developer"),
    )
    books = models.ForeignKey(Book, on_delete=models.CASCADE,
                              related_name="book_expert")
    full_name_of_Author = models.CharField(max_length=100)
    activity = models.CharField(choices=ACTIVITY_CHOICE, max_length=100)
    personal_info = models.TextField()

    def __str__(self):
        return self.books.title