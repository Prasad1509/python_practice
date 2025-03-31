#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("hallo world")


# In[1]:


def power(a,b):
    if b!=0:
        return a * power(a,b-1)
    else:
        return 1
    a=int(input("enter a number : "))
    b=int(input("enter a number : "))
    print(a,"to the power",b,"is",power(a,b))


# In[5]:


def power(a,b):
    if b!=0:
        return a * power(a,b-1)
    else:
        return 1
    a=int(input("enter a number : "))
    b=int(input("enter a number : "))
    print(a,"to the power",b,"is",power(a,b))


# In[1]:


def power(a,b):
    if b!=0:
        return a * power(a,b-1)
    else:
        return 1
    a=int(input("enter a number : "))
    b=int(input("enter a number : "))
    print(a,"to the power",b,"is",power(a,b))
    


# In[1]:


count = 0

my_string = "Programiz"
my_char = "r"

for i in my_string:
    if i == my_char:
        count += 1
        
        
print(count)        


# In[2]:


list1 = [10, 20, 4, 45, 99]
print("largest element is:" , max(list1))


# In[5]:


mylist = ["python", "math", "electronics", "python", "dbms", "python", "math"]
mylist=list(dict.fromkeys(mylist))
print(mylist)


# In[ ]:


import random
a=[]
n=int(input("enter number of elements:"))
for j in range(n):
    a.append(random.randist(1,20))
print('randomised list is : ',a)    


# In[ ]:


import random
n=random.randlist(1,20)
print(n)


# In[1]:


def merge_list(list_1, list_2):
   merged_list = list_1 + list_2
   merged_list.sort()
   return(merged_list)

list_1 = [20, 18, 9, 51, 48, 31]
list_2 = [28, 33, 3, 22, 15, 20]
print("The first list is :")
print(list_1)
print("The second list is :")
print(list_2)
print(merge_list(list_1, list_2))


# In[2]:


my_list = []
if my_list == []:
    print("the list is empty")


# In[1]:


my_list = ["prasad"]
if my_list == []:
    print("the list is empty")


# In[4]:


list1 = [11, 22, 1, 2, 5, 67, 21, 32]
#using built-in sort method
list1.sort()
#second last element
print("second largest element in the list is:", list1[-2])


# In[7]:


# python   print second largest element in list
 
lst = [10, 20, 4, 45, 99]
maximum1 = max(lst)
maximum2 = max(lst, key=lambda x: min(lst)-1 if (x == maximum1) else x)
print(maximum2)


# In[ ]:





# In[8]:


a= [10, 20, 4, 45, 99]
m=max(a)
x=[a for i, a in enumerate(a) if a<m]
print(max(x))


# In[ ]:


list = [12,23,34,45,56,67,78,89,]
for index in range (len(list)):
    value = list 
    
    print(index,value)


# In[4]:


marks = {"kirti":40,"kavya":56,"pari":48}
print(marks)
sv = sorted(marks.items(),key = lambda x : x[1])
print(sv)


# In[ ]:


def counline():
    file = open('prasad','r')
    line = file.readlines()
    c = 0
    for i in line:
        if i [0] == 'a' or i [0] == 'A':
        c=c+1
        print("total number of line start with a:",c)
        file.close()
counline()


# In[11]:


f = open("prasad", "r")
print(f.read())


# In[ ]:


int words = 0;
int lines = 0;
int chars = 0;
while(in.hasnextline()){
    lines++;
    string line = in.nextline();
    chars +=line.length();
    words +=new stringtokenizer(line," ,").counttokens();
}


# In[1]:


import numpy as np
ini_array = np.array([1,2,3,6,4,5])
res = np.flip(ini_array )
print("final array", str(res))


# In[20]:


def read_data():
    count = 0
    f = open("prasad",'r')
    s = f.readlines()
    for i in s:
        if i[0] == 'the':
            count += 1
        else:
            pass
        print(count,""+"lines")
read_data()        


# In[ ]:


print(max(open('prasad', key=len)))


# In[15]:


import numpy as np
c = np.array([1, 2, 3, 4])
add_ans = c
print(add_ans)


print(add_ans)


# In[ ]:


