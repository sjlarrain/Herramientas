#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import sklearn as sk
import bs4
import sqlite3
import os
from IPython.display import display
pd.set_option('max_columns',1000)
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


path=r'./EOD'


# # Mision 1

# In[3]:


tablas=dict()
for e in os.listdir(path):
    if str(e)[-4:] in ".csv" :
        print(e)
        df=pd.read_csv(path+"/"+e, error_bad_lines=False,sep=";",decimal=",",encoding='iso-8859-1', engine='python')
        display(df.head(5))
        tablas.update({e:df})


# # Mision 2

# In[4]:


print(tablas.keys())


# In[5]:


path_M2=path+"/Tablas_parametros/PropositoAgregado.csv"
df1=pd.read_csv(path_M2,sep=";")
x=df1['PropositoEstraus'].tolist()
y=df1['Id'].tolist()
y=map(lambda w: float(w),y)
conversion=dict(zip(y,x))
conversion.update({'NR':None})
df=tablas['viajes.csv']
df['PropositoAgregado'].fillna('NR', inplace=True)
df['PropositoAgregado']=df['PropositoAgregado'].apply(lambda x: conversion[x])
cuenta=df["PropositoAgregado"].value_counts().to_dict()
total=sum(cuenta.values())
for e in cuenta.keys():
    print(e, '{}%'.format(cuenta[e]/total*100))


# # Mision 3

# In[6]:


df=tablas['Hogares.csv']
df.boxplot(column='IngresoHogar', by=['Comuna'])
mpl.pyplot.show()
x=0
v=df.groupby('Comuna')['IngresoHogar'].var().to_dict()
for e in v.keys():
    if v[e]>x:
        x=v[e]
        y=e
y,x


# # Mision 4

# In[7]:


def con_org(org):
    df_comunas=pd.read_csv(path+'/Tablas_parametros/Comunas.csv',sep=",")
    conversion=dict(zip(map(lambda x: x.upper(),df_comunas['Comuna'].tolist()),df_comunas['Id'].tolist()))
    df=tablas['viajes.csv']
    col=df.columns.to_list()
    com_org=conversion[org.upper()]
    datos1=df.loc[df['ComunaOrigen']==com_org]
    df1=pd.DataFrame(datos1,columns=col)
    return df1

def con_destino(des):
    df_comunas=pd.read_csv(path+'/Tablas_parametros/Comunas.csv',sep=",")
    conversion=dict(zip(map(lambda x: x.upper(),df_comunas['Comuna'].tolist()),df_comunas['Id'].tolist()))
    df=tablas['viajes.csv']
    col=df.columns.to_list()
    com_des=conversion[des.upper()]    
    datos2=df.loc[df['ComunaDestino']==com_des]
    df2=pd.DataFrame(datos2,columns=col)
    return df2

display(con_org('Las Condes').head(5))
display(con_destino('Isla de Maipo').head(5))


# # Mision 5

# In[8]:


df=tablas['viajes.csv']
col=df.columns.tolist()
df['OrigenCoordX']=pd.to_numeric(df['OrigenCoordX'],errors='coerce')
df['OrigenCoordY']=pd.to_numeric(df['OrigenCoordY'],errors='coerce')
df['DestinoCoordX']=pd.to_numeric(df['DestinoCoordX'],errors='coerce')
df['DestinoCoordY']=pd.to_numeric(df['DestinoCoordY'],errors='coerce')
datos1=df.loc[(df['OrigenCoordX'].notnull())&(df['OrigenCoordY'].notnull())&(df['DestinoCoordX'].notnull())&(df['DestinoCoordY'].notnull())]
df1=pd.DataFrame(datos1,columns=col)
df1['Distancia']=df1.apply(lambda x: (((x['DestinoCoordX']-x['OrigenCoordX'])**2+(x['DestinoCoordY']-x['OrigenCoordY'])**2)**0.5) ,axis=1)
tablas.update({"Distancia_M5":df1})
display(df1.head(10))


# In[9]:


df=tablas['personas.csv']
col=df.columns.tolist()
display(df.head(5))
datos1=df.loc[(df['Sexo']==1)&(df['LicenciaConducir']!= '1')]
df1=pd.DataFrame(datos1,columns=col)
display(df1.head(5))


# In[10]:


df=tablas['Edadpersonas.csv']
df_=pd.merge(df1,df, on='Persona')


