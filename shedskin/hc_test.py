#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import Basic
import Hill_Climbing
from time import *

def exp_HC(arr,times):
    #初始化 適應度list
    fitness_li = []
    #資料初始化
    individual = Hill_Climbing.Initial(arr)
    file=open('HC_data.txt','w')
    start_time = time()
    for i in range(times):
        individual = Hill_Climbing.HC(individual)
        file.write(repr(individual.getFitness()) + "\n")
        fitness_li.append(individual.getFitness())
    file.close()
    end_time = time()
    print end_time - start_time

arr = Basic.Gen_RandArr(20)    
exp_HC(arr,100)
