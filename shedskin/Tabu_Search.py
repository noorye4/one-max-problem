#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import Basic
import random

#封裝資料 (數組,適應度,禁忌表長度)
class Individual:
    def __init__(self,arr,fitness,tabu_li):
        self.arr = arr
        self.fitness = fitness
        self.tabu_li = tabu_li
    def __repr__(self):
        return repr((self.arr,self.fitness,self.tabu_li))
    def getArr(self):
        return self.arr
    def getFitness(self):
        return self.fitness
    def getTabuList(self):
        return self.tabu_li

#記憶結構
class ChangePoint:
    def __init__(self,arr,memcrpt):
        self.arr = arr
        self.memcrpt = memcrpt
    def __repr__(self):
        return repr((self.arr,self.memcrpt))
    def getArr(self):
        return self.arr
    def getMemcrpt(self):
        return self.memcrpt

#更改數組其中一個bit為0 or 1,並紀錄更改位置
def RecordBitChange(arr,tabu_li):
    length = len(arr)
    crpt = random.randint(0,length-1)
    #如果隨機點在禁忌表內
    while crpt in tabu_li:
        #則再重新產生隨機點
        crpt = random.randint(0,length-1)
    if arr[crpt] == 1:
        arr[crpt] = 0
    #封裝
    change_point = ChangePoint(arr,crpt)
    return change_point

#初始設定
def Initial(arr,tabu_len):
    #禁忌表初始化(全設為0)
    tabu_li = []
    for i in range(tabu_len):
        tabu_li.append(0)
    #取得適應度
    curr_fitness = Basic.Fitness(arr)
    #封裝
    individual = Individual(arr,curr_fitness,tabu_li)
    return individual 
#禁忌搜尋
def TS(individual):
    #取得禁忌表
    tabu_li = individual.getTabuList()
    #取得當前數組
    arr = individual.getArr()
    #取得當前評價
    curr_fitness = individual.getFitness()
    #取得禁忌對象
    change_point = RecordBitChange(arr,tabu_li)
    #取得上次更改bit的位置
    crpt = change_point.getMemcrpt()
    #加入到禁忌表
    tabu_li.insert(0,crpt)
    #釋放最早加入的位置
    tabu_li.pop()
    #取得附近狀態
    arr = change_point.getArr()
    #評價附近狀態
    next_fitness = Basic.Fitness(arr)
    #附近狀態是否更好
    if next_fitness > curr_fitness:
        curr_fitness = next_fitness
    #封裝
    individual = Individual(arr,curr_fitness,tabu_li)
    return individual
#do something
