# Generated by Django 3.2.9 on 2022-04-26 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_image',
            field=models.ImageField(default='NO_image', upload_to='book_img/'),
        ),
    ]