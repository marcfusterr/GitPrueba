"""
Esta prueba no ha valido la pena

no usar esto

"""




import matplotlib.pylab as plt
import pandas as pd
import numpy as np
import matplotlib.dates
import datetime

plt.style.use('seaborn')

y_true =    [0,1,2,3,4]
y_predict = [1,0,3,3,5]
datelist = pd.date_range(pd.datetime.today(), periods=5).tolist()

df=pd.DataFrame(
        {'y_true': y_true,
        'y_predict': y_predict,
        'ds' : datelist        
         })
#df.set_index('ds', inplace=True)


number_of_ticks=5

days=np.arange(1,len(y_true)+1,1)

plt.figure()
df.plot()
#df.plot(x='Index', y='y', style=".")

df.plot(style=".")
df.plot(style=".")

plt.xlabel('Days of January 2019')
plt.ylabel(r'Units sold that day')
plt.title('Error analysis')

plt.xticks(np.linspace(min(datelist), max(datelist)+1, number_of_ticks))
#set ticks every week
plt.gca().xaxis.set_major_locator(matplotlib.dates.DayLocator())


plt.gca().xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%d %b'))


plt.legend()

#increase all text
ax=plt.gca()
for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
             ax.get_xticklabels() + ax.get_yticklabels() + ax.legend().get_texts()):
    item.set_fontsize(18)

plt.show()