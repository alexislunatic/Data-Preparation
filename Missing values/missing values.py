#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 00:41:28 2018

@author: aalvarez
"""
##Librerias
import pandas as pd 
import numpy as np 

#Leer el dataset
dataset = pd.read_csv('prestamos.csv')

#Ver valores nulos
print('Valores nulos:\n', dataset.isnull().sum())


#1.Eliminar valores nulos
dataset = dataset.loc[dataset['Sexo'].isnull() == False]
dataset = dataset.loc[dataset['CantidadPrestamo'].isnull() == False]
dataset = dataset.loc[dataset['Plazo'].isnull() == False]
dataset = dataset.loc[dataset['Casado'].isnull() == False]

#2.Inputar valores nulos
dataset['Sexo'].fillna(dataset['Sexo'].mode()[0],inplace=True)
dataset['CantidadPrestamo'].fillna(dataset['CantidadPrestamo'].mean(),inplace=True)
dataset['Plazo'].fillna(dataset['Plazo'].mean(),inplace=True)
dataset['Casado'].fillna(dataset['Casado'].mode()[0],inplace=True)




