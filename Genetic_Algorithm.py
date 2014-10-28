#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import Basic
import random

#封裝資料 (數組,適應度)
class Individual:
    def __init__(self,gene,fitness):
        self.gene = gene
        self.fitness = fitness

#封裝資料 (群體適應度,平均適應度,個體最佳適應度)
class Analysis_Fitness:
    def __init__(self,total_fitness,aver_fitness,better_fitness):
        self.total_fitness = total_fitness
        self.aver_fitness = aver_fitness
        self.better_fitness = better_fitness
#適應度函數
def Fitness(gene):
    fitness = Basic.Fitness(gene)
    return fitness

#產生初始種群(參數:種群規模,數組長度)
def Gen_pop(quantity,length):
    pop = []
    #print "初始種群"
    for i in range(quantity):
        gene = Basic.Gen_RandArr(length)
        #print gene
        pop.append(gene)
    return pop
#評估
def Evaluate(pop):
    eva_pop = []
    for i in pop:
        fitness = Fitness(i)
        individual = Individual(i,fitness)
        eva_pop.append(individual)
    return eva_pop

#分析
def AnalysisFitness(eva_pop,quantity):
    total_fitness = 0.0
    better_fitness = 0.0
    for i in eva_pop:
        if i.fitness > better_fitness:
            better_fitness = i.fitness
        total_fitness = i.fitness + total_fitness
    aver_fitness = total_fitness/quantity
    analysis_fitness = Analysis_Fitness(total_fitness,aver_fitness,better_fitness)
    #print "群體適應度" + repr(total_fitness)
    #print "平均適應度" + repr(aver_fitness)
    #print "最佳適應度 " + repr(better_fitness)
    return analysis_fitness

#輪盤選擇(參數: 評估後的pop,種群規模,分析適應度)
def Selection(eva_pop,quantity,analysis_fitness):
    #設定"選擇數組"為空
    selection_li = []
    #取得最個體最佳適應度
    better_fitness = analysis_fitness.better_fitness
    #取得群體適應度
    total_fitness = analysis_fitness.total_fitness
    #輪盤最大值
    RouletteSize = better_fitness/total_fitness
    #輪盤選擇
    #print "被選擇的 :"
    i = 0
    #X表示單個個體
    while 1:
        X = eva_pop[i]
        X_fitness = X.fitness
        X_prob = X_fitness/total_fitness #計算該個體被選中的機率
        #被選中則加入到"選擇數組"
        if X_prob > random.uniform(0.0,RouletteSize):
            selection_li.append(X.gene)
            #print X.getGene()
        #選滿種群大小則跳出
        if len(selection_li) == quantity:
            break
        i+=1
        #從頭開始選
        if i == quantity:
            i = 0
    return selection_li

#隨機單點交叉(參數: 選擇數組,基因長度,交配機率)
def Crossover(selection_li,length,cross_prob):
    #切片暫存
    temp_li = []
    #交配數組
    crossover_li = []
    #產生隨機交叉點
    crpt = random.randint(0,length-1)
    #print "交配 :"
    index = 0
    for i in selection_li:
        if cross_prob > random.random():
            i_f = i[0:crpt]     #gene前半
            i_b = i[crpt:]      #gene後半
            #存放切片gene
            temp_li.append(i_f)
            temp_li.append(i_b)
            index += 1
            #1~2交配 3~4交配 ....以此類推
            if index %2 == 0:
                matingA = temp_li[0] + temp_li[3]
                matingB = temp_li[1] + temp_li[2]
                crossover_li.append(matingA)
                crossover_li.append(matingB)
                #print matingA
                #print matingB
                temp_li = []
                crpt = random.randint(0,length-1) #產生隨機交叉點
        else:
            i_f = i[0:crpt]     #gene前半
            i_b = i[crpt:]      #gene後半
            #存放切片gene
            temp_li.append(i_f)
            temp_li.append(i_b)
            index += 1
            #1~2交配 3~4交配 ....以此類推
            if index %2 == 0:
                matingA = temp_li[0] + temp_li[1]
                matingB = temp_li[2] + temp_li[3]
                crossover_li.append(matingA)
                crossover_li.append(matingB)
                #print "未交配"
                #print matingA
                #print matingB
                temp_li = []
                crpt = random.randint(0,length-1) #產生隨機交叉點
    return crossover_li

#突變 (參數: 交配數組,基因長度,突變機率)
def Mutation(crossover_li,length,muta_prob):
    #print "突變 :"
    mutation_li = []
    for i in crossover_li:
        if muta_prob > random.random():
            crpt = random.randint(0,length-1) #產生隨機交叉點
            if i[crpt] == 0:
                i[crpt] = 1
            else:
                i[crpt] = 0
            #print i
            mutation_li.append(i)
        else:
            mutation_li.append(i)
    return mutation_li

