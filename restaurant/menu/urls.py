from django.urls import path
from menu import views

urlpatterns=[
    path('food',views.func1,name="fd")
]