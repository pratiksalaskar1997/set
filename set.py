# Set Problems:

dir(set)

## 1. find size of set:

s = {1,2,3,4,5,6}

import sys

#1 method:
sys.getsizeof(s)

#2 method:
s.__sizeof__()

## 2. iterate over a set in python

s = {1,2,3,4,5,6}

#1 for loop:
for i in s:
    print(i)

#2 method:
for i in enumerate(s):
    print(i[0], i[1])

#3 method:
s1 = list(s)
for i in range(len(s)):
    print(s1[i])

#4 method:
c = list(i for i in s)

print(*c)

#5 method:
print(*list(map(lambda x: x, s)))

## 3. maximum and minimum in python

s

#1  method:
max(s)
min(s)

#2 method:
list(s)[0]  # min
list(s)[-1] # max

#3 method:
{i for i in s if i==max(s)}
{i for i in s if i==min(s)}

#4 method:
list(filter(lambda x: x==list(s)[-1],s))[0]
list(filter(lambda x: x==list(s)[0],s))[0]

#5 method:
[i for i in list(map(lambda x: x if x==max(s) else 'n',s)) if type(i)==int][0]
[i for i in list(map(lambda x: x if x==min(s) else 'n',s)) if type(i)==int][0]

## 4. revome item from set

s = {1, 2, 3, 4, 5, 6}
s

it = 2

#1 method:
s.remove(it)

#2 method:
{i for i in s if i!=it}

#3 method:
s1=set()
for i in s:
    if i!=it:
        s1.add(i)
s1

#4 method:
set(filter(lambda x: x!=it,s))

#5 method:
{i for i in list(map(lambda x:x if x!=it else 'n',s)) if type(i)==int}

## 5.check if two list have at least one element common

x1 = [1,2,3,4,5]
x2 = [5,6,7,8,9]

#1 method:
if len(set(x1).intersection(set(x2)))>=1:
    print('True')
else:
    print('False')

#2 method:
x3=[]
for i in x1:
    if i in x2:
        x3.append(i)
if len(x3)>0:
    print('True')
else:
    print('False')

#3 method:
res = [True if i in x2 else False for i in x1 ]
if True in res:
    print('True')
else:
    print('False')

#4 method:
if len(list(filter(lambda x: x in x2,x1)))>0:
    print('True')
else:
    print('False')

## 6. find missing and additional value in two list

x1

x2

#1 method:
#missing x1:
set(x2).difference(set(x1))

#missing in x2:
set(x1).difference(set(x2))

#additional in x1:
set(x1).difference(set(x2))

#additional in x2:
set(x2).difference(set(x1))

#2 method:
#missing in x2:
[i for i in x1 if i not in x2]

#missing in x1:
[i for i in x2 if i not in x1]

#aditional in x1:

[i for i in x1 if i not in x2]

# additional in x2
[i for i in x2 if i not in x1]

## 7. to find difference between two list:

x1

x2

#1 method:
set(x1).difference(set(x2))

## 8. count number of vowels using set:

s = 'geeksforgEeks'

v = set('aeiou')
v

len([i for i in s if i.lower() in v])

#2 method:
count=0
for i in s:
    if i.lower() in v:
        count+=1
count

#3 method:
list(enumerate((filter(lambda x: x.lower() in v,s ))))[-1][0]+1

import numpy as np
len([ i for i in list(map(lambda x: x if x.lower() in v else np.nan,s )) if type(i)==str])

