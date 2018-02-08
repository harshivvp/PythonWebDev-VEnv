from django.urls import path
from . import views
from django.contrib.auth.views import login,logout

app_name = 'ecomapp'

urlpatterns = [
    path('', views.ProdIndexView.as_view() ,name='index'),
    path('<int:pk>/', views.ProdDetailView.as_view(), name='detail'),
    path('<int:pk>/prod_delete/', views.ProdDeleteView.as_view(), name='delete_prod'),
    path('prod_create/', views.ProdCreateView.as_view(), name='prod_create'),
    path('<int:pk>/prod_update/', views.ProdUpdateView.as_view(), name='prod_update'),
    path('search/', views.search_prod_new, name='search'),

    # path('/accounts/login/', login, {'template_name':'accounts/login.html'}),
        # path('logout/', logout, {'template_name': 'accounts/login.html'}),

]


