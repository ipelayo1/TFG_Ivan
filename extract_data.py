# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 10:26:53 2026

@author: ivanp
"""

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np


#data = xr.open_dataset('air.mon.1981-2010.ltm.nc') #para leer la media a largo plazo, 0.995 sigma (?)
data = xr.open_dataset('air.2m.mon.mean.nc') #para leer la media de cada mes a 2m de altura
#data = xr.open_dataset('air.2m.4Xday.ltm.1991-2020.nc') #para leer x4 day a 2m altura de media a largo plazo

#print(data)

temperatura = data['air']
#print(temperatura)
print(temperatura.time)
#print(temperatura.time.values) #muestra los valores de la lista level que se encuentra dentro del xarray temperatura

temperatura.isel(time=0).plot() #.isel() me permite seleccionar los elementos de temperatura por posición
                                         #si quisiera buscar 10 mbar de presion, por ejemplo, el codigo seria igual pero usando .sel()
plt.show()

np.shape(temperatura['time'])