from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Book

# Create your views here.
def loadBook(request):
  books = Book.objects.all()
  return render(request,'ReadBook/Book.html',context={'books':books})

def bookDescription(request,id):
  book = None
  if Book.objects.filter(id=id).exists():
    book = Book.objects.get(id=id)
  return render(request,'ReadBook/BookDescription.html',context={'book':book})

def addBook(request):
  error = None
  if request.method == 'POST':
    try:
      files = request.FILES
      post = request.POST
      user = request.user
      price = post['price'] if post['price'] else 0
      Book.objects.create(book_name=post['name'],book_price=price ,book_type=post['type'],book_cover=files['image'],book_description=post['description'],book_category=post['category'],book_file=files['file'],uploaded_by_id=1) #replace with user.id
    except Exception as e:
      error = "Error While processing the data. This might be because your data is incomplete."
      print("ERROR : "+e)
    else:
      return redirect('premiumbook')

  return render(request,'ReadBook/AddBook.html',context={'error':error})