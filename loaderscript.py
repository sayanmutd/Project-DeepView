#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 13:29:25 2018

@author: rishav
"""

import json 
import pandas as pd
import os 
from sklearn.metrics import accuracy_score
import pickle
#creating dummy row 
file = open('Violent/rgb_000350_keypoints.json','r')
datastore = json.load(file)
person1=datastore['people'][0]['pose_keypoints_2d']
person2=datastore['people'][1]['pose_keypoints_2d']
rperson1=[]
rperson2=[]
counter=1;
for dat in person1:
    if counter%3 !=0:
        rperson1.append(dat);
    counter=counter+1;
counter=1;
#print(len(rperson1))
for dat in person2:
    if counter%3 !=0:
        rperson2.append(dat);
    counter=counter+1;
datamerge=rperson1+rperson2
datamerge.append(1)
df=pd.DataFrame([datamerge])
df2=pd.DataFrame([datamerge])
df3=pd.DataFrame([datamerge])
df4=pd.DataFrame([datamerge])
#print(df)
## REPLACE ALL THESE MULTIPLE CALLS WITH A SINGLE FUNCTION WITH PASSED PARAMETERS AFASP
for file in os.listdir("Violent"):
    if file.endswith(".json"):
        dir=os.path.join("Violent/", file)
        file = open(dir,'r')
        datastore = json.load(file)
        person1=datastore['people'][0]['pose_keypoints_2d']
        person2=datastore['people'][1]['pose_keypoints_2d']
        rperson1=[]
        rperson2=[]
        counter=1;
        for dat in person1:
            if counter%3 !=0:
                rperson1.append(dat);
            counter=counter+1;
        counter=1;
        for dat in person2:
            if counter%3 !=0:
                rperson2.append(dat);
            counter=counter+1;

        datamerge=rperson1+rperson2
        datamerge.append(1)
        df.loc[len(df)]=datamerge
for file in os.listdir("NonViolent"):
    if file.endswith(".json"):
        dir=os.path.join("NonViolent/", file)
        file = open(dir,'r')
        datastore = json.load(file)
        try:
            person1=datastore['people'][0]['pose_keypoints_2d']
            person2=datastore['people'][1]['pose_keypoints_2d']
        except:
            print()
        rperson1=[]
        rperson2=[]
        counter=1;
        for dat in person1:
            if counter%3 !=0:
                rperson1.append(dat);
            counter=counter+1;
        counter=1;
        for dat in person2:
            if counter%3 !=0:
                rperson2.append(dat);
            counter=counter+1;

        datamerge=rperson1+rperson2
        datamerge.append(0)
        df.loc[len(df)]=datamerge
for file in os.listdir("NV2"):
    if file.endswith(".json"):
        dir=os.path.join("NV2/", file)
        file = open(dir,'r')
        datastore = json.load(file)
        try:
            person1=datastore['people'][0]['pose_keypoints_2d']
            person2=datastore['people'][1]['pose_keypoints_2d']
        except:
            print()
        rperson1=[]
        rperson2=[]
        counter=1;
        for dat in person1:
            if counter%3 !=0:
                rperson1.append(dat);
            counter=counter+1;
        counter=1;
        for dat in person2:
            if counter%3 !=0:
                rperson2.append(dat);
            counter=counter+1;

        datamerge=rperson1+rperson2
        datamerge.append(0)
        df.loc[len(df)]=datamerge
for file in os.listdir("NV3"):
    if file.endswith(".json"):
        dir=os.path.join("NV3/", file)
        file = open(dir,'r')
        datastore = json.load(file)
        try:
            person1=datastore['people'][0]['pose_keypoints_2d']
            person2=datastore['people'][1]['pose_keypoints_2d']
        except:
            print()
        rperson1=[]
        rperson2=[]
        counter=1;
        for dat in person1:
            if counter%3 !=0:
                rperson1.append(dat);
            counter=counter+1;
        counter=1;
        for dat in person2:
            if counter%3 !=0:
                rperson2.append(dat);
            counter=counter+1;

        datamerge=rperson1+rperson2
        datamerge.append(0)
        df.loc[len(df)]=datamerge
for file in os.listdir("NV4"):
    if file.endswith(".json"):
        dir=os.path.join("NV4/", file)
        file = open(dir,'r')
        datastore = json.load(file)
        try:
            person1=datastore['people'][0]['pose_keypoints_2d']
            person2=datastore['people'][1]['pose_keypoints_2d']
        except:
            print()
        rperson1=[]
        rperson2=[]
        counter=1;
        for dat in person1:
            if counter%3 !=0:
                rperson1.append(dat);
            counter=counter+1;
        counter=1;
        for dat in person2:
            if counter%3 !=0:
                rperson2.append(dat);
            counter=counter+1;

        datamerge=rperson1+rperson2
        datamerge.append(0)
        df.loc[len(df)]=datamerge
for file in os.listdir("NV5"):
    if file.endswith(".json"):
        dir=os.path.join("NV5/", file)
        file = open(dir,'r')
        datastore = json.load(file)
        try:
            person1=datastore['people'][0]['pose_keypoints_2d']
            person2=datastore['people'][1]['pose_keypoints_2d']
        except:
            print()
        rperson1=[]
        rperson2=[]
        counter=1;
        for dat in person1:
            if counter%3 !=0:
                rperson1.append(dat);
            counter=counter+1;
        counter=1;
        for dat in person2:
            if counter%3 !=0:
                rperson2.append(dat);
            counter=counter+1;

        datamerge=rperson1+rperson2
        datamerge.append(0)
        df.loc[len(df)]=datamerge
for file in os.listdir("NV6"):
    if file.endswith(".json"):
        dir=os.path.join("NV6/", file)
        file = open(dir,'r')
        datastore = json.load(file)
        try:
            person1=datastore['people'][0]['pose_keypoints_2d']
            person2=datastore['people'][1]['pose_keypoints_2d']
        except:
            print()
        rperson1=[]
        rperson2=[]
        counter=1;
        for dat in person1:
            if counter%3 !=0:
                rperson1.append(dat);
            counter=counter+1;
        counter=1;
        for dat in person2:
            if counter%3 !=0:
                rperson2.append(dat);
            counter=counter+1;

        datamerge=rperson1+rperson2
        datamerge.append(0)
        df.loc[len(df)]=datamerge
for file in os.listdir("V2"):
    if file.endswith(".json"):
        dir=os.path.join("V2/", file)
        file = open(dir,'r')
        datastore = json.load(file)
        try:
            person1=datastore['people'][0]['pose_keypoints_2d']
            person2=datastore['people'][1]['pose_keypoints_2d']
        except:
            print()
        rperson1=[]
        rperson2=[]
        counter=1;
        for dat in person1:
            if counter%3 !=0:
                rperson1.append(dat);
            counter=counter+1;
        counter=1;
        for dat in person2:
            if counter%3 !=0:
                rperson2.append(dat);
            counter=counter+1;

        datamerge=rperson1+rperson2
        datamerge.append(1)
        df.loc[len(df)]=datamerge
for file in os.listdir("V3"):
    if file.endswith(".json"):
        dir=os.path.join("V3/", file)
        file = open(dir,'r')
        datastore = json.load(file)
        try:
            person1=datastore['people'][0]['pose_keypoints_2d']
            person2=datastore['people'][1]['pose_keypoints_2d']
        except:
            print()
        rperson1=[]
        rperson2=[]
        counter=1;
        for dat in person1:
            if counter%3 !=0:
                rperson1.append(dat);
            counter=counter+1;
        counter=1;
        for dat in person2:
            if counter%3 !=0:
                rperson2.append(dat);
            counter=counter+1;

        datamerge=rperson1+rperson2
        datamerge.append(1)
        df.loc[len(df)]=datamerge
for file in os.listdir("V4"):
    if file.endswith(".json"):
        dir=os.path.join("V4/", file)
        file = open(dir,'r')
        datastore = json.load(file)
        try:
            person1=datastore['people'][0]['pose_keypoints_2d']
            person2=datastore['people'][1]['pose_keypoints_2d']
        except:
            print()
        rperson1=[]
        rperson2=[]
        counter=1;
        for dat in person1:
            if counter%3 !=0:
                rperson1.append(dat);
            counter=counter+1;
        counter=1;
        for dat in person2:
            if counter%3 !=0:
                rperson2.append(dat);
            counter=counter+1;

        datamerge=rperson1+rperson2
        datamerge.append(1)
        df.loc[len(df)]=datamerge
for file in os.listdir("V5"):
    if file.endswith(".json"):
        dir=os.path.join("V5/", file)
        file = open(dir,'r')
        datastore = json.load(file)
        try:
            person1=datastore['people'][0]['pose_keypoints_2d']
            person2=datastore['people'][1]['pose_keypoints_2d']
        except:
            print()
        rperson1=[]
        rperson2=[]
        counter=1;
        for dat in person1:
            if counter%3 !=0:
                rperson1.append(dat);
            counter=counter+1;
        counter=1;
        for dat in person2:
            if counter%3 !=0:
                rperson2.append(dat);
            counter=counter+1;

        datamerge=rperson1+rperson2
        datamerge.append(1)
        df.loc[len(df)]=datamerge
for file in os.listdir("V6"):
    if file.endswith(".json"):
        dir=os.path.join("V6/", file)
        file = open(dir,'r')
        datastore = json.load(file)
        try:
            person1=datastore['people'][0]['pose_keypoints_2d']
            person2=datastore['people'][1]['pose_keypoints_2d']
        except:
            print()
        rperson1=[]
        rperson2=[]
        counter=1;
        for dat in person1:
            if counter%3 !=0:
                rperson1.append(dat);
            counter=counter+1;
        counter=1;
        for dat in person2:
            if counter%3 !=0:
                rperson2.append(dat);
            counter=counter+1;

        datamerge=rperson1+rperson2
        datamerge.append(1)
        df.loc[len(df)]=datamerge
for file in os.listdir("V7"):
    if file.endswith(".json"):
        dir=os.path.join("V7/", file)
        file = open(dir,'r')
        datastore = json.load(file)
        try:
            person1=datastore['people'][0]['pose_keypoints_2d']
            person2=datastore['people'][1]['pose_keypoints_2d']
        except:
            print()
        rperson1=[]
        rperson2=[]
        counter=1;
        for dat in person1:
            if counter%3 !=0:
                rperson1.append(dat);
            counter=counter+1;
        counter=1;
        for dat in person2:
            if counter%3 !=0:
                rperson2.append(dat);
            counter=counter+1;

        datamerge=rperson1+rperson2
        datamerge.append(1)
        df2.loc[len(df2)]=datamerge
for file in os.listdir("NV7"):
    if file.endswith(".json"):
        dir=os.path.join("NV7/", file)
        file = open(dir,'r')
        datastore = json.load(file)
        try:
            person1=datastore['people'][0]['pose_keypoints_2d']
            person2=datastore['people'][1]['pose_keypoints_2d']
        except:
            print()
        rperson1=[]
        rperson2=[]
        counter=1;
        for dat in person1:
            if counter%3 !=0:
                rperson1.append(dat);
            counter=counter+1;
        counter=1;
        for dat in person2:
            if counter%3 !=0:
                rperson2.append(dat);
            counter=counter+1;

        datamerge=rperson1+rperson2
        datamerge.append(0)
        df3.loc[len(df3)]=datamerge
for file in os.listdir("TestO"):
    if file.endswith(".json"):
        dir=os.path.join("TestO/", file)
        file = open(dir,'r')
        datastore = json.load(file)
        try:
            person1=datastore['people'][0]['pose_keypoints_2d']
            person2=datastore['people'][1]['pose_keypoints_2d']
        except:
            print()
        rperson1=[]
        rperson2=[]
        counter=1;
        for dat in person1:
            if counter%3 !=0:
                rperson1.append(dat);
            counter=counter+1;
        counter=1;
        for dat in person2:
            if counter%3 !=0:
                rperson2.append(dat);
            counter=counter+1;

        datamerge=rperson1+rperson2
        datamerge.append(0)
        df4.loc[len(df4)]=datamerge
df=df.sort_values(by=[72])
df=df.reset_index(drop=True)
X = df.iloc[363:, 0:72].values
y = df.iloc[363:, 72].values
XTEST = df2.iloc[1:, 0:72].values
yTEST = df3.iloc[1:, 0:72].values
Custom= df4.iloc[1:,0:72].values

 # Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 42) 
# Feature Scaling
#from sklearn.preprocessing import MinMaxScaler
#sc = MinMaxScaler(feature_range=(0,1))
#X_train = sc.fit_transform(X_train)
#X_test = sc.transform(X_test)
#######Linear SVM Classification:

# Fitting SVM to the Training set
#from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
#classifier = SVC(kernel = 'linear', random_state = 0)
####RBF SVM Classification:
#classifier = SVC(kernel = 'sigmoid', random_state = 42)
###### POLYNOMIAL########
#classifier = SVC(kernel = 'poly', random_state = 0, degree = 3)
######SIGMOID ############################
classifier= GaussianNB()
classifier.fit(X_train, y_train)
filename="RBF.sav"
pickle.dump(classifier, open(filename, 'wb'))
# Visualising the Test set results
######SIGMOID ############################
# Visualising the Test set results
predicted_test=classifier.predict(X_test)
predicted_train=classifier.predict(X_train)
predicted_violent=classifier.predict(XTEST)
predicted_nonviolent=classifier.predict(yTEST)
predicted_Custom=classifier.predict(Custom)
#get the accuracy score
test_accuracy=accuracy_score(y_test,predicted_test)
train_accuracy=accuracy_score(y_train,predicted_train)
print(test_accuracy,train_accuracy)

