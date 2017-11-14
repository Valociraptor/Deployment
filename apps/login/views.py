# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.messages import error
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import bcrypt
from models import *

def index(request):
    if not 'valid' in request.session:
        request.session['valid'] = 0

    return render(request, "login/index.html")


def success(request):
    
    if request.session['valid'] != 0:
        
        id = request.session['valid']
        context= {
            "user": User.objects.get(id=id)
        }
        return render(request, "login/success.html", context)
    
    return redirect('/login')

def login(request):
    
    result = User.objects.loginvalidate(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/login')

    request.session['valid'] = result.id

    
    return redirect('/login/success')
        
    
    

def register(request):
    
    errors = User.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
            return redirect("/login")


    name = request.POST['name']
    email = request.POST['email']
    password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    User.objects.create(name=name, email=email, password=password)

    user = User.objects.get(email=email)   
    id = user.id 
    request.session['valid'] = id
    
    
    return redirect('/login/success')
