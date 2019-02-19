# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 17:52:28 2019

@author: marc.fuster
"""

import matplotlib.pylab as plt
import pandas as pd
import numpy as np
import matplotlib.dates
from datetime import datetime

""" Scatter Error """

from ScatterError import scatter_error_plot

y_true =    [0,1,2,3,4]
y_predict = [1,0,3,3,5]

dates = ['02/02/1991','02/03/1991','02/04/1991','02/08/1991','03/09/1991']
datelist = [datetime.strptime(d,'%m/%d/%Y').date() for d in dates]

    
fig1=scatter_error_plot(y_true, y_predict, datelist,
                   ' ','Units Sold','Error Analysis') 

""" Calendar Map """

from CalendarMapFunction import plot_calmap


all_days = pd.date_range('1/1/2018', periods=365, freq='D')
days = np.random.choice(all_days, 500)
df_serie = pd.Series(np.random.randn(len(days)), index=days)

fig2=plot_calmap(df_serie,'2018 data')

plt.show(fig1)


