"""
URL configuration for HousePricePredictionModel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
# from .views import authView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home),
    # path('register/',authView, name="authView"),
    path('',views.login,name='login'),
    path('predict/',views.predict),
    path('signup/',views.signup,name='signup'),
    path('predict/result/',views.result),
    # path("signup/", authView, name="authView"authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
]