# In[11]:


display(df_.head(5))


# In[12]:


datos=df_.loc[(df_['Edad']>30)&(df_['Edad']<50)]
df_1=pd.DataFrame(datos,columns=['Persona','Sexo','Edad','LicenciaConducir'])
display(df_1.head(5))


# In[14]:


df=tablas['Distancia_M5']
path_M7=path+"/Tablas_parametros/Proposito.csv"
df1=pd.read_csv(path_M7,sep=";")
proposito=df1['Proposito'].tolist()
ids=df1['Id'].tolist()
ids=map(lambda x: float(x),ids)
conversion=dict(zip(ids,proposito))
#df['Proposito']=df['Proposito'].apply(lambda x: conversion[x])
path_M7=path+"/Tablas_parametros/Sector.csv"
df1=pd.read_csv(path_M7,sep=";")
nom=df1['Nombre'].tolist()
sec=df1['Sector'].tolist()
sec=map(lambda x: float(x),sec)
conversion=dict(zip(sec,nom))
conversion.update({0.0:None})
#df['SectorOrigen']=df['SectorOrigen'].apply(lambda x: conversion[x])
fig, (ax1,ax2,ax3)=plt.subplots(1,3)
df.groupby(['Proposito'])['Distancia'].mean().plot(kind="bar",ax=ax1)
df.groupby(['SectorOrigen'])["Distancia"].mean().plot(kind="bar",ax=ax2)
df.groupby(['Etapas'])["Distancia"].mean().plot(kind="bar",ax=ax3)


# # Mision 8
# 
# Para la mision se estimo el tiempo de viaje. Para calcular esto construimos un dataframe ocupando las siguentes varaibles:
#     1. Edad del individuo
#     2. Hora de inicio del viaje
#     3. Factor laboral normal
#     4. Ingreso del Hogar
#     5. Monto de arriendo
#     6. Sexo del individuo

# In[94]:


def hours(x):
    if not isinstance(x, float):
        x=x.strftime("%H:%M:%S")
        x=pd.to_numeric(x)
        return x
predictor=tablas["Edadpersonas.csv"]
df_hogares=tablas["Hogares.csv"][['Hogar','MontoArr','IngresoHogar']]
df_viajes=tablas["Distancia_M5"][['Hogar', 'Persona','HoraIni','FactorLaboralNormal','TiempoViaje','Distancia']]
df_persona=tablas['personas.csv'][['Persona','Sexo']]
predictor=pd.merge(predictor,df_viajes,left_on="Persona",right_on='Persona')
predictor=pd.merge(predictor,df_hogares,left_on='Hogar',right_on='Hogar')
predictor=pd.merge(predictor,df_persona,left_on='Persona',right_on='Persona')
predictor['Sexo']=predictor['Sexo'].apply(lambda x: 0 if x==2 else 1)
#predictor['HoraIni'] = predictor['HoraIni'].replace(to_replace='None', value=np.nan).dropna()
predictor=predictor.dropna()
#predictor['HoraIni']=predictor['HoraIni'].fillna("00:00", inplace=True)
#predictor['HoraIni']=predictor['HoraIni'].apply(hours(x))
predictor['FactorLaboralNormal'].fillna(predictor['FactorLaboralNormal'].mean(),inplace=True)
predictor=predictor[['MontoArr','IngresoHogar','FactorLaboralNormal','TiempoViaje','Sexo','Edad','Distancia']]
display(predictor.head())


# Ocupando el modelo definido en la clase 5.1 del curso entrenamos el sistema de prediccion

# In[107]:


from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn import svm
from sklearn import metrics
import numpy as np

def classification_model(model, data, predictors, outcome):
    model.fit(data[predictors],data[outcome])
    predictions = model.predict(data[predictors])
    #parameters = model.coef_
    score= metrics.r2_score(data[outcome],predictions)
    #for i in range(len(parameters)):
     #   print(predictors[i],":",parameters[i])
    print(np.mean(predictions))
    print(score)

outcome_var = 'TiempoViaje'
model = DecisionTreeClassifier()
predictor_var = ['MontoArr','IngresoHogar','FactorLaboralNormal','Sexo','Edad','Distancia']
classification_model(model,predictor,predictor_var,outcome_var)


# # Parte dos

# In[ ]:





# In[ ]:




