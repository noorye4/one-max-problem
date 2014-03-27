#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import Basic
import random
import math

#封裝資料 (數組,適應度,初始溫度,計數器)
class Individual:
    def __init__(self,arr,fitness,T,k):
        self.arr = arr
        self.fitness = fitness
        self.T = T
        self.k = k
    def __repr__(self):
        return repr((self.arr,self.fitness,self.T,self.k))
    def getArr(self):
        return self.arr
    def getFitness(self):
        return self.fitness
    def getTemp(self):
        return self.T
    def getK(self):
        return self.k
#初始設定
def Initial(arr,T):
    #取得適應度
    curr_fitness = Basic.Fitness(arr)
    #計數器歸0
    k = 0
    print "初始溫度 " + repr(T) 
    print "初始狀態..."
    print arr
    print "適應度 :" + repr(curr_fitness)
    #封裝
    individual = Individual(arr,curr_fitness,T,k)
    return individual 
#模擬退火
def SA(individual):
    arr = individual.getArr() #取得數組
    curr_fitness = individual.getFitness() #取得適應度
    T = individual.getTemp() #取得溫度
    k = individual.getK() #取得評估次數
    #取得附近狀態(隨機更改bit為0 or 1)
    arr = Basic.BitChange(arr)
    #評價附近狀態
    next_fitness = Basic.Fitness(arr)
    #附近能量是否更好
    if next_fitness > curr_fitness :
        curr_fitness = next_fitness
    else:
        #根據機率決定是否接受
        P = math.exp(-(k/T))
        Rnd = random.random()
        print "P " + repr(P) + "  " + "Rnd " + repr(Rnd)
        if P > Rnd:
            print "接受..."
            #接受當前適應度
            curr_fitness = next_fitness
        else:
            print "不接受..."
    print "適應度 :" + repr(curr_fitness)
    print "當前狀態" 
    print arr 
    print "當前溫度" + repr(T)
    k +=1
    #封裝
    individual = Individual(arr,curr_fitness,T,k)
    return  individual

if __name__ == '__main__':
    print ""


