from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your models here.



class  Book(models.Model):

    CHOICE_STARS = (
        ('1' , 'خیلی بد'),
        ('2' , 'بد'),
        ('3' , 'متوسط'),
        ('4' , 'خوب'),
        ('5' , 'خیلی خوب'),
    )

    user = models.ForeignKey(User , on_delete = models.CASCADE)

    title = models.CharField(max_length = 200 )
    content = models.TextField()
    writer = models.CharField(max_length=150 )
    translator = models.CharField(max_length = 200)
    institute = models.CharField(max_length = 350)
    stars = models.CharField(max_length = 15 , choices=CHOICE_STARS)
    covers = models.ImageField(upload_to='covers/' , null = True)
    date_created = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} : {self.title}'



    def get_absolute_url(self):

        return reverse('book:detail_books' , args = [self.id])







class Comment(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    book = models.ForeignKey(Book , on_delete = models.CASCADE , related_name = 'comments')
    text = models.TextField()

    date_created = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} : {self.id}'