import numpy as np
c = np.array([1, 2, 3, 4])
add_ans = a+b+c
print(add_ans)

add_ans = np.add(a, b, c)
print(add_ans)


# In[11]:


import numpy as np
a = np.array([5, 2, 3, 1])
b = np.array([2, 5, 1, 6])

add_ans = a+b
print(add_ans)


# In[ ]:


def largest
arr = [10, 324, 45, 90,9808]
n = len(arr)
ans = largest(arr,n)
print ("largest in given array is",max)


# In[7]:


f=open("prasad","r")
wrd=input("enter the word to be searched")
#store the string in s
s=f.read()
f=s.split()
count=0
for i in f:
    if(i==wrd):
        count+=1
print("word {} occurred {} times".format(wrd,count))        


# In[19]:


# count only those lines starting with "a"
def read_data():
    count = 0
    f = open("prasad","r")
    s = f.readlines()
    for i in s:
        if i[0]=='a':
            count += 1
        else:
            pass
        print(count,""+"lines")
read_data()        
        


# In[21]:


# count only those lines starting with "a"
def read_data():
    count = 0
    f = open("prasad","r")
    s = f.readlines()
    for i in s:
        if i[0]=='a':
            count += 1
        else:
            pass
        print(count,""+"lines")
read_data()      


# In[35]:


x=open("prasad","r")
y=x.readlines()
n=int(input("enter the no of lines"))
print(y[-n])


# In[36]:


f=open("prasad","r")
def countthe():
    count=0
    lst=f.readlines()
    for i in lst:
        if i[0]=="the":
            print(i)
            count += 1

print("so for the number of sentences started with the:",countthe())
f.close()


# In[39]:


f=input("enter a file")
f1=f.split(' ')
for i in f1:
    print(i,f1.count(i))


# In[41]:


f=open("prasad","r")
data=f.read()
print("given text file data is",data)

occurrences=data.count('generation')
print("number of occurrence of the word:",occurrences)
occurrences=data.count('language')
print("number of occurrence of the word:",occurrences)


# In[46]:


string="once in a blue moon";
ch='-';
#replace space with specific character ch
string=string.replace('',ch);
print("string after replacing spaces with given character:");
print(string);


# In[2]:


a=5
b=8
x=a+b
print(x)


# In[8]:


x=3
y=2
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)
print(x//y)


# In[9]:


print("enter the radius of a circle")
r=int(input())
area=3.14*r*r
print("area of circle is:",area)


# In[10]:


b = float(input("enter base: "))
h = float(input("enter height: "))

area = 0.5*b*h
print("area of tringle is: ",area)


# In[12]:


x=45
y=54

x, y = y, x
print("the value of x is",x)
print("the value of y is",y)


# In[16]:


import random
a=random.randint(0,10)
print(a)


# In[17]:


def function (n):
    if n%2 == 0:
        print("number is even ")
    else:
        
        print("number is odd ")
function(7)        
        
        


# In[19]:


num=12
if num>0:
    print("it is a positive number")
elif num == 0:
    print("it is zero")
else:
    print("it is a negative number")
    


# In[25]:


num = int(input("enter any number : "))
print("\nnatural numbers from 1 to ",num)
for i in range(1, num + 1):
    print(i,end=" ")


# In[23]:


num = int(input("enter any number : "))
print("\nnatural numbers from 1 to ",num)


# In[1]:


a="a b c"
   
b="n m o"
g=" "
c=a + g+b
print(c)
   


# In[ ]:


import numpy as np
arr =np . arry[(1,2,3,4,5)]
print(arr)


# In[10]:


z = ["h","l","m","b"]
z.pop(3)
print(z)


# In[17]:


a=("kalika")

l=a.upper()

print(l)


# In[3]:


d={"A":300,"B":150,"c":500,"D":850,"E":400}
l=list(d.values())

print(l)


# In[3]:


stack = []
stack.append(10)
stack.append(20)
stack.append(30)
stack


# In[23]:


stack.pop(1)


# In[24]:


stack.append(41)
stack


# In[ ]:


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


f = open("prasad", "r")
print(f.read())


# In[4]:


f = open("prasad", "w")
f.write("Good Luck")
f.close()
f = open("prasad", "r")
print(f.read())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




