#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import random
from string import strip
import matplotlib.pyplot as plt


def gen_rnd_arr(size):
    """
    generate random array include 0 and 1
    """

    file = open("random_array.txt","w")
    arr = []
    for i in range(size):
        x = random.randint(0,1)
        file.write(repr(x))
        arr.append(x)
    file.close()

def Gen_RandNode(arr):
    """
    generate random index position array
    """
    size = len(arr)
    node = random.randrange(size)
    while 1:
        if arr[node] == 1:
            node = random.randrange(size)
        else:
            break
    return node

def evaluate(arr):
    """
    calc array total 0
    """
    fitness = 0.0
    counter = 0.0
    for i in arr:
        counter +=1.0
        if i == 0 :
            fitness += 1.0
    return fitness

def bit_change(arr):
    """
    chagne array index to 1 or 0 randomly
    """
    length = len(arr)
    #隨機取點
    crpt = random.randint(0,length-1)
    if arr[crpt] == 1:
        arr[crpt] = 0
    return arr

def read_arr():
    """
    generate random array include 0 and 1
    """
    f = open("random_array.txt","r")
    arr = []
    for i in f.readline():
        i = int(i)
        arr.append(i)
    f.close()
    print len(arr)
    return arr

def graph_draw(list):
    """

    """
    plt.plot(list)
    plt.xlabel('generation')
    plt.ylabel('fitness')
    plt.show()

if __name__ == '__main__':
    gen_rnd_arr(200)

