
# coding: utf-8

# In[35]:


#Program is to calculate the Multiplicity of two interating Einstein solids, 1 and 2.
#qt is the total energy of both of the solids combined

#import numpy as np
import matplotlib.pyplot as plt
#for plotting the graph
from math import log, exp
#for log and exp funcitons

def factorial(N):
    if N == 0 or N == 1:
        return 1
    else:
        total = 1
        for i in range(2,N+1):
            total *= i
        return total
    
#Factorial function for Multiplicity calculations

N1 = 3000
N2 = 2000
qt = 100

#Values for number of osscilators for solids 1 and 2 and the total energy of the system
    
def M1(N1,q1):
    return exp((log(factorial(int(q1) + int(N1) - 1))) - ((log(factorial(int(q1)))) + (log(factorial(int(N1)-1)))))

def M2(N2,q1):
    return exp((log(factorial(int(qt-q1) + int(N2) - 1))) - ((log(factorial(int(qt-q1)))) + (log(factorial(int(N2)-1)))))

#Calcuations of M1 and M2. M2 is made dependant on q1 due to the fact that qt minus q1 is q2.
#Return function is used to input M values into Omega sets

def Plot_Multiplicity(N):

    N_series = range(N+1)
    #Omega1 = [] #Use if you wish to see the plot of M1
    #Omega2 = [] #Use if you wish to see the plot of M2
    Omega3 = []
    
    for q1 in N_series:
        #Omega1.append(M1(N1,q1)) #Use if you wish to see the plot of M1
        #Omega2.append(M2(N2,q1)) #Use if you wish to see the plot of M2
        Omega3.append(M1(N1,q1)*(M2(N1,q1)))
        
#By making both M1 and M2 dependant on q1, we can have q1 in the N_series work for both.
#Omega3.append(M1(N1,q1)*(M2(N1,q1))) is used to multiply the multiplicites together to get a total multiplicity
        
    #plt.plot(N_series, Omega1) #Use if you wish to see the plot of M1
    #plt.plot(N_series, Omega2) #Use if you wish to see the plot of M2
    plt.plot(N_series, Omega3)
    
    plt.xlabel('Total Energy (q_t) ')
    plt.ylabel('Multiplicity total (Omega 1 * Omega 2)')

    plt.show()
    
#As N increses the multiplicity will be more localized. In this function it is localized at (N+1)/2


# In[36]:


Plot_Multiplicity(qt)

