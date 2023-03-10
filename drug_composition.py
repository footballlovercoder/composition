# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 21:16:14 2023

@author: ritup
"""
import altair as alt
from datetime import date
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import regex as re
import requests
import math
from dateutil.relativedelta import relativedelta
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys
from st_keyup import st_keyup
url3='https://raw.githubusercontent.com/footballlovercoder/wellocity_consumption/main/drug_info1.csv'
url4='https://raw.githubusercontent.com/footballlovercoder/wellocity_consumption/main/drug_info2.csv'
def clean_data(x):
    if x[-1]==',':
        return x[:-1]
    
@st.experimental_memo
def load_data():
        df1 = pd.read_csv(url3,sep = ',',header=0)
        df1=df1.drop(['Unnamed: 0'],axis=1)
        df2=pd.read_csv(url4,sep = ',',header=0)
        df2=df2.drop(['Unnamed: 0'],axis=1)
        return df1,df2
df1,df2= load_data()
df=pd.concat([df1,df2])
df=df.fillna(' ')
df['Salt']=df['Salt'].apply(lambda x:clean_data(x))
df['Uses']=df['Uses'].apply(lambda x:clean_data(x))
df['Alternate Medicines']=df['Alternate Medicines'].apply(lambda x:clean_data(x))
df=df.rename(columns={"Medicine Name":"Item_Name"})
data=df.copy()
debounce = st.checkbox("Add 0.5s debounce?")
name = st_keyup("Enter medicine name", debounce=500 if debounce else None)
if name:
    filtered=data[data.Item_Name.str.lower().str.contains(name.lower(), na=False)]
else:
    filtered=data
st.write(len(filtered), "medicines found")
st.write(filtered)
#data_filtered=data[data['Item_Name']==choice]

