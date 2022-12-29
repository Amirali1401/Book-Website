from django import forms

from .models import Comment , Book


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ( 'text' ,)





class CreateBookForm(forms.ModelForm):
     class Meta:
         model = Book
         fields = ('title' , 'content' ,'writer' , 'translator', 'institute' , 'covers' )