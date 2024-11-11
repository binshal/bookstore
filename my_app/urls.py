from django.urls import path
from . import views


urlpatterns = [
   path("createbook/",views.createbook,name='createbook'),
   path("adminview/",views.listbook,name='booklist'),
   path("detailsView/<int:book_id>/",views.detailsView,name='details'),
   path("updateview/<int:book_id>/",views.updateView,name='update'),
   path('deleteview/<int:book_id>/',views.deleteView,name='delete'),
   path('author/',views.createauthor,name='author'),
   path('index/',views.index),
   path('search/',views.SearchBook,name='search'),
  
]
