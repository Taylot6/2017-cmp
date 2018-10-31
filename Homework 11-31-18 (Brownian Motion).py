
# coding: utf-8

# In[6]:



get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np
import matplotlib.pyplot as plt

N = 100

L = 101
L1 = 101/2 

x = np.zeros(N)
y = np.zeros(N)

def Brownian(N):
    x = np.zeros(N)
    y = np.zeros(N)
    for i in range(1,N):
        x[0] = 50
        y[0] = 50
        r = np.random.random()

        if 0 <= r and r < 0.25 and x[i-1] < 101:
            x[i] = x[i-1] +1
            y[i] = y[i-1]
        elif 0.25 < r and r < 0.5 and x[i-1] > 0:
            x[i] = x[i-1] - 1
            y[i] = y[i-1]
        elif 0.5 < r and r < 0.75 and y[i-1] < 101:
            x[i] = x[i-1] 
            y[i] = y[i-1] + 1
        elif 0.75 < r and r < 1 and y[i-1] > 0:
            x[i] = x[i-1] 
            y[i] = y[i-1] - 1 
        else:
            x[i] = x[i-1] 
            y[i] = y[i-1]
    plt.figure(figsize = [18,12])
    plt.scatter(x,y,c=range(N))
    plt.colorbar()
    plt.show()


# In[8]:


Brownian(1000)


# In[12]:


get_ipython().run_line_magic('matplotlib', 'notebook')

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation 

L = 101
L1 = 101/2 

fig = plt.figure()
ax = plt.axes(xlim=(0, 101), ylim=(0,101))
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

x = np.zeros(N)
y = np.zeros(N)

def Brownian(N):
    #x = np.zeros(N)
    #y = np.zeros(N)
    for i in range(1,N):
        x[0] = 50
        y[0] = 50
        r = np.random.random()

        if 0 <= r and r < 0.25 and x[i-1] < 101:
            x[i] = x[i-1] +1
            y[i] = y[i-1]
        elif 0.25 < r and r < 0.5 and x[i-1] > 0:
            x[i] = x[i-1] - 1
            y[i] = y[i-1]
        elif 0.5 < r and r < 0.75 and y[i-1] < 101:
            x[i] = x[i-1] 
            y[i] = y[i-1] + 1
        elif 0.75 < r and r < 1 and y[i-1] > 0:
            x[i] = x[i-1] 
            y[i] = y[i-1] - 1 
        else:
            x[i] = x[i-1] 
            y[i] = y[i-1]*i
            
    #fig = fig = plt.figure()
    #scat = plt.scatter(x,y,c=range(N))
    #plt.figure(figsize = [18,12])
    #plt.colorbar()
    #plt.show()
    
    #ani = animation.FuncAnimation(fig,update_plot,interval=1000)
    
    #plt.show()
    
    #line.set_data(x, y)
    #return line,
    return x,y

def animate(i):
    Brownian(100)
    line.set_data(x, y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

