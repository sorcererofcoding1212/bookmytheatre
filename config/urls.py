from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.pages.urls')),
    path('users/', include('apps.users.urls')),
    path('shows/', include('apps.shows.urls')),
    path('movies/', include('apps.movies.urls')),
    path('core/', include('apps.core.urls')),
    path('book/', include('apps.book.urls')),
    path('admin/', admin.site.urls),
]
