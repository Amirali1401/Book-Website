# Generated by Django 4.1.4 on 2022-12-29 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0006_alter_book_covers_alter_book_stars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='user',
        ),
    ]
