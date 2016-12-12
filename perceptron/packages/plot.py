import numpy as np
import matplotlib.pyplot as plt

def plot_decision_boundary(net):
    xmin, xmax = plt.xlim()
    ymin, ymax = plt.ylim()
    w = net.coef_[0]
    b = net.intercept_[0]
    if not w[1]==0:
        a = -w[0] / w[1]
        xx = np.linspace(xmin, xmax)
        yy = a * xx - b / w[1]
    elif not w[0]==0:
        a = -w[1] / w[0]
        yy = np.linspace(ymin, ymax)
        xx = a * yy - b / w[0]
    else:
        xx = []
        yy = []
    plt.plot(xx,yy, 'b-')
    plt.xlim([xmin,xmax])
    plt.ylim([ymin,ymax])
        
def plot_data(x,y):
    plt.rcParams['figure.figsize'] = (3.0, 3.0)
    colormap = np.array(['r', 'k'])
    plt.scatter(x[:,0], x[:,1], c=colormap[y.astype(int)], s=50);
    plt.axis([-1.2,1.2,-1.2,1.2]);