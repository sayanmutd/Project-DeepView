#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 13:39:33 2018

@author: rishav
"""

import json 
import pandas as pd
import os 
import pickle

def predict():
    file = open('TestR/result.json','r')
    datastore = json.load(file)
    person1=[]
    person2=[]
    for i in range(0,55):
        person1.append(i)
        person2.append(i)
    try:
        person1=datastore['people'][0]['pose_keypoints_2d']
        person2=datastore['people'][1]['pose_keypoints_2d']
    except:
        return 0.0
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
    df4=pd.DataFrame([datamerge])

    Custom= df4.iloc[:,0:72].values
    filename="GaussianNBmodel.sav"
    classifier = pickle.load(open(filename, 'rb'))
    predicted_Custom_saved=classifier.predict(Custom)
    os.remove('TestR/result.json')
    return(float(predicted_Custom_saved[0]))

print(predict())