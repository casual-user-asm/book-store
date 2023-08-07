from books.models import Book
from django.views.generic import ListView, TemplateView

class HomePageView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"