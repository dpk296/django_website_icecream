from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("register",views.register,name="register"),
    path("home",views.home,name="home"),
    path("login",views.login,name="home"),
    path("logout",views.logout,name="home"),
    # path("buy",views.buy,name="buy"),
    path("makeadeal",views.makeadeal,name="makeadeal"),
    path("orders",views.orders,name="orders"),
    path("buy1",views.buy1,name="buy1"),
]
