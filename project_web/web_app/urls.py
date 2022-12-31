from django.urls import path, re_path
from . import views

urlpatterns = [
    path("home/", views.homepage, name="home"),
    path("income/", views.income, name="income"),
    path("calculate/", views.calculate, name="calc"),
    path("contact_form/", views.contact_form, name="contact"),
    path("contact_sent/", views.contact_sent, name="processing"),
    path("our_projects/", views.Objects.as_view(), name="apps"),
    path("our_services/", views.TableData.as_view(), name="services")
]