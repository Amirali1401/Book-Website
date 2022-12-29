from django.shortcuts import render , get_object_or_404 , reverse , redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Book , Comment
from .forms import CommentForm , CreateBookForm

# Create your views here.



def index(request):
    books = Book.objects.all()
    return render(request , 'Book/index_1.html' , context = {'books':books})





class CreateViewBook(LoginRequiredMixin , generic.CreateView ):
     template_name = 'Book/create_view_book.html'
     model = Book
     fields = ('title' , 'content' , 'covers')

     def form_valid(self, form):
        obj_form = form.save(commit=False)
        obj_form.user = self.request.user
        form.save()
        return super().form_valid(form)


@login_required
def detail_view_book(request , book_id):
     book = Book.objects.get(id = book_id)
     book_comments = book.comments.all()
     form = CommentForm(request.POST)

     return render(request , 'Book/detail_view_books.html' , context={'books':book , 'comments':book_comments , 'comment_form':form})



class CreateCommentBook(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse('book:index')

    def form_valid(self, form):
        obj_form = form.save(commit=False)
        obj_form.user = self.request.user
        book_id = int(self.kwargs['book_id'])
        book = get_object_or_404(Book , id = book_id)
        obj_form.book = book
        return super().form_valid(form)




