"""
Joint plot with matplotlib

Author: Sukhbinder Singh

inspired by
http://www.win-vector.com/blog/2015/06/wanted-a-perfect-scatterplot-with-marginals/
http://cxhernandez.com/tutorials/dataviz/2014/11/19/jointplot-d3.html

"""

from matplotlib import pyplot as plt
from matplotlib import gridspec
from scipy.stats import gaussian_kde

def jointPlot(data,kde=False,**kwargs):
    ymin, ymax=data[:,1].min(),data[:,1].max()
    xmin, xmax=data[:,0].min(),data[:,0].max()
    #Define grid for subplots
    gs = gridspec.GridSpec(2, 2, width_ratios=[3, 1], height_ratios = [1, 4])

    #Create scatter plot
    fig = plt.figure(facecolor='white')
    ax = plt.subplot(gs[1, 0],frameon = False)
    cax = ax.scatter(data[:,0], data[:,1], color='darkred', alpha=.6,)
    ax.grid(True)
    
    #Create Y-marginal (right)
    axr = plt.subplot(gs[1, 1], sharey=ax, frameon = False,xticks = [] ) #xlim=(0, 1), ylim = (ymin, ymax) xticks=[], yticks=[]
    axr.hist(data[:,1], color = '#5673E0', orientation = 'horizontal', normed = True)

    #Create X-marginal (top)
    axt = plt.subplot(gs[0,0], sharex=ax,frameon = False,yticks = [])# xticks = [], , ) #xlim = (xmin, xmax), ylim=(0, 1)
    axt.hist(data[:,0], color = '#5673E0', normed = True)

    
    
    try:
        ax.set_title(kwargs['title'])
        ax.set_xlabel(kwargs['xlabel'])
        ax.set_ylabel(kwargs['ylabel'])
    except:
        pass
    
    #Bring the marginals closer to the scatter plot
    fig.tight_layout(pad = 1)

    if kde:
        kdex=gaussian_kde(data[:,0])
        kdey=gaussian_kde(data[:,1])
        x= np.linspace(xmin,xmax,100)
        y= np.linspace(ymin,ymax,100)
        dx=kdex(x)
        dy=kdey(y)
        axr.plot(dy,y,color='black')
        axt.plot(x,dx,color='black')
        
        
        
    


if __name__=='__main__':
    import pandas as pd
    import numpy as np
    tips=pd.read_csv(r'tests/tips_p.csv')
    data=np.c_[tips['total_bill'].values,tips['tip'].values]
    kwargs = {"title": "Total-bill Vs tips","xlabel": "Total_bill","ylabel":"Tips"}
    jointPlot(data,kde=True,**kwargs)
    plt.show()
    
