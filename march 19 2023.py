#!/usr/bin/env python
# coding: utf-8

# In[1]:


#filter

def test(a):
    
    if a % 2 == 0:
        return True
    else:
        return False
a = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(test,a)))


# In[2]:


#mapping
def test(a):
    
    if a % 2 == 0:
        return True
    else:
        return False
a = [1,2,3,4,5,6,7,8,9,10]
print(list(map(test,a)))


# In[3]:


#reduce
from functools import reduce

def test(a,b):
    
    return (a*b)
a = [1,2,3,4,5,6,7,8,9,10]
print(reduce(test,a))


# In[4]:


# Create a deque
import collections

DoubleEnded = collections.deque(["Mon","Tue","Wed"])
print (DoubleEnded)
print("Adding to the right: ")
DoubleEnded.append("Thu")
print (DoubleEnded)

# append to the left
print("Adding to the left: ")
DoubleEnded.appendleft("Sun")
print (DoubleEnded)


# In[5]:


#chainmap

from collections import ChainMap
	
	
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
	
# Defining the chainmap
c = ChainMap(d1, d2, d3)
	
print(c)


# In[6]:


#counter
from collections import Counter
 
# Creation of a Counter Class object using
# string as an iterable data container
x = Counter("geeksforgeeks")
print(x)


# In[7]:


###namedtuple
from collections import namedtuple
 
# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])
 
# Adding values
S = Student('Nandini', '19', '2541997')
 
# Access using index
print("The Student age using index is : ", end="")
print(S[0])
 
# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)


# In[8]:


class a():
    
    "ajdgashd"
    def test(self):
        pass


# In[9]:


b = a()
b.__doc__


# In[10]:


#read
a = open(r"C:\Users\DK\requirement.txt", "r")
for i in a:
    print(i)


# In[11]:


#write
a = open(r"C:\Users\DK\demo.txt", "w")
a.write("hello")
a.write("today")
a.close()


# In[ ]:


#
a = open(r"C:\Users\DK\demo.txt", "a")
a.write("demo")
a.close()


# In[ ]:


#pandas

import pandas as pd
data = pd.read_csv("newhousing.csv")        #csv comma seperated values are tables
data.head()

