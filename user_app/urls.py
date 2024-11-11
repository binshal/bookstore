from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .import views




urlpatterns = [
    path('usernav/',views.UserPage,name='usernav'),
    path('UserBookDetails/<int:book_id>',views.Bookdetail,name='userbookdetails'),
    path('user/',views.UserBookList,name='userbooklist'),
    path('usersearch/',views.UserSearchBook,name='usersearch'),
    path('add_to_cart/<int:book_id>',views.add_to_cart,name='addtocart'),
    path('view-cart/',views.view_cart,name='viewcart'),
    path('increase/<int:item_id>',views.increase_quantity,name='increase_quantity'),
    path('decrease/<int:item_id>',views.decrease_quantity,name='decrease_quantity'),
    path('view-cart/<int:item_id>',views.remove_from_cart,name='remove_cart'),
    path('create-checkout-session/',views.create_checkout_session,name='create-checkout-session'),
    path('success/',views.success,name='success'),
    path('cancel/',views.success,name='cancel'),
]