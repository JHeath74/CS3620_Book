from django.db import models


# Create your models here.

class BookData(models.Model):

    def __str__(self):
        return self.Book_Name

    Book_Name = models.CharField(max_length=200)
    Book_Category = models.CharField(max_length=200)
    Book_ISBN = models.CharField(max_length=100)
    Book_Description = models.CharField(max_length=200)
    Book_Rating = models.FloatField()
    Book_Image = models.ImageField(upload_to='Images')
