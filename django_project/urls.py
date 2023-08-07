from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("anything-but-admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("pages.urls")),
    path("books/", include(("books.urls", 'books'))),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)