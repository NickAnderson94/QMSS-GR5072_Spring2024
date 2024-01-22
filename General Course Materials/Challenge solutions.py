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



