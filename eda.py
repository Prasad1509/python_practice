#!/usr/bin/env python
# coding: utf-8

# In[29]:


from matplotlib import pyplot as plt
x=[4,8,9]
y=[10,12,15]
plt.plot(x,y)
#plt.tittle("line grap")


# In[13]:


import pandas as pd
print(pd.__version__)


# In[16]:


import seaborn as sns
print(sns.__version__)


# In[30]:


from matplotlib import pyplot as plt
x=[4,8,9]
y=[10,12,15]
plt.plot(x,y)
#plt.tittle("line grap")


# In[18]:


import matplotlib
matplotlib.__version__


# In[26]:


import matplotlib
x=[4,8,9]
y=[10,12,15]
plt.plot(x,y)
plt.title("line grap")
plt.ylabel("y axis")
plt.xlabel("x axis")
plt.ylim(9,20)
plt.xlim(0,10)


# In[27]:


import matplotlib.pyplot as plt
import numpy as np

x=np.array([5,9,6,7,4,8,2,3])
y=np.array([23,56,45,47,50,24,44,33])
plt.scatter(x,y)
plt.show


# In[67]:


import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
x=[5,8,10]
y=[12,16,6]
x2=[6,9,11]
y2=[7,15,7]
plt.bar(x,y,color="g",align="center")
plt.bar(x2,y2,color="m",align="center")
plt.title("Information")
plt.xlabel("x axis")
plt.ylabel("y axis")


# In[97]:


import matplotlib.pyplot as plt
players=("rohit","virat","shikhar","yuvraj")
runs=(45,30,15,10)
explode=(0.1,0,0,0)
colors=("m","g","b","y")
fig1,ax1=plt.subplots()
ax1.pie(runs,explode=explode,labels=players,colors=colors,autopct='%1.1f%%',
        shadow=True,startangle=90)
plt.legend()
plt.title("pie chart")
plt.show()


# In[27]:


import matplotlib.pyplot as plt

x=[23,33,44,55,66,77,88]
y=[23,76,89,21,32,34,48]
plt.plot(x,y)
plt.title("line graoh")
plt.xlabel("x axis")

plt.ylabel("y axis")
plt.xlim(0,90)
plt.ylim(0,90)


# In[2]:


import matplotlib.pyplot as plt
x=[4,8,9]
y=[10,12,15]
plt.plot(x,y)
plt.title("line grap")
plt.ylabel("y axis")
plt.xlabel("x axis")
plt.ylim(9,20)
plt.xlim(0,10)


# In[21]:


import pandas as pd
df=pd.DataFrame({"name":["prasad","arati","kirti","kavya","arnav","pari"],
                "Age Group":["middle","young","old","middle","young","old"],
                "sex":["m","f","f","f","m","f"],
                "sal":[20000,40000,20000,40000,50000,20000]})
df


# In[22]:


a=pd.crosstab(index=df['Age Group'],columns=df['sex'])
a


# In[29]:


print(df)
var=df.groupby(['sal'])
var


# In[1]:


import pandas as pd
df=pd.DataFrame({"name":["prasad","arati","kavya","kavya","arnav","kavya"],
                "Age Group":["middle","young","old","middle","young","old"],
                "sex":["m","f","f","f","m","f"],
                "sal":[20000,40000,20000,40000,50000,20000]})
df
var=df.groupby('sal')
var


# In[40]:


import pandas as pd
df=pd.DataFrame({"name":["prasad","arati","kavya","kavya","arnav","kavya","kavya","kavya","kavya"],
                "marks":[7,5,12,9,8,21,14,16,25]})
df
a=df['marks']
b=a.mean()
print(b)


# In[41]:


c=a.median()
print(c)


# In[1]:


from scipy import stats
marks=[2,3,4,4,5,6,7,8,9]
stats.mode(marks)


# In[53]:


df=pd.DataFrame({"name":["prasad","arati","kavya","kavya","arnav","kavya"],
                "marks":[98,90,97,97,95,97]})
df


# In[54]:


var=df.groupby('marks')
var


# In[3]:


import pandas as pd

data = {
  'co2': [95, 90, 99, 104, 105, 94, 99, 104],
  'model': ['Citigo', 'Fabia', 'Fiesta', 'Rapid', 'Focus', 'Mondeo', 'Octavia', 'B-Max'],
  'car': ['Skoda', 'Skoda', 'Ford', 'Skoda', 'Ford', 'Ford', 'Skoda', 'Ford']
}

