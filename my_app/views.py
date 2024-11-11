from django.shortcuts import render
from django.http import HttpResponse
from .models import book
from django.contrib import messages
from django.shortcuts import redirect
from .forms import AuthorForm,BookForm
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth


# Create your views here.
# def createbook(request):

#     Books=book.objects.all()
#     if request.method=='POST':

#         title=request.POST.get("title")
#         price=request.POST.get("price")

#         Book=book(title=title,price=price)

#         Book.save()

#     return render(request,'book.html',{'books':Books})

def listbook(request):

    Books=book.objects.all()

    paginator = Paginator(Books,4)
    page_number = request.GET.get('page')

    try:
        page = paginator.get_page(page_number)

    except EmptyPage:
        page = paginator.page(page_number.num_pages)

    return render(request,'listbook.html',{'books':Books,'page':page})

def detailsView(request,book_id):
    books = book.objects.get(id=book_id)
    return render(request,'detailsview.html',{'book':books})

def updateView(request,book_id):
    Book=book.objects.get(id=book_id)

    if request.method=='POST':
        form=BookForm(request.POST,request.FILES,instance=Book)
        

        if form.is_valid():
            form.save()
            return redirect('booklist')
            
    else:
        form=BookForm(instance=Book)
    return render(request,'updateview.html',{'form':form})

def deleteView(request,book_id):

    Book=book.objects.get(id=book_id)
    if request.method == 'POST':

        Book.delete()
        return redirect('/')

    return render(request,'deleteview.html',{'book':Book})

def createbook(request):

    Book=book.objects.all()

    if request.method=='POST':
        form=BookForm(request.POST,request.FILES)
        

        if form.is_valid():
            form.save()
            return redirect('/')
            
    else:
        form=BookForm()

    return render(request,'book.html',{'form':form,'books':Book})


def createauthor(request):
    if request.method=='POST':

        form =AuthorForm(request.POST)

        if form.is_valid:
            form.save()

            return redirect('createbook')
        
    else:
        form = AuthorForm()

    return render(request,'author.html',{'form':form})


def index(request):
    return render(request,'base.html')

def SearchBook(request):
    query = None
    books = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        books = book.objects.filter(Q(title__icontains=query) | Q(author__name__icontains=query))

    else :
        books = []

    context = {'books':books,'query':query}

    return render(request,'search.html',context)




