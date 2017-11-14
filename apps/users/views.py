# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.messages import error
from django.shortcuts import render, redirect, HttpResponse
from models import *

# Create your views here.

def index(request):
    
    context = {
        "users" : User.objects.all()
    }

    return render(request, "users/index.html", context)

def show(request, id):
    uid = int(id)
    
    context = {
        "users" : User.objects.get(id=uid)
    }

    
    
    
    return render(request, "users/show.html", context)


def new(request):
    
    return render(request, "users/new.html")


def edit(request, id):

    uid = int(id)
    
    context = {
        "users" : User.objects.get(id=uid)
    }
    
    return render(request, "users/edit.html", context)

def create(request):
    
    errors = User.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field) 

        return redirect('/users/new') 

    else:
        username = request.POST['name']
        useremail = request.POST['email']

        User.objects.create(name=username, email=useremail)
    
    return redirect("/users")


def destroy(request, id):
    print id

    user = User.objects.get(id=id)
    user.delete()
    
    return redirect("/users")

def update(request, id):
    
    errors = User.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field) 

        return redirect("/users/"+id+"/edit") 

    else:
        username = request.POST['name']
        useremail = request.POST['email']

        user = User.objects.get(id=id)
        user.name = username
        user.email = useremail
        user.save()
    
    return redirect("/users/"+id+"/edit")