df = pd.DataFrame(data)

df


# In[12]:


var=df.drop("car",axis=1)
var


# In[22]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = {
  'co2': [95, 90, 99, 104, 105, 94, 99, 104],
'marks': [23,45,67,89,90,45,67,89],
'age':[12,23,34,45,56,67,78,89]}
df = pd.DataFrame(data)

df


# In[36]:


df1=df.corr()
df1


# In[36]:


s1=sns.heatmap(df1,annot=True,fmt='g')
plt.show()


# In[3]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = {'name':['a','b','c','d','e','f','g','h'],
  'maths': [95, 90, 99, 104, 105, 94, 99, 104],
'bio': [23,45,67,89,90,45,67,89],
'age':[12,23,34,45,56,67,78,89]}
df = pd.DataFrame(data)

print(df)
df1=df.corr()
print(df1)

sns.heatmap(df1,annot=True,cmap='RdBu')
plt.show()


# In[2]:


import pandas as pd
df=pd.DataFrame({"name":["prasad","arati","kavya","kavya","arnav","kavya","pari"],
                "marks":[9,12,15,18,21,24,27]})
df


# In[11]:


print(df['marks'].var())


# In[12]:


df=pd.DataFrame({"name":["prasad","arati","kavya","kavya","arnav","kavya"],
                "marks":[1,3,5,7,9,11]})
df


# In[13]:


print(df['marks'].var())


# In[3]:


import pandas as pd
df=pd.DataFrame({"name":["prasad","arati","kirti","kavya","arnav","pari"],
                "Age Group":["middle","young","old","middle","young","old"],
                "sex":["m","f","f","f","m","f"],
                "sal":[20000,40000,20000,40000,50000,20000]})
df


# In[5]:


df["sex"]=df["sex"].replace({"m":1,"f":0})
df


# In[27]:


import numpy as np
a=np.array([9,12,15,18,21,24,27])
np.var(a)


# In[28]:


np.ptp(a)


# In[2]:


p=open(r"C:\Users\prasa\OneDrive\Desktop\file.json")
print(p.read())


# In[ ]:





# In[2]:


#p=open(r"C:\Users\prasa\OneDrive\Desktop\file.json","a")
#p.write(   "students") 
#p.close()
#p = open(r"C:\Users\prasa\OneDrive\Desktop\file.json", "r")
#print(p.read())


# In[6]:


from scipy import stats

a=(9,12,15,18,21,24,27)
print(a)


# In[3]:


import json

dictionary = {"rss":34}

with open(r"C:\Users\prasa\OneDrive\Desktop\file.json","a")as outfile:
    json.dump(dictionary,outfile)
    
p=open(r"C:\Users\prasa\OneDrive\Desktop\file.json")
print(p.read())    


# In[ ]:





# In[18]:


import pandas as pd
df=pd.DataFrame([9,12,15,18,21,24,27])
df


# In[21]:


df=pd.DataFrame({"name":["prasad","arati","kavya","kavya","arnav","kavya"],
                "marks":[1,3,5,7,9,11]})
df


# In[22]:


import statistics
marks=[2,3,4,4,5,6,7,8,9,4,4,4,4,5,6,7,8,9,2,4,]
mean=statistics.mean(marks)
median=statistics.median(marks)
mode=statistics.mode(marks)

print("mean:",mean)
print("median:",median)
print("mode:",mode)


# In[21]:


import matplotlib.pyplot as plt

import seaborn as sns
import pandas as pd
variable=[12,10,15,18]
plt.hist(variable,bins=10)
plt.title("Histogram")
plt.xlabel("variable")
plt.ylabel("frequency")


plt.show()
y=variable.std()


# In[4]:


import pandas as pd

df=pd.DataFrame({"name":["a","b","c","d","e"],
                 "age":[12,23,11,13,14],
                 "sex":["m","f","m","m","m"]})
print(df)


# In[8]:


df['sex']=df['sex'].replace({"m":1,"f":0})
df


# In[67]:


import pandas as pd

df1=pd.DataFrame({"id":[1,2,3,4,5],
                 "name":["a","b","c","d","e"],
                 "age":[12,23,11,13,14],
                 "sex":["m","f","m","m","m"]})
print(df1)

df2=pd.DataFrame({"id":[1,2,3,4,5],
                 
                 "marks":[90,95,94,97,98]})
