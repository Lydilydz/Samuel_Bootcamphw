# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 15:13:52 2019

@author: Twilight Navigator
"""

import csv
import os

#set path for file
csvpath = "Resources/budget_data.csv"

with open("budget_data.csv",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")
