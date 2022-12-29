# Generated by Django 4.1.4 on 2022-12-29 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0004_book_institute_book_translator'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='stars',
            field=models.CharField(choices=[('خیلی بد', '1'), ('بد', '2'), ('متوسظ', '3'), ('خوب', '4'), ('خیلی خوب', '5')], default=1, max_length=15),
            preserve_default=False,
        ),
    ]
