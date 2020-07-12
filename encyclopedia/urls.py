from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.title, name="title"),
    path("createpage", views.add_page, name="add_page"),
    path("wiki/edit/<str:edit_title>", views.edit, name="edit_title"),
    path("random_page", views.rand, name="random"),
    path("search", views.search, name="search")

]
