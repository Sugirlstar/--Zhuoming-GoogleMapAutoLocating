# -*- coding: UTF-8 -*-
import datetime
import pytz
import simplekml
import pandas as pd
import sys
from pathlib import Path

file = sys.argv[1]
time = datetime.datetime.now(tz=pytz.timezone('Asia/Shanghai'))
time_str = time.replace(tzinfo=None).isoformat(timespec='hours')
data = pd.read_excel(file, index_col=0)
file_stem = Path(file).stem
kml = simplekml.Kml()

for i, coord_str in enumerate(data.Coordinate):
    pnt = kml.newpoint()
    pnt.name = i
    coord_str = coord_str.strip('()').split(',')
    coords = tuple([float(x) for x in coord_str])
    pnt.coords = [coords]
    pnt.description = data['Description'][i]
    pnt.style.iconstyle.icon.href = 'images/icon-{}{}.png'.format(data['Type'][i], data['Priority'][i])
output_name = '{}-{}.kmz'.format(file_stem, time_str)
kml.savekmz(output_name)