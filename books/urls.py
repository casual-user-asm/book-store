from django.urls import path

from .views import BookListView, BookDetailView, SearchResultsListView, basket_add, basket_remove, basket

app_name = "books"

urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("<uuid:pk>", BookDetailView.as_view(), name="book_detail"),
    path("search/", SearchResultsListView.as_view(), name="search_results"),
    path("basket_add/<uuid:book_id>", basket_add, name="basket_add"),
    path("basket_remove/<int:basket_id>", basket_remove, name="basket_remove"),
    path("basket/", basket, name="basket"),
]