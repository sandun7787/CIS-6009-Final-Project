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

    d = {'dis':dis.count(),'pat':pat.count(),'doc':doc.count(), 'feed':feed.count()}
    return render(request,'admin_home.html'd)

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




def home(req,):
    return render(req,"carousel.html")
