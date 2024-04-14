from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django import datetime

from sklearn.ensemble import GradientBoostingClassifier

from . forms import DoctorForm
from . models import *
from  django.contrib.auth import authenticate, login , logout
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

from sklearn.preprocessing import StandardScaler,minmax_scale,RobustScaler
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.svm import OneClassSVM
from sklearn.neural_network import MLPClassifier
from django.http import HttpRequest


def Home(request):
    return render(request,'carousel.html')

def admin_Home(request):
    dis = Seaech_Data.object.all()
    pat = Patient.objects . all()
    doc = Doctor.objects.all()
    feed = Feedback.objecets.all()

    d = {'dis':dis.count(),'pat':pat.count(),'doc':doc.count(),'feed':feed.count()}
    return render(request,'admin_home.html',d)


@login_required(login_url="login")
def assign_status(request,pid):
    doctor =doctor.object.get(id=pid)
    if Doctor.status == 1:
        doctor.status = 2
        messages.success(request, 'Selected doctor are successfully withdraw his approval')

    else:
        doctor.status=1
        messages.success(request,'Selected doctor are  successfully approved.')
        doctor
        return redirect('view_doctor')
    

    @login_required(login_url="login")
    def User_Home(request):
        return render(request,'patient_home.html')
    
    @login_required(login_url="login")
    def Doctor_Home(request):
        return render (request,'patient_home.html')
    
    def About(request):
        return render(request,'about.html')
    
    def Contact(request):
        return render(request,'contatct.html')
    
    def Gallery(request):
        return render(request,'Gallery.html')
    

    def Login_User(request):
        error=""
        if request.method == "POST":
            u= request.POST['uname']
            p=request.POST['pwd']
            user= authenticate(username=u,password=p)
            sign=""
            try:
                sign=Patient.objects.get(user=user)
            except:
                pass
            if sign:
                login(request,user)
                error="pat1"

            else:
                login(request,user)
                error="notmember"

        else:
          error="not"
    d = {'error': error}
    return render(request, 'login.html', d)

def Login_admin(request):
    error-""
    if request.method == "POST":
        u= request.POST['uname']
        p= request.POST['pwd']
        user =  authenticate (username=u, password=p)
        if user.is_staff:
            login(request,user)
            error="pat"

        else:
            error="not"
            d={'error':error}
            return render(request, 'admin_login.html',d)
        
    def Signup_User(request):
        error = ""
        if request.method == 'POST':
            f =  request.POST['fname']
            l =  request.POST['lname']
            u =  request.POST['uname']
            e =  request.POST['email']
            p = request.POST['pwd']
            d =  request.POST['dob']
            con = request.PSOT['contact']
            add = request.POST['add']
            type = request.POST['type']
            im = request.POST['image']
            dat = datetime.data.today()
            user = User.objects.create_user(email=e, username=u, password=p, first_name=f,last_name=l)
        if type == "Patient":
            Patient.objects.create(user=user,contact=con,address=add,image=im,dob=d)
        else:
            Doctor.objects.create(dob=d,image=im,user=user,contact=con,address=add,status=2)
        error = "create"
    d = {'error':error}
    return render(request,'register.html',d)





def home(req,):
    return render(req,"carousel.html")
