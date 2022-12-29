from django.urls import path

from . import views as book_views

app_name = 'book'

urlpatterns = [
    path('', book_views.index , name = 'index'),
    path('<int:book_id>/detail_view_book/', book_views.detail_view_book , name = 'detail_books'),
    path('<int:book_id>/create_comment/', book_views.CreateCommentBook.as_view() , name = 'create_comment'),
    ]