print(df2)


# In[68]:


merge_data=pd.merge(df1,df2,on="id")
merge_data


# In[69]:


var=df1.join(df2.set_index('id'),on='id')
var


# In[72]:


var=pd.concat([df1,df2],axis=0)
var


# In[78]:


var.isnull()


# In[79]:


var.dropna(axis=1)


# In[80]:


var.dropna(axis=0)


# In[86]:


var.fillna({"name":"ram","age":23,"sex":"m","marks":45})
var


# In[85]:


df1=pd.DataFrame({"name":["prasad","arati","kavya","kavya","arnav","kavya"],
                "marks":[1,3,5,7,9,11]})
df1


# In[ ]:





# In[44]:


df2=pd.DataFrame({
                "age":[9,12,15,18,21,24,27]})
df2


# In[45]:


var=df1.join(df2)
var


# In[62]:


var=pd.concat([df1,df2],axis=0)
var


# In[73]:



df1=pd.DataFrame({"id":[1,2,3,4,5],
                 "name":["a","b","c","d","e"],
                 "age":[12,23,11,13,14],
                 "sex":["m","f","m","m","m"]})
print(df1)



# In[75]:


filtered_data=df1[df1['sex']=='m']
filtered_data


# In[2]:


import pandas as pd
df=pd.DataFrame({"name":["prasad","arati","kavya","kavya","arnav","kavya","kavya","kavya","kavya"],
                "marks":[7,5,12,9,8,21,14,16,25]})
df
a=df['marks']
b=a.mean()
print(b)


# In[40]:


import pandas as pd
df=pd.DataFrame({"name":["prasad","arati","kavya","kavya","arnav","kavya","kavya","kavya","kavya"],
                "marks":[7,5,12,9,8,21,14,16,25]})
df
a=df['marks']
b=a.mean()
print(b)


# In[3]:


import pandas as pd
df=pd.DataFrame({"name":["prasad","arati","kavya","kavya","arnav","kavya","kavya","kavya","kavya"],
                "marks":[7,5,12,9,8,21,14,16,25]})
df
a=df['marks']
b=a.mean()
print(b)


# In[5]:


import pandas as pd
df=pd.DataFrame({"name":["prasad","arati","kavya","kavya","arnav","kavya"],
                "Age Group":["middle","young","old","middle","young","old"],
                "sex":["m","f","f","f","m","f"],
                "sal":[20000,40000,20000,40000,50000,20000]})
df
var=df.groupby('sal')
var.get_group(40000)


# In[6]:


import pandas as pd
df=pd.DataFrame({"name":["prasad","arati","kavya","kavya","arnav","kavya"],
                "Age Group":["middle","young","old","middle","young","old"],
                "sex":["m","f","f","f","m","f"],
                "sal":[20000,40000,20000,40000,50000,20000]})
df


# In[7]:


df.info


# In[8]:


df.head()


# In[9]:


df.tail()


# In[11]:


df.describe()


# In[12]:


df.columns


# In[13]:


df.shape


# In[12]:


from scipy import stats
data=[10,15,7,22,18,25,12,10,10,10]

#mean
mean_data=stats.mean(data)
print("Mean:",mean_data)
#median
median_data=stats.median(data)
print("median:",median_data)
#mode


mode_data=stats.mode(data)
print("mode:",mode_data.mode[0])


# In[22]:


from scipy import stats
marks=[2,3,4,4,5,6,7,8,9]
stats.mode(marks)


# In[23]:


import numpy as np

values = np.array([1,2,3,4,5])
weights=np.array([0.1,0.2,0.3,0.2,0.2])

weighted_mean=np.average(values,weights=weights)

print("weighted mean:",weighted_mean)


# In[9]:


p=open(r"C:\Users\prasa\OneDrive\Desktop\prasad1.xlsx")
p


# In[15]:


import pandas as pd
df=pd.read_excel(r"C:\Users\prasa\OneDrive\Desktop\prasad2.xlsx")
df


# In[16]:


df['age']=df['age'].replace({18:15})
df


# In[18]:


df.isnull()


# In[19]:


df.notnull()


# In[21]:


df.dropna()


# In[22]:


df.dropna(axis=1)


# In[23]:


df.dropna(axis=0)


# In[25]:


df.fillna("mi")


# In[28]:


"*"


# In[ ]:




