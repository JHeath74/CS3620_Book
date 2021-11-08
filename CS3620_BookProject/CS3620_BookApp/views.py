from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import BookData
from django.core.paginator import Paginator
from django.template import loader
from .forms import Add_New_Book_Form


# Create your views here.


def booklist(request):
    book_object = BookData.objects.all()
    Book_Category = request.GET.get('Book_Category')
    if Book_Category != '' and Book_Category is not None:
        book_object = book_object.filter(name__icontains=Book_Category)
    paginator = Paginator(book_object, 5)
    page = request.GET.get('page')
    book_object = paginator.get_page(page)
    return render(request, 'CS3620_BookApp/BookList.html', {'book_object': book_object})


def add_new_book(request):
    form = Add_New_Book_Form(request.POST or None)

    if form.is_valid():
        form.save("Book Has Been Saved")
        return redirect('CS3620_BookApp:BookList')

    return render(request, 'CS3620_BookApp/add_new_book_form.html', {'form': form})




