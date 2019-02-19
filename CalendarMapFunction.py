import matplotlib.pylab as plt
import pandas as pd
import calmap
import numpy as np


    
def plot_calmap(df_serie, title='Calendar 2018'): 
    """
    Function that plots a Calendar Map
    
    Arguments:
        df_serie {Pandas series} -- Pandas series with the index in a day
         frequency: such as:
                2018-01-01     4959
                2018-01-02    55614
                2018-01-03    60449
                ...           ...
        
        title {string} -- Title of the figure
    """
    
    
    plt.style.use('seaborn')

    fig = plt.figure(figsize=(15,6))
    ax = fig.add_subplot(111)
    cax = calmap.yearplot(df_serie, ax=ax  )#, cmap='YlGn')
    cb=fig.colorbar(cax.get_children()[1], ax=cax, orientation='horizontal')
    
    plt.title(title)
    
    
    #increase all text
    ax=plt.gca()
    for item in ([ ax.xaxis.label, ax.yaxis.label] +
                 ax.get_xticklabels() + ax.get_yticklabels()  ):
        item.set_fontsize(16)
    
    cb.ax.tick_params(labelsize=14)     
    ax.title.set_fontsize(22)
       
    
    return fig



if __name__ == '__main__':

    # Create data 
    all_days = pd.date_range('1/1/2018', periods=365, freq='D')
    days = np.random.choice(all_days, 500)
    df_serie = pd.Series(np.random.randn(len(days)), index=days)

    # plot data
    fig=plot_calmap(df_serie)
    plt.show(fig)
