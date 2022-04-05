"""
Copyright (c) 2022 - present Samed Buğra KARATAŞ
"""

import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from app.forms import LoginForm
from .models import *


@login_required(login_url="login")
def main_page(request):

    context = {
        "todos": todo.objects.filter(user_id=request.session['current_user_id']).order_by('-checked_date'),
        "current_username": user.objects.filter(id=request.session['current_user_id']).first().username
    }

    html_template = loader.get_template('app/main_page.html')
    return HttpResponse(html_template.render(context, request))


def add_todo(request, title):

    temp_todo = todo.objects.create(
        user_id=request.session['current_user_id'], checked=False, title=title)

    todo.save(temp_todo)

    return HttpResponseRedirect('main')


def checked_todo(request, todo_id):

    temp_todo = todo.objects.filter(id=todo_id).first()
    temp_todo.checked = True
    temp_todo.checked_date = datetime.now()
    todo.save(temp_todo)

    return HttpResponseRedirect('main')


def delete_todo(request, todo_id):

    temp_todo = todo.objects.filter(id=todo_id).first()

    todo.delete(temp_todo)

    return HttpResponseRedirect('main')


def edit_todo_page(request, todo_id):

    temp_todo = todo.objects.filter(id=todo_id).first()
    context = {
        "edit_id": temp_todo.id,
        "edit_title": temp_todo.title
    }

    html_template = loader.get_template('app/edit.html')
    return HttpResponse(html_template.render(context, request))


def edit_todo_save(request, todo_id, new_title):

    temp_todo = todo.objects.filter(id=todo_id).first()
    temp_todo.title = new_title
    temp_todo.checked = False
    temp_todo.checked_date = None
    temp_todo.updated_date = datetime.now()
    todo.save(temp_todo)

    return HttpResponseRedirect('main')


def sign_up_page(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_found = user_search(request.POST.get('username'))
            if(user_found == False):
                new_user = user()
                new_user.username = request.POST.get('username')
                new_user.password = request.POST.get('password')
                new_user.save()

                User.objects.create_user(
                    username=new_user.username, password=new_user.password)

                return HttpResponseRedirect('login')
            else:
                context = {"username": user.objects.filter(
                    id=user_found).first().username}
                return render(request, 'app/sign_up_page.html', context)

    else:
        form = LoginForm()

    context = {
        "form": form
    }

    html_template = loader.get_template('app/sign_up_page.html')
    return HttpResponse(html_template.render(context, request))


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            userx = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
            if userx is not None:
                login(request, userx)
                db_user = user.objects.filter(username=request.POST.get('username')).first()
                if db_user and db_user.password == request.POST.get('password'):
                    request.session['current_user_id'] = str(
                        user.objects.filter(id=db_user.id).first().id)
                    return HttpResponseRedirect('main')
            else:
                context = {"hata": "Yanlış Kullanıcı Adı veya Şifre Girdiniz."}
                return render(request, 'app/login_page.html', context)
    else:
        form = LoginForm()

    context = {
        "form": form,
    }

    html_template = loader.get_template('app/login_page.html')
    return HttpResponse(html_template.render(context, request))


def log_out(request):
    logout(request)
    return HttpResponseRedirect('login')


def user_search(username):
    db_user = user.objects.filter(username=username).first()
    if db_user:
        return db_user.id
    else:
        return False
