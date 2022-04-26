from django.shortcuts import render
from multiprocessing import context
from django.urls import reverse_lazy
from django.views.generic import *
from book.forms import BookForm
from .models import *
from book.models import Book

# Create your views here.
def home(req):
    return render(req,'book/home.html')

def customer_books(req):
    book=Book.objects.all()
    context={'book':book}
    return render(req,'customer/books.html',context)

class BookCreateView(CreateView):
    model = Book
    form_class=BookForm
    template_name = 'book/books.html'
    success_url = reverse_lazy('books')
    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        data = super().get_context_data()
        
        data['book_list'] = Book.objects.all()
        data.setdefault('action','add')
        return data    


class BookView(ListView):
    template_name = 'book/books.html'
    model = Book
    context_object_name='book_list'


class BookUpdateView(UpdateView):
    model = Book
    template_name = "book/books.html"
    form_class=BookForm
    success_url=reverse_lazy('books')

    def get_context_data(self,**kwargs):
        data = super().get_context_data()
        data['action']='update'
        data['book_list']=Book.objects.all()
        return  data

class BookDeleteView(DeleteView):
    model=Book
    success_url=reverse_lazy('books')

class BookDetailView(DetailView):
    model=Book
    template_name='book/books.html'

    def get_context_data(self,**kwargs):
        data = super().get_context_data()
        print("data",data,type(data))
        # data['product']=Product.objects.get()
        data['action']='detail'
        return  data

