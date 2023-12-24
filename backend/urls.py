from django.urls import path
from . import views


urlpatterns = [
    path('<str:GroupName>/',views.home_loader)

]
