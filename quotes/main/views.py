from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from .models import TestUsers, TestProjects
from .MyLogger import MyLogger
from django.db import connection

def index(request):
    testUsers = TestUsers.objects.all()
    myUsers = list(testUsers)
    print(myUsers[1].name)
    return HttpResponse("<h2>Hello world!</h2>")

def checkUSer(cd):
    with connection.cursor() as cursor:
        val = cd['username']
        cursor.execute("SELECT password FROM users WHERE users.email = %s", [val])
        row = cursor.fetchone()
    print(row[0])
    return row[0] == cd['password']

def projects(request, pk):
    if pk == "Allowed":
        testProjects = TestProjects.objects.all()
        data = {'projects': testProjects}
        myUsers = list(testProjects)
        print(myUsers[1].title)
        return render(request, 'main/projects.html', data)
    else:
        redirect('logform')