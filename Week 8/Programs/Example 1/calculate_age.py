# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 07:29:54 2024

@author: nicho
"""

import datetime

def get_age(yyyy:int, mm:int, dd:int) -> int:
    dob = datetime.date(yyyy, mm, dd)
    today = datetime.date.today()
    age = round((today - dob).days / 365.25) +1
    return age

# # Quick function test
# get_age(1980, 1, 23)
# get_age(2000, 2, 1)
# get_age(2000, 9, 7)
# 
# # Practice with the datetime class !
# x = datetime.date(2000, 3, 5)
# y = datetime.date(2000, 3, 6)
# z = datetime.date(2001, 3, 5)
# 
# x - y
# (x - y).days
# x - z
# (x - z).days / 365.25
# round((x - z).days / 365.25)

t = 2
