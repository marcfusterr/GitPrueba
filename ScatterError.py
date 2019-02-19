import matplotlib.pylab as plt
import numpy as np
import matplotlib.dates
from datetime import datetime

def scatter_error_plot(y_true, y_predict, datelist,
                       xlab='Dates', ylab='Units sold', title='Error analysis',
                       ticks_separation='weeks'):
    """Create scatter error plot to compare the Prediction.

    Args:
        y_true {[List of values]} -- Array of Real values
        y_predict {[List of values]} -- Array of Predicted Values.
        datelist: {[List of Datetime.date()]} --
                Array of Datetime.date() dates that correspond to the
                dates where y_true and y_predict are.
        xlab: {[String]} -- Title of xlabel
        ylab: {[String]} -- Title of ylabel
        title: {[String]} -- Title of figure
        ticks_separation {[String]} -- Select the range where of the 
            ticks separation. Options are the following:

            -'days'
            -'weeks'
            -'months'
            -'years'

    Returns:
        Matplotlib Figure

    """
    plt.style.use('seaborn')

    #create plot
    fig=plt.figure(figsize=(15,10))
    
    #plot things
    plt.plot(datelist,y_true, label=r'True Values' ,
             linestyle='--', linewidth=2)
    plt.plot(datelist,y_predict, label=r'Predicted Values',
             linestyle='--', linewidth=2)
    plt.scatter(datelist,y_true)
    plt.scatter(datelist,y_predict)
    
    #labels
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(title)
    
    #set ticks every week
    if ticks_separation == 'days':
        plt.gca().xaxis.set_major_locator(matplotlib.dates.DayLocator())
        
    elif ticks_separation == 'weeks':
        plt.gca().xaxis.set_major_locator(matplotlib.dates.WeekdayLocator())
        
    elif ticks_separation == 'months':
        plt.gca().xaxis.set_major_locator(matplotlib.dates.MonthLocator())
        
    elif ticks_separation == 'days':
        plt.gca().xaxis.set_major_locator(matplotlib.dates.YearLocator())

    
    #set week format
    plt.gca().xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%d %b'))
    
    
    plt.legend(loc='best')
    
    #increase all text
    ax=plt.gca()
    for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
                 ax.get_xticklabels() + ax.get_yticklabels() + ax.legend().get_texts()):
        item.set_fontsize(18)
    
    
    return fig




if __name__ == '__main__':
    
    # Create data
    y_true =    [0,1,2,3,4]
    y_predict = [1,0,3,3,5]

    dates = ['02/02/1991','02/03/1991','02/04/1991','02/08/1991','03/09/1991']
    datelist = [datetime.strptime(d,'%m/%d/%Y').date() for d in dates]

    # Plot
    fig = scatter_error_plot(y_true, y_predict, datelist,
                   '','Units Sold','Error Analysis')
    plt.show() # make f1 active again

    
