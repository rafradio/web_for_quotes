from django.shortcuts import render, redirect
import asyncio
from django.http import HttpResponse
from .forms import LoginForm
from .models import TestUsers, TestProjects
from .MyLogger import MyLogger
from django.views.generic import TemplateView
from asgiref.sync import sync_to_async

class LogTemplateView(TemplateView):
    template_name = "main/login.html"
    
    def get(self, request, *args, **kwargs):
        # request.session['fav_color'] = 'red'
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
                # fav_color = request.session.get('fav_color')
                # print(fav_color)
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
                response = render(request, self.template_name, context)
                response.delete_cookie('quotes_user', testUser.email)
                response.headers['Rafael'] = 'no-cache'
                return response
                # request.META['HTTP_Rafael'] = 'bar'
                # return render(request, self.template_name, context)
            else:
                message = "Пароль введен не правильно"
                clientip = f'"Пароль введен не правильно"; {testUser.name}; {testUser.email}'
                d = {'clientip': clientip}
                MyLogger.logger.info('Password entering', extra = d)
                context['message'] = message
                return render(request, self.template_name, context)
    