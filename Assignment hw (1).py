#!/usr/bin/env python
# coding: utf-8

# In[5]:


queue=[]
queue.append(10)
queue


# In[6]:


queue.append(20)
queue.append(30)
queue.append(40)
queue.append(50)
queue.append(60)
queue


# In[14]:


queue.pop(0) 
queue


# In[15]:


queue.insert(0,11)
queue.insert(0,12)
queue.insert(0,13)
queue.insert(0,14)
queue.insert(0,15)
queue.insert(0,16)
queue.insert(0,17)
queue.insert(0,18)
queue.insert(0,19)
queue.insert(0,20)
queue


# In[16]:


queue.pop()


# In[4]:


for i in range(4):
    print("*",end=" ")


# In[5]:


for i in range(4):
    print("#",end=" ")


# In[7]:


for i in range(1):
    print("*",end=" ")


# In[10]:


for i in range(4,41,4):
    print(i,end=" ")


# In[11]:


for i in range(5,51,5):
    print(i,end=" ")


# In[16]:


for i in range(0,5):
    for j in range(0,i+1):
        print("*",end=" ")
    print()


# In[22]:


for i in range(0,6):
    for j in range(0,i+1):
        print(i,end=" ")
    print()


# In[25]:


for i in range(5,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print("\n")


# In[29]:


for i in range(5):
    print("*")
    print("#")


# In[31]:


for i in range(5):
    print("*",end=" ")
    print("#",end=" ")


# In[33]:


for i in range(1,5):
    for j in range(1,i+1):
         print("*",end=" ")
    print(i)
        


# In[34]:


for i in range(1,5):
    for j in range(1,i+1):
         print("",end=" ")
    print(i)
        


# In[37]:


for i in range(0,5):
    for j in range(0,7):
         print("#",end=" ")
    print()


# In[39]:


for i in range(6,0,-1):
    for j in range(6,0,-1):
         print(j,end=" ")
    print(i)


# In[41]:


for i in range(30,301,30):
    print(i)


# In[42]:


for i in range(50,501,50):
    print(i)


# In[44]:


for i in range(69,700,69):
    print(i)


# In[1]:


for i in range(5,51,5):
    print(i)


# In[4]:


# 1 2 3 vertically
n=3
for i in range(1,n+1):
    print(i)


# In[7]:


# 1 2 3 horizontally

for i in range(1,4):
    print(i,end="  ")


# In[8]:


for i in range(3,0,-1):
    print(i,end="  ")


# In[9]:


for i in range(1,4):
    print(i)


# In[11]:


for i in range(4):
    print("i")


# In[12]:


for i in range(4):
    print("i",end="  ")


# In[13]:


for i in range(4):
    print("*",end="  ")


# In[15]:


for i in range(5):
    print(" * ")


# In[17]:


for i in range(5):
    print("#")


# In[5]:


for i in range(5):
    if i % 2==0:
        
        print("#")
    else:
        print("*")
        


# In[6]:


for i in range(5):
    if i % 2==0:
        
        print("#",end=" ")
    else:
        print("*",end=" ")
        


# In[7]:


for i in range(0,10,+1):
    print(i)


# In[15]:


for i in range(0,10,+1):
    if  i %2 ==0:
        print(i)


# In[19]:


for i in range(0,10,+1):
    if  i %2!=0:
        print(i)


# In[26]:


for i in range(10):
    for j in range(10):
        if  i==j and j+i:
            print("#")
        else:
            print("*")


# In[34]:


for i in range(5):
    for j in range(5):
        if  i==j and j+2:
            print("#",end=" ")
        else:
            print("*",end=" ")


# In[2]:


# liner search in python 

def linearSearch(array,n,x):
    for i in range(0, n):
        if (array[i]==x):
            return i
        return -1

array = (2,4,0,4,9)
x=int(input("enter the element to be search:"))
n = len(array)
result = linearSearch(array,n,x)
if (result == -1):
    print("element not found")
else:
    print("element found at index: ",result)
    


# In[5]:


# liner search in python 

def linearSearch(array,n,x):
    for i in range(0, n):
        if (array[i]==x):
            return i
        return -1

array = (2,4,0,4,9)
x=int(input("enter the element to be search:"))
n = len(array)
result = linearSearch(array,n,x)
if (result == -1):
    print("element not found")
else:
    print("element found at index: ",result)
    


# In[1]:



for i in range(1,5):
    for j in range(1,i+1):
         print("@",end=" ")
    print(i)
        


# In[3]:


a=open(r"C:\Users\prasa\OneDrive\Desktop\file.json")
print(a.read())


# In[1]:


for i in range(5,51,5):
    print(i,end=" ")


# In[2]:


for i in range(5,51,5):
    print(i)


# In[ ]:




