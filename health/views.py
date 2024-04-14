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



def home(req,):
    return render(req,"carousel.html")
