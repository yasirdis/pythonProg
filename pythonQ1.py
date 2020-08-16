#!/usr/bin/env python
# coding: utf-8

# In[27]:


import numpy as np
N=int(input("Enter Matrix size "))#matrix size N*N
arr = np.zeros(N*N).reshape(N,N)#generate 0 matrix conside it as empty matrix


# In[28]:


k=int(input("enter Number of jobs "))#enetr number of jobs


# In[29]:


i=0
j=0# i and j are i,j index of a given matrix
count=1 # conside 1 as x and 0 as empty
for x in range(0, k): # loop runs till all jobs will get done
    i=int(input("enter i"))#enter row
    j=int(input("enter j"))#enter col
    arr[i][j]=1 # populate i,j cell by 1 
    print("number of remaining empty Cells are",np.count_nonzero(arr==0))#print number of remianing empty cells
    print("indices of empty cells are: ",np.where(arr==0))#print indicies of empty cells.


# 

# In[ ]:




