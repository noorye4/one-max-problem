#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import random

#產生隨機包含0,1 數組
def Gen_RandArr(size):
    arr = [] 
    for i in range(size):
        x = random.randint(0,1)
        arr.append(x)
    return arr
#產生隨機點
def Gen_RandNode(arr):
    size = len(arr)
    node = random.randrange(size)
    while 1:
        if arr[node] == 1:
            node = random.randrange(size)
        else:
            break
    return node
#適應度函數
def Fitness(arr):
    fitness = 0.0
    counter = 0.0
    for i in arr:
        counter +=1.0
        if i == 0 :  
            fitness += 1.0
    return fitness

#更改數組其中一個bit為0 or 1
def BitChange(arr):
    length = len(arr)
    #隨機取點
    crpt = random.randint(0,length-1)
    if arr[crpt] == 1:
        arr[crpt] = 0
    return arr

if __name__ == '__main__':
    print ""
