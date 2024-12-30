from django.urls import path
from .views import BurgerListView

urlpatterns = [
    path('burgers/', BurgerListView.as_view(), name='burger-list'),
]
