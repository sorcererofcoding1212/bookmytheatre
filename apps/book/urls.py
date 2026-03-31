from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('show/<int:s>/', views.CreateShowBookingView.as_view(), name='show')
]
