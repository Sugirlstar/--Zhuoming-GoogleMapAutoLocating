# -*- coding: UTF-8 -*-
import datetime
import pytz
import simplekml
import pandas as pd
import sys
file = sys.argv[1]
time = datetime.datetime.now(tz=pytz.timezone('Asia/Shanghai')).strftime("%Y-%m-%d-h%H")
data = pd.read_excel(file, index_col=0)
kml = simplekml.Kml()
for i in data.index:
    pnt = kml.newpoint()
    pnt.name = i
    coords = tuple([float(i) for i in data['Coordinate'][i].strip('(').strip(')').split(',')])
    pnt.coords = [coords]
    pnt.description = description=data['Description'][i]
    pnt.style.iconstyle.icon.href = 'images/icon-' + data['Type'][i] + str(data['Priority'][i]) +'.png'
kml.savekmz(file[:-5] + '--' + time +'.kmz')