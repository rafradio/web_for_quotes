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

def logForm(request):
    # testUsers = TestUsers.objects.all()
    MyLogger.configure()
    clientip = f'{request.get_full_path()}; {request.headers["User-Agent"]}; {request.method};'
    d = {'clientip': clientip}
    MyLogger.logger.info('Start work', extra = d)
    message = ""
    visibility = "block"
    visibility1 = "none"
    htmlTitle="Log-in"
    form = LoginForm()
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            testUser = TestUsers.objects.get(email=cd['username'])
            if cd['password'] == testUser.password: 
                clientip = f'"Пароль введен верно"; {testUser.name}; {testUser.email}'
                d = {'clientip': clientip}
                MyLogger.logger.info('Password entering', extra = d)
                visibility = "none"
                visibility1 = "flex"
                htmlTitle="Информация для квот"
                message = "Пароль введен правильно" if cd['password'] == testUser.password else "Пароль введен не правильно"
                testProjects = TestProjects.objects.all()
                usersAll = TestUsers.objects.all()
                data = {
                    'data': testProjects,
                    'users': usersAll,
                    'message': message,
                    'htmlTitle': htmlTitle,
                    'visibility': visibility,
                    'visibility1': visibility1,
                }
                return render(request, 'main/login.html', data)
            else:
                message = "Пароль введен не правильно"
                clientip = f'"Пароль введен не правильно"; {testUser.name}; {testUser.email}'
                d = {'clientip': clientip}
                MyLogger.logger.info('Password entering', extra = d)
    else:
        pass
    
    data = {
        'data': form,
        'message': message,
        'htmlTitle': htmlTitle,
        'visibility': visibility,
        'visibility1': visibility1,
    }
    return render(request, 'main/login.html', data)

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