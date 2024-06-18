from django.urls import path

from . import views


urlpatterns = [
    path('get_balance', views.get_balance, name='get_balance'),
    path('get_balance_batch', views.get_balance_batch, name='get_balance_batch'),
    path('get_top', views.get_top, name='get_top'),
    path('get_top_with_transactions', views.get_top_with_transactions, name='get_top_with_transactions'),
    path('get_token_info', views.get_token_info, name='get_token_info'),
]
