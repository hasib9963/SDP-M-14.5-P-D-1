from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = "homepage"),
    path('about/', views.about, name = "aboutpage"),
    path('form/', views.DjangoForm, name = "django_form"),
    # path('form/', views.InputForm, name = "django_form"),
]