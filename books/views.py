from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin 
)
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from .models import Book, Basket
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


class BookListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/book_list.html"
    login_url = "account_login"


class BookDetailView(
        # LoginRequiredMixin,
        # PermissionRequiredMixin,
        DetailView):
    model = Book
    context_object_name = "book"
    template_name = "books/book_detail.html"
    login_url = "account_login"
    # permission_required = "books.special_status"
    queryset = Book.objects.all().prefetch_related('reviews__author',)


class SearchResultsListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/search_results.html"
    
    def get_queryset(self):
        query = self.request.GET.get("q")
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )

@login_required
def basket_add(request, book_id):
    book = Book.objects.get(id=book_id)
    basket = Basket.objects.filter(user=request.user, book=book)

    if not basket.exists():
        Basket.objects.create(user=request.user, book=book, quantity=1)
    else:
        basket = basket.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def basket(request):
    basket = Basket.objects.filter(user=request.user)
    return render(request, 'books/basket.html', {'basket': basket})


