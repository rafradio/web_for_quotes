from django.urls import path, include
from . import views
from .LogTemplateView import LogTemplateView

urlpatterns = [
    path('', views.index, name="main"),
    # path('login', views.logForm, name="logform"),
    path('projects/<str:pk>', views.projects, name="projects"),
    path('logintest', LogTemplateView.as_view(), name="testform"),
    # path('test', views.test, name="test"),
]