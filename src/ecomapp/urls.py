from django.urls import path
from django_filters.views import FilterView

from . import views
from django.contrib.auth.views import login,logout
from .filters import ProductFilter

app_name = 'ecomapp'

urlpatterns = [
    path('', views.ProdIndexView.as_view() ,name='index'),
    path('<int:pk>/', views.ProdDetailView.as_view(), name='detail'),
    path('<int:pk>/prod_delete/', views.ProdDeleteView.as_view(), name='delete_prod'),
    path('prod_create/', views.ProdCreateView.as_view(), name='prod_create'),
    path('<int:pk>/prod_update/', views.ProdUpdateView.as_view(), name='prod_update'),
    path('search/', views.search, name='search'),
    path('search2/', views.search2, name='search2'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogOutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]


