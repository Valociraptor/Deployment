# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.messages import error
from django.shortcuts import render, redirect, HttpResponse
from models import *

# Create your views here.

def index(request):
    
    context ={
        'courses':Course.objects.all()
    }

    return render(request, "courses/index.html", context)


def create(request):
    errors = Course.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
            return redirect("/courses")

        
    name = request.POST['name']
    desc = request.POST['desc']
    Course.objects.create(name=name, desc=desc)
    print Course.objects.all()

    return redirect("/courses")

def delete(request, id):
    print id

    
    context = {
        "course" : Course.objects.get(id=id)
    }
    
    return render(request, "courses/delete.html", context)

def destroy(request, id):
    print id

    course = Course.objects.get(id=id)
    course.delete()
    
    return redirect("/courses")