#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import os
import matplotlib.pyplot as plt

f = open("HC_data.txt")

list = []
for line in f.readlines():
	line=line.strip('\n')  
	list.append(line)
#	print line
print list

def MatlabDraw(list):
    plt.plot(list)
    plt.xlabel('generation')
    plt.ylabel('fitness')
    plt.show()
    
MatlabDraw(list)

