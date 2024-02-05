#!/usr/bin/env python
# coding: utf-8

# # DAY 02 OF 75 DAYS CHALLENGE 

# In[1]:


a = { "sumit ","amit"}
print(a)
print(type(a))


# In[4]:


#a = { "sumit ","amit"}                   #unordered
#print(a[0])


# In[20]:


a = { "sumit ","amit","sumit","aman","aman"}
print(a)
print(len(a))
print(type(a))


# # access item in set

# In[9]:


a = {2,4,5,6,6,6,4,4,5}
for x in a :
    print(x)


# In[10]:


a = {2,4,5,6,6,6,4,4,5}
print ( 2 in a)


# In[12]:


a = {2,4,5,6,6,6,4,4,5}
print( 9 in a)


# In[13]:


a = {2,4,5,6,6,6,4,4,5}
a.add(100)
print(a)


# In[14]:


a = {2,4,5,6,6,6,4,4,5}
a.remove(4)
print(a)


# In[15]:


a = {2,4,5,6,6,6,4,4,5}
a.clear()
print(a)


# In[17]:


a = {2,4,5,6,6,6,4,4,5}
b = {7,8,9,3,2,5,6}
z = a.union(b)
print(z)


# In[ ]:


a = {2,4,5,6,6,6,4,4,5}
print


# In[21]:


a = {2,4,5,6,6,6,4,4,5}
b = {7,8,9,3,2,5,6}
z = a.intersection(b)
print(z)


# In[22]:


a = {2,4,5,6,6,6,4,4,5}
print(len(a))
print(min(a))
print(max(a))


# # numpy library 

# In[5]:


import numpy as np


# In[27]:


arr =np.array([2,3,4,54,5,5,5,5,56,6,6])
print(type(arr))


# #  1 d dimensions in array 

# In[28]:


arr = np.array([2,2,3,34,4,5,5,5,5,50,4,])
print(arr)
print(arr.ndim)


# In[7]:


arr = np.array((4,5,6,7))
print(arr)
print(type(arr))
print(arr.ndim)


# # 2 D dim array 

# In[11]:


arr = np.array([[ 2,3,4,5,],[9,99,999,9999]])
print(arr.ndim)
print(arr)


# #  3D  DIMENSION ARRAY 

# In[12]:


s= np.array([[[2,3,4],[6,7,8],[5,6,7]]])
print(s)
print(s.ndim)


# In[15]:


arr = np.array([2,3,4,5,5], ndmin= 7)
print(arr)
print(arr.ndim)


# # NUMPY ARRAY INDEXING

# In[16]:


arr = np.array((4,5,6,7))
print(arr[1])


# In[17]:


arr = np.array((4,5,6,7))
print(arr[1:3])


# In[18]:


arr = np.array([[ 2,3,4,5,],[9,99,999,9999]])
print(arr[0:1])


# In[26]:


arr = np.array([[2,3,4,5,],[9,99,999,9999]])
print(arr[0:0])


# # slicing of numpy 

# In[27]:


arr = np.array((4,5,6,7))
print(arr[1 :3])


# In[31]:


arr = np.array([[ 2,3,4,5,],[9,99,999,9999]])
print(arr[1,1:3])


# In[32]:


arr = np.array([[ 2,3,4,5,],[9,99,999,9999]])
print(arr[0,1:3])


# In[39]:


s= np.array([[[2,3,4],[6,7,8],[5,6,7]]])
print(s[0,1:2])


# # checking datatype of array

# In[40]:


s= np.array([[[2,3,4],[6,7,8],[5,6,7]]])
print(s.dtype)


# In[44]:


arr = np.array([4,5,6,7],dtype = 'S')
print(arr.dtype)


# In[47]:


arr = np.array([4,5,6,7],dtype = 'i4')
print(arr.dtype)


# # numpy array shape 

# In[48]:


s = np.array([[2,3,4],[7,8,9]])
print(s.shape)


# In[49]:


s = np.array([[[2,3,4],[7,8,9],[4,5,6]]])
print(s.shape)


# # joining numpy array 

# In[55]:


a =np.array([2,3,4,5])
b =np.array([2,3,4,5])
s =np.concatenate((a ,b))
print(s)


# In[62]:


arr1 =np.array([[2,3,4,5],[33,5,6]])
arr2 =np.array([[2,3,4,5],[2,3,5,6]])
s =np.concatenate((arr1,arr2), axis = 1)
print(s)


# # spliting numpy array 

# In[64]:


a =np.array([2,3,4,5])
s = np.array_split(a,3)
print(s)


# # ravel & flatten

# In[68]:


s= np.array([[[2,3,4],[6,7,8],[5,6,7]]])
print(s.ndim)
n =s.ravel()
print(n)
print(n.ndim)


# In[69]:


s= np.array([[[2,3,4],[6,7,8],[5,6,7]]])
print(s.ndim)
n =s.flatten()
print(n)
print(n.ndim)


# In[70]:


s = np.array([2,4,54,56,6,7,7,7,8,5,4,4,3,3,3,])
p = np.unique(s)
print(p)


# In[73]:


s = np.array([2,4,54,56,6,7,7,7,8,5,4,4,3,3,3,])
p = np.unique(s, return_counts = True)
print(p)


# # DELATE 

# In[77]:


a =np.array([2,3,4,5])
d = np.delete(a,[1])
print(d)


# In[ ]:





# In[ ]:




