#!/usr/bin/env python
# coding: utf-8

# In[2]:


# linear search in python
def linear_Search(list1, n, key):  
  
    for i in range(0, n):  
        if (list1[i] == key):  
            return i  
    return -1  
  
  
list1 = [1 ,3, 5, 4, 7, 9]  
key = 9 
  
n = len(list1)  
res = linear_Search(list1, n, key)  
if(res == -1):  
    print("Element not found")  
else:  
    print("Element found at index: ", res)  


# In[16]:


def linear_search(arry,n,x):
    for i in range(0,n):
        if(array[i]==x):
            return i
    return-1
array=(2,4,0,1,9) 
x=int(input("Entre the element to be search:"))
n=len(array)
result= linear_search(array,n,x)
if(result==-1):
    print("Element not found")
else:
    print("Element found at index:",result)


# In[21]:


def binary_search(list1, low, high, n):   
  
   if low <= high:  
  
      mid = (low + high) // 2  
  
      if list1[mid] == n:   
         return mid   
  
      elif list1[mid] > n:   
         return binary_search(list1, low, mid - 1, n)   
  
      else:   
         return binary_search(list1, mid + 1, high, n)   
  
   else:   
      return -1  
  
 
list1 = [12, 24, 32, 39, 45, 50, 54]  
n = 39 
  

res = binary_search(list1, 0, len(list1)-1, n)   
  
if res != -1:   
   print("Element is present at index", str(res))  
else:   
   print("Element is not present in list1")  


# In[25]:


#bubble sort
def bubble_sort(list1):
    for i in range(0,len(list1)-1):
        for j in range(len(list1)-1):
            if(list1[j]>list1[j+1]):
                temp = list1[j]
                list1[j]=list1[j+1]
                list1[j+1]=temp
                
    return list1
list1 = [21,45,78,43,90,54,76,48]    
print("The unsorted list is:",list1)
print("The sorted list is:",bubble_sort(list1))


# In[28]:


#selection sort
def selection_sort(array):
    length=len(array)
    for i in range (length-1):
        minIndex=i
        for j in range(i+1,length):
            if array[j]<array[minIndex]:
                minIndex = j
        array[i],array[minIndex]=array[minIndex],array[i]
    return array
array=[21,3,6,33,9]
print("The sorted array is:",selection_sort(array))


# In[31]:


# creating a function for insertio
def insertion_sort(list1):  
  
        for i in range(1, len(list1)):  
  
            value = list1[i]  
  
            j = i - 1  
            while j >= 0 and value < list1[j]:  
                list1[j + 1] = list1[j]  
                j -= 1  
            list1[j + 1] = value  
        return list1  
  
list1 = [10, 5, 13, 8, 2]  
print("The unsorted list is:", list1)  
  
print("The sorted list1 is:", insertion_sort(list1))  


# In[1]:


def quicksort(arr):
    if len(arr)<= 1:
        return arr
    
    pivot = arr[len(arr)//2]
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    
    return quicksort(left)+middle+quicksort(right)

my_list = [3,6,8,10,1,2,1]
sorted_list=quicksort(my_list)
print(sorted_list)


# In[2]:


class StaticQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0
    def is_empty(self):
        return self.size == 0
    def is_full(self):
        return self.size == self.capacity
    def enqueue(self, item):
        if self.is_full():
             print("Queue is full. Cannot enqueue.")
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = item
            self.size += 1
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        else:
            item = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            return item
    def peek(self):
        if self.is_empty():
            print("Queue is empty. Cannot peek.")
            return None
        else:
            return self.queue[self.front]
if __name__ == "__main__":
    queue = StaticQueue(5)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print("Queue: ", queue.queue)
    print("Dequeue:", queue.dequeue())
    print("Queue after dequeue: ", queue.queue)
    print("Peek:", queue.peek())
    print("Queue size:", queue.size)
    print("Is the queue empty?", queue.is_empty())
    print("Is the queue full?", queue.is_full())


# In[15]:


def inserstion_sort(array,n,x):
    for i in range(0,n):
        if(array[i]==x):
            return i
    return -1
array=(3,6,4,9,6,4,5)
n=len(array)
x=int(input("Enter the element to be search:"))
result=inserstion_sort(array,n,x)
if(result==-1):
    print("Element is not found")
else:
    print("Element is search position:",result)


# In[2]:


def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
        arr[j + 1] = key
arr=(2,6,5,8,7)
print(arr)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




