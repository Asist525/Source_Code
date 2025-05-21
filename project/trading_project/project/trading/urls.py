from django.urls import path
from .views import backtest_page, backtest_view

urlpatterns = [
    path("backtest/", backtest_view), # json API
    path("backtest/view/", backtest_page), 
    #path("auto/", views.auto_trading_view, name="auto_trading"),
]
