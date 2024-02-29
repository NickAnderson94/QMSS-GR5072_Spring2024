# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 19:24:39 2023

@author: nicka
"""

###  Week 1 ===================================

items = ["spam", "eggs", "beans", "bacon", "sausage"]
items[::-1] # reverses order
items[3:0:-1]
items[3:1:-1]
items[4:0:-1] # reverse order and don't include the last element, which is spam after the flip


# spam, eggs, sausage, spam, and spam
[items[0]] + [items[1]] + [items[4]] + [items[0]]*2

# add lobster
items + ["lobster"]



###  Week 3 ===================================

import numpy as np
np.array(range(2,21,2))
np.arange(2,21,2)


## Gender challenge
# solution 1
gender = np.array(["Female", "F", "Female", "M", "Male"])  
gender
gender.astype('<U1') # Select first character, by converting to a type which only stores one byte

# solution 2
np.where(len(gender)==1, gender, gender.astype('<U1'))

# solution 3
np.where(np.where(gender == "Female", "F", gender) == "Male", "M", "NA")

# solutoin 4
np.where(np.in1d(gender, ['F', 'M']), gender, gender.astype('<U1'))


## Linear algebra challenge
# Generate data for this exercise
rng = np.random.default_rng(seed=3252)
x1 = rng.standard_normal(1000)
x2 = rng.standard_normal(1000)
Y = -1 + 2*x1 + 7*x2 + rng.standard_normal(1000)

# Step 1
X = np.column_stack((np.ones(1000), x1, x2))
X
#Step 2
beta_hat = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(Y)
beta_hat


##  Week 5 ===================================

# Fix function to accept np.inf values
def rescale01(x):
    x = x.replace(np.inf, np.nan)
    min_ = x.min()  
    max_ = x.max()
    return ( x - min_ ) / ( max_ - min_ )
rescale01(x)



###  Week 6 ===================================

### Practice for for loops

# Generate data for practice problems
import numpy as np
import pandas as pd 
import seaborn as sns

rng = np.random.default_rng(seed=3252)

a = rng.standard_normal(10)
b = rng.standard_normal(10)
c = rng.standard_normal(10)
d = rng.standard_normal(10)

the_dict = {'a':a,'b':b,'c':c,'d':d}

df = pd.DataFrame(the_dict)

# a) Compute the mean of every column in df.
### iteration using a for loop
output = []
for i in df.columns:
    output.append(round(np.mean(df[i]),2))
output


# b) Determine the type of data each column holds.
output = []
for i in df.columns:
    data_type = type(df[i][0])
    output.append(data_type) 
output


# c) Compute the number of unique values in each column of iris
from sklearn import datasets # to load iris dataset
iris0 = datasets.load_iris()
iris = pd.DataFrame(data=iris0.data, columns=iris0.feature_names)

unique_vals = []
for i in iris.columns:
    unique_vals.append(len(np.unique(iris[i])))          
unique_vals


# d) Write a function that prints the mean of each numeric column in the iris dataframe. 
# This for loop will need to check whether each dtype is numeric. 
# If it is, then you will compute and store the mean, adding it to a list object.
from pandas.api.types import is_numeric_dtype
means = []
for col in iris.columns:
    # if type(iris[col][0]) == np.float64:   # Works, but only checks for one numeric data type!
    if is_numeric_dtype(iris[col]):  # Recall that you need to tell Python this col is in the iris df
        m = np.mean(iris[col])       # Compute mean
        means.append(m)              # Append mean
means       


###  Week 7 ===================================

import re

# regex challenge 1:
string = '39801 356, 2102 1111'
pattern = '\d{3} \d{2}'

# match variable contains a Match object.
match = re.search(pattern, string) 
print(match)
   

# regex challenge 2:
string = "Python is fun"

# check if 'Python' is at the beginning
match = re.match('Python', string)
print(match)

 
# regex challenge 3:   
# Match strings starting with "The"
regex = 'The'
strings = ['The quick brown fox', 'The lazy dog', 'A quick brown fox']
for string in strings:
    if re.match(regex, string):
        print(f'Matched: {string}')
    else:
        print(f'Not matched: {string}')    
  
    
# regex challenge 4:
string0 = ["I went to him at 11 A.M. on 4th July 1886", "She went to him at 10 A.M. on 4th July 1890"]
for string in string0:
    print(re.findall("\d{4}", string))


