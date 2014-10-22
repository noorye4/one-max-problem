#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import Basic

#封裝資料 (數組,適應度)
class Individual:
    def __init__(self,arr,fitness):
        self.arr = arr
        self.fitness = fitness
    def __repr__(self):
        return repr((self.arr,self.fitness))
    def getArr(self):
        return self.arr
    def getFitness(self):
        return self.fitness

#初始設定
def Initial(arr):
    #取得適應度
    curr_fitness = Basic.Fitness(arr)
    #print "初始狀態..."
    #print arr
    #print "適應度 :" + repr(curr_fitness)
    #封裝
    individual = Individual(arr,curr_fitness)
    return individual

#爬山
def HC(individual):
    #取得數組
    arr = individual.getArr()
    #取得適應度
    curr_fitness = individual.getFitness()
    #取得附近狀態
    arr = Basic.BitChange(arr)
    #評價附近狀態
    next_fitness = Basic.Fitness(arr)
    #附近狀態是否更好
    if next_fitness > curr_fitness:
        curr_fitness = next_fitness
    #print "當前狀態"
    #print arr
    #print "適應度 :" + repr(curr_fitness)
    #封裝
    individual = Individual(arr,curr_fitness)
    return individual

#if __name__ == '__main__':
    #print ""
