#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import random
from string import strip
import matplotlib.pyplot as plt

#產生隨機包含0,1 數組
def gen_rnd_arr(size):
    file = open("random_array.txt","w")
    arr = []
    for i in range(size):
        x = random.randint(0,1)
        file.write(repr(x))
        arr.append(x)
    file.close()
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
def evaluate(arr):
    fitness = 0.0
    counter = 0.0
    for i in arr:
        counter +=1.0
        if i == 0 :
            fitness += 1.0
    return fitness

#更改數組其中一個bit為0 or 1
def bit_change(arr):
    length = len(arr)
    #隨機取點
    crpt = random.randint(0,length-1)
    if arr[crpt] == 1:
        arr[crpt] = 0
    return arr

def read_arr():
    f = open("random_array.txt","r")
    arr = []
    for i in f.readline():
        i = int(i)
        arr.append(i)
    f.close()
    print len(arr)
    return arr

#繪製圖表
def graph_draw(list):
    plt.plot(list)
    plt.xlabel('generation')
    plt.ylabel('fitness')
    plt.show()

if __name__ == '__main__':
    gen_rnd_arr(200)

