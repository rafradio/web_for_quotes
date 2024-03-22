from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="main"),
    path('login', views.lofForm, name="logform"),
    path('projects/<str:pk>', views.projects, name="projects"),
    # path('test', views.test, name="test"),
]