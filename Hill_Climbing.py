#!/usr/bin/env python
#-*- encoding: utf-8 -*-
from DataOperating import *
import sys

#封裝資料 (數組,適應度)
class Individual:
    def __init__(self,arr,fitness):
        self.arr = arr
        self.fitness = fitness

def initial(arr):
    #取得適應度
    curr_fitness = evaluate(arr)
    individual = Individual(arr,curr_fitness)
    return individual

def hill_climbing(individual):
    #取得數組
    arr = individual.arr
    #取得適應度
    curr_fitness = individual.fitness
    #取得附近狀態
    arr = bit_change(arr)
    #評價附近狀態
    next_fitness = evaluate(arr)
    #附近狀態是否更好
    if next_fitness > curr_fitness:
        curr_fitness = next_fitness
    individual = Individual(arr,curr_fitness)
    return individual

def loop(arr,times):
    fitness_li = []
    #資料初始化
    individual = initial(arr)
    file=open('hill_climbing_data.txt','w')
    for i in range(times):
        individual = hill_climbing(individual)
        file.write(repr(individual.fitness) + "\n")
        fitness_li.append(individual.fitness)
    file.close()
    graph_draw(fitness_li)

"""main"""
times = int(sys.argv[1])
arr = read_arr()
loop(arr,times)

