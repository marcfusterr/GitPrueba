import matplotlib.pylab as plt
import pandas as pd
import numpy as np
import matplotlib.dates
from datetime import datetime

plt.style.use('seaborn')

y_true =    [0,1,2,3,4]
y_predict = [1,0,3,3,5]

dates = ['02/02/1991','02/03/1991','02/04/1991','02/08/1991','03/09/1991']
datelist = [datetime.strptime(d,'%m/%d/%Y').date() for d in dates]


number_of_ticks=5


plt.figure(figsize=(15,10))
plt.plot(datelist,y_true, label=r'True Values' , linestyle='--', linewidth=2)
plt.plot(datelist,y_predict, label=r'Predicted Values', linestyle='--', linewidth=2)
plt.scatter(datelist,y_true)
plt.scatter(datelist,y_predict)

plt.xlabel('Days of January 2019')
plt.ylabel(r'Units sold that day')
plt.title('Error analysis')

#set ticks every week
plt.gca().xaxis.set_major_locator(matplotlib.dates.MonthLocator())


plt.gca().xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%d %b'))


plt.legend()

#increase all text
ax=plt.gca()
for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
             ax.get_xticklabels() + ax.get_yticklabels() + ax.legend().get_texts()):
    item.set_fontsize(18)

plt.show()