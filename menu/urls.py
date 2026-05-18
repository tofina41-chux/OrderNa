from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/book-table/', views.book_table, name='book_table'), # The new API bridge path
]