#!/usr/bin/env python
#-*- encoding: utf-8 -*-
from DataOperating import *
import random
import math
import sys

#封裝資料 (數組,適應度,初始溫度,計數器)
class Individual:
    def __init__(self,arr,fitness,T,k):
        self.arr = arr
        self.fitness = fitness
        self.T = T
        self.k = k
#初始設定
def initial(arr,T):
    #取得適應度
    curr_fitness = evaluate(arr)
    #計數器歸0
    k = 0
    #封裝
    individual = Individual(arr,curr_fitness,T,k)
    return individual
#模擬退火
def simulated_annealing(individual):
    arr = individual.arr
    curr_fitness = individual.fitness
    T = individual.T
    k = individual.k
    #取得附近狀態(隨機更改bit為0 or 1)
    arr = bit_change(arr)
    #評價附近狀態
    next_fitness = evaluate(arr)
    #附近能量是否更好
    if next_fitness > curr_fitness :
        curr_fitness = next_fitness
    else:
        #根據機率決定是否接受
        P = math.exp(-(k/T))
        Rnd = random.random()
        if P > Rnd:
            #接受當前適應度
            curr_fitness = next_fitness
    k +=1
    individual = Individual(arr,curr_fitness,T,k)
    return  individual

#模擬退火 參數: 數組,選代次數,初始溫度
def loop(arr,times,T):
    fitness_li = []
    individual = initial(arr,T)
    file=open('SA_data.txt','w')
    for i in range(times):
        individual = simulated_annealing(individual)
        file.write(repr(individual.fitness) + "\n")
        fitness_li.append(individual.fitness)
    file.close()
    graph_draw(fitness_li)

"""main"""
times = int(sys.argv[1])
T = int(sys.argv[2])
arr = read_arr()
loop(arr,times,T)

