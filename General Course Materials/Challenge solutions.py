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




