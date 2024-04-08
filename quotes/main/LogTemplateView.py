from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from .models import TestUsers, TestProjects
from .MyLogger import MyLogger
from django.views.generic import TemplateView

class LogTemplateView(TemplateView):
    template_name = "main/login.html"
    
    def get(self, request, *args, **kwargs):
        MyLogger.configure()
        clientip = f'{request.get_full_path()}; {request.headers["User-Agent"]}; {request.method};'
        d = {'clientip': clientip}
        MyLogger.logger.info('Start work', extra = d)
        message = ""
        visibility = "block"
        visibility1 = "none"
        htmlTitle="Log-in"
        form = LoginForm()
        
        context = {
            'data': form,
            'message': message,
            'htmlTitle': htmlTitle,
            'visibility': visibility,
            'visibility1': visibility1,
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        message = ""
        visibility = "block"
        visibility1 = "none"
        htmlTitle="Log-in"
        form = LoginForm()
        
        context = {
            'data': form,
            'message': message,
            'htmlTitle': htmlTitle,
            'visibility': visibility,
            'visibility1': visibility1,
        }
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
                context = {
                    'data': testProjects,
                    'users': usersAll,
                    'message': message,
                    'htmlTitle': htmlTitle,
                    'visibility': visibility,
                    'visibility1': visibility1,
                }
                return render(request, self.template_name, context)
            else:
                message = "Пароль введен не правильно"
                clientip = f'"Пароль введен не правильно"; {testUser.name}; {testUser.email}'
                d = {'clientip': clientip}
                MyLogger.logger.info('Password entering', extra = d)
        return render(request, self.template_name, context)