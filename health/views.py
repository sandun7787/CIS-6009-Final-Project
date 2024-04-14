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


def logout(request):
    logout(request)
    return redirect('home')

@login_required(login_url="login")
def Change_Password(request):
    sign =0
    user = User.object.get(username=request.user.username)
    error = ""
    if not request.user.is_staff:
        try:
            sign = Patient.objects.get(user=user)
            if sign:
                error ="pat"

        except:
            sign =Doctor.obejct.get(user=user)
            terror=""
            if c == n:
                u =User.object.get(username__exact=request.user.username)
                u.set_password(n)
                u.save()
                terror = "yes"

            else:
                terror="note"
                d = {'error':error,'terror':terror,'data':sign}
                return render (request,'change_password.html',d)
            
def preprocess_input(df,scaler):
    csv_file = Admin_Helath_CSV.objects.get(id=1)
    df = pd.read_csv(csv_file.csv_file)
    X = df[['age','sex','cp',  'trestbps',  'chol',  'fbs',  'restecg',  'thalach',  'exang',  'oldpeak',  'slope',  'ca',  'thal']]
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=0)
    nn_model = GradientBoostingClassifier(n_estimators=100,learning_rate=1.0,max_depth=1, random_state=0)
    nn_model.fit(X_train, y_train)
    pred = nn_model.predict([list_data])
    print("Neural Network Accuracy: {:.2f}%".format(nn_model.score(X_test, y_test) * 100))
    print("Prdicted Value is : ", format(pred))
    dataframe = str(df.head())
    return (nn_model.score(X_test, y_test) * 100),(pred)



        





def home(req,):
    return render(req,"carousel.html")
