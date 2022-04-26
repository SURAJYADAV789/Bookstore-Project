from django.db import models

# Create your models here.
class Book(models.Model):
    book_id = models.BigAutoField(primary_key=True)
    book_name = models.CharField(max_length=50)
    book_price = models.FloatField()
    book_desc = models.TextField()
    book_image=models.ImageField(upload_to='book_img/',default='NO_image')