
# coding: utf-8

# In[1]:


from sympy import *

N = input('Let N = ')
q = input('Let q = ')

if int(N) > 0 and int(q) > -1:
    Q = (((factorial(int(q) + int(N) - 1)))/((factorial(int(q))*factorial(int(N)-1))))
    print("Multiplicity =",Q)
else:
    print("Please enter acceptable values for N and q")


# In[3]:


y = input('How many Fibonacci terms?')
x = [0,1]
i = len(x)
j = i -1
k = j -1
while True:
    k = x[j] + x[k]
    x.append(k) 
    j = len(x)-1
    k = len(x)-2
    if k > int(y):
        break
    print(x)

