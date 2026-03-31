from django.urls import path
from . import views

app_name = 'shows'

urlpatterns = [
    path('<int:m>/', views.ShowListView.as_view(), name='shows'),
]
