# ----Importing libraries---
from django.shortcuts import render
from django.shortcuts import render
from matplotlib.style import context
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from requests import request
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras

# Create your views here.

def index(request):
    return render(request, 'index.html')  

def predict(request):
    return render(request, 'predict.html')

def Causes(request):
    return render(request, 'Causes.html') 

def churnRate(request):

    # val1 = int(request.GET["mstart"])
    # val2 = int(request.GET["mend"])
    # rate=((val1-val2)/val1)*100
    # context={
    #     'rate':rate +" "
    # }
    return render(request, 'churnRate.html')

def Measures(request):
    return render(request, 'Measures.html')

def result(request):
#-----------python code start here-------------

    #import dataset and store in df variable
    df=pd.read_csv(r'C:\Users\MWAURA P.K\Desktop\C_model\static\WA_Fn-UseC_-Telco-Customer-Churn.csv')
   

#drop columns
    df.drop(['customerID','Dependents','PhoneService','OnlineBackup','InternetService',
    'OnlineSecurity','DeviceProtection','StreamingTV','StreamingMovies','PaymentMethod']
    ,axis='columns',inplace=True)

#new dataframe (df1) with no nulls
    df1=df[df.TotalCharges!=' ']

#convert the notnull columns to integer datatype
    df1.TotalCharges=pd.to_numeric(df1.TotalCharges)

 #replace the 'no internet service ' and 'no phone service' with 'no'
    df1.replace('No phone service','No',inplace=True)
    df1.replace('No internet service','No', inplace=True)

#change the gender column to 0 & 1 as well
    df1['gender'].replace({'Female':0,'Male':1},inplace=True)
    df1['gender'].unique()

 # replace the columns with 'yes', 'no' values into 0 and 1
    yes_no_columns=['Partner','MultipleLines', 'TechSupport','PaperlessBilling','Churn']
    for col in yes_no_columns:
        df1[col].replace({'Yes':1,'No':0},inplace=True)

  #one hot encoding
    df2=pd.get_dummies(data=df1, columns=['Contract'])


#  Spliting test and traing data
 # set the neurons (input layer) & output columns (output layer)
    X=df2.drop('Churn',axis='columns')
    y=df2['Churn']

 #train test samples
    X_train, X_test,y_train, y_test =train_test_split(X,y,test_size=0.2,random_state=0)


  
#create neurons according to the number of columns and fit traing and test data
    model=keras.Sequential([
    keras.layers.Dense(12, input_shape=(12,), activation='relu'),
    keras.layers.Dense(7, activation='relu'), keras.layers.Dense(1, activation='sigmoid'), ])
       
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X_train,y_train)

    prediction=model.predict(X_test)

#array for fetching the inputs by user from the interface
    if request.method =='POST':
        data_list=[]
        data_list.append(int(request.POST.get("gender")))
        data_list.append(int(request.POST.get("seniorCitizen")))
        data_list.append(int(request.POST.get("partner")))
        data_list.append(int(request.POST.get("tenure")))
        data_list.append(int(request.POST.get("mlines")))
        data_list.append(int(request.POST.get("techSupport")))
        data_list.append(int(request.POST.get("pbill")))
        data_list.append(float(request.POST.get("mcharge")))
        data_list.append(float(request.POST.get("tcharges")))
        data_list.append(int(request.POST.get("m-m")))
        data_list.append(int(request.POST.get("oyr")))
        data_list.append(int(request.POST.get("tyrs")))
        result= model.predict([data_list])
        print(float(result))
    if result>=0.5:
        resulttext= 'leave'
    else:
        resulttext= 'stay'    
    context={
    'result':result,
    'text': resulttext
     
    }

#-----------python code end here----------------
    return render(request, 'result.html',context)


