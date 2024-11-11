from itertools import product
from lib2to3.fixes.fix_input import context

from django.conf import settings
from django.db.models.fields import return_None
from django.shortcuts import render, redirect
from django.urls import reverse

from my_app.models import book, Author
from my_app.forms import BookForm,AuthorForm
from django.db.models import Q
from . models import Cart,CartItem
from account_app.models import UserProfile
from django.contrib.auth.models import User
import stripe



# Create your views here.

def UserPage(request):


    return render(request,'user/user.html')

def Bookdetail(request,book_id):
    books = book.objects.get(id=book_id)
    return render(request,'user/userbookdetails.html',{'book':books})

def UserBookList(request):
    Book = book.objects.all()
    return render(request, 'user/userbooklist.html', {'books': Book})

def UserSearchBook(request):
    query = None
    books = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        books = book.objects.filter(Q(title__icontains=query) | Q(author__name__icontains=query))

    else :
        books = []

    context = {'books':books,'query':query}

    return render(request,'user/usersearch.html',context)

def add_to_cart(request,book_id):
    Book = book.objects.get(id=book_id)

    if Book.quantity>0:
        user_profile = UserProfile.objects.get(username=request.user.username)
        cart,created =Cart.objects.get_or_create(user=user_profile)
        cart_item,item_created = CartItem.objects.get_or_create(cart=cart,book=Book)

        if not item_created:
            cart_item.quantity+=1
            cart_item.save()


    return redirect('viewcart')

def view_cart(request):
    user_profile = UserProfile.objects.get(username=request.user.username)
    cart,created = Cart.objects.get_or_create(user=user_profile)
    # cart_items = cart.CartItem.set.all()
    cart_items = CartItem.objects.filter(cart=cart)
    cart_item = CartItem.objects.all()
    total_price = sum(item.book.price*item.quantity for item in cart_items)
    total_items = cart_items.count()

    context = {'cart_items':cart_items,'cart_item':cart_item,'total_price':total_price,'total_items':total_items}
    return render(request,'user/cart.html',context)

def increase_quantity(request,item_id):
    cart_item = CartItem.objects.get(id=item_id)
    if cart_item.quantity<cart_item.book.quantity:
        cart_item.quantity+=1
        cart_item.save()

    return redirect('viewcart')

def decrease_quantity(request,item_id):
    cart_item = CartItem.objects.get(id=item_id)
    if cart_item.quantity >1:
        cart_item.quantity -= 1
        cart_item.save()
    return redirect('viewcart')

def remove_from_cart(request,item_id):
    try:
        cart_item = CartItem.objects.get(id=item_id)
        cart_item.delete()
    except cart_item.DoesNotExist:
        pass

    return redirect('viewcart')


def create_checkout_session(request):
    cart_items = CartItem.objects.all()
    if cart_items:
        stripe.api_key = settings.STRIPE_SECRET_KEY
        if request.method=='POST':
            line_items = []
            for cart_item in cart_items:
                if cart_item.book:
                    line_item = {
                        'price_data':{
                            'currency':'INR',
                            'unit_amount':int(cart_item.book.price*100),
                            'product_data':{
                                'name':cart_item.book.title
                            },
                        },
                        'quantity':cart_item.quantity
                    }
                    line_items.append(line_item)
            if line_items:
                checkout_session = stripe.checkout.Session.create(
                    payment_method_types = ['card'],
                    line_items = line_items,
                    mode = 'payment',
                    success_url = request.build_absolute_uri(reverse('success')),
                    cancel_url = request.build_absolute_uri(reverse('cancel'))
                )
                return redirect(checkout_session.url,code=303)

def success(request):
    cart_items = CartItem.objects.all()
    for cart_item in cart_items:
        product = cart_item.book
        if product.quantity >= cart_item.quantity:
            product.quantity -= cart_item.quantity
            product.save()

    cart_items.delete()
    return render(request,'user/success.html')

def cancel(request):
    return render(request,'cancel.html')
