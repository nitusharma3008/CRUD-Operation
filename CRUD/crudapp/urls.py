from django.urls import path
from .views import home,ADD, Edit ,Update, Delete

urlpatterns = [
    path('', home , name="home"),
    path('add', ADD, name="add"),
    path('edit', Edit, name="edit"),
    path('update/<str:id>', Update, name="update"),
    path('delete/<str:id>', Delete, name="delete"),
]