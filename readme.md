![image](https://github.com/sukhbinder/JointPlotWithMatplotlib/blob/master/image/JointPlot_with_matplotlib.png)


Seaborn is an excellent plotting library but unfortunately it’s not always available as a standard installation. Recently had the requirement for an [Jointplot](http://seaborn.pydata.org/generated/seaborn.jointplot.html) but didn’t have access to seaborn, so wrote this simple jointplot implementation with matplotlib.



**usage**

~~~~
Import Jointplot
tips=pd.read_csv(r'tests/tips_p.csv')
data=np.c_[tips['total_bill'].values,tips['tip'].values]
jointPlot(data,kde=True)

~~~~




