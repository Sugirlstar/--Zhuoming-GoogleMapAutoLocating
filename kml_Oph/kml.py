# -*- coding: UTF-8 -*-
import datetime
import pytz
import simplekml
import pandas as pd
import sys
import math
import numpy as np

file = sys.argv[1]
time = datetime.datetime.now(tz=pytz.timezone('Asia/Shanghai')).strftime("%Y-%m-%d-h%H")

pd.set_option("display.max_colwidth",1000)
data = pd.read_excel(file)
data = data.dropna()

descpt = data.iloc[:,1]
coordi = data.iloc[:,0]

kml = simplekml.Kml()

for i in data.index:

    descriptext = descpt[i].strip('【').split('\n')
    namei = [j for j in descriptext if '信息编号' in j]
    if str(namei).find('T') == -1:
        continue
    nameint = str(namei)[str(namei).find('T'):str(namei).find('T')+14] 
    prior = [j for j in descriptext if '优先等级' in j]
    if str(prior).count('级')==1:
        continue
    priorint = str(prior)[str(prior).find('】')+1]
    Typeo = 'B' if priorint == '3' else 'A'
    coords = tuple([float(i) for i in data['Coordinate'][i].split(',')])
    
    pnt = kml.newpoint()
    pnt.name = nameint
    pnt.coords = [coords]
    pnt.description = description=descpt[i]
    pnt.style.iconstyle.icon.href = 'images/icon-' + Typeo + priorint +'.png'
    
kml.savekmz(file[:-5] + '--' + time +'.kmz')

#if there are duplicated coordinates:
#Warning (from warnings module):
#  File "C:\Program Files\Python39\lib\zipfile.py", line 1505
#    return self._open_to_write(zinfo, force_zip64=force_zip64)
#UserWarning: Duplicate name: 'files/icon-A1.png'

