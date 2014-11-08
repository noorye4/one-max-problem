#!/usr/bin/env python
#-*- encoding: utf-8 -*-
from DataOperating import *
import random
import sys

class Individual:
    """
    wrap a individual data struture
    """
    def __init__(self,gene,fitness):
        self.gene = gene
        self.fitness = fitness

class Analysis_Fitness:
    """
    wrap a fitness  data struture
    """
    def __init__(self,total_fitness,aver_fitness,best_fitness):
        self.total_fitness = total_fitness
        self.aver_fitness = aver_fitness
        self.best_fitness = best_fitness

#產生初始種群(參數:種群規模,數組長度)
def gen_pop(arr,quantity,length):
    quantity -= 1
    pop = []
    for i in range(quantity):
        gene = gen_other_gene(length)
        pop.append(gene)
    pop.append(arr)

    return pop

def gen_other_gene(size):
    arr = []
    for i in range(size):
        x = random.randint(0,1)
        arr.append(x)
    return arr
#評估
def evaluate_pop(pop):
    eva_pop = []
    for gene in pop:
        fitness = evaluate(gene)
        individual = Individual(gene,fitness)
        eva_pop.append(individual)
    return eva_pop

#分析
def AnalysisFitness(eva_pop,quantity):
    total_fitness = 0.0
    best_fitness = 0.0
    for i in eva_pop:
        if i.fitness > best_fitness:
            best_fitness = i.fitness
        total_fitness = i.fitness + total_fitness
    aver_fitness = total_fitness/quantity
    analysis_fitness = Analysis_Fitness(total_fitness,aver_fitness,best_fitness)
    #print "群體適應度" + repr(total_fitness)
    #print "平均適應度" + repr(aver_fitness)
    #print "最佳適應度 " + repr(best_fitness)
    return analysis_fitness

#輪盤選擇(參數: 評估後的pop,種群規模,分析適應度)
def selection(eva_pop,quantity,analysis_fitness):
    #設定"選擇數組"為空
    selection_li = []
    #取得最個體最佳適應度
    best_fitness = analysis_fitness.best_fitness
    #取得群體適應度
    total_fitness = analysis_fitness.total_fitness
    #輪盤最大值
    roulette_size = best_fitness/total_fitness
    #輪盤選擇
    #print "被選擇的 :"
    i = 0
    #X表示單個個體
    while 1:
        X = eva_pop[i]
        X_fitness = X.fitness
        X_prob = X_fitness/total_fitness #計算該個體被選中的機率
        #被選中則加入到"選擇數組"
        if X_prob > random.uniform(0.0,roulette_size):
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
def crossover(selection_li,length,cross_prob):
    #切片暫存
    temp_li = []
    #交配數組
    crossover_li = []
    #產生隨機交叉點
    crpt = random.randint(0,length-1)
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
                temp_li = []
                crpt = random.randint(0,length-1) #產生隨機交叉點
    return crossover_li

#突變 (參數: 交配數組,基因長度,突變機率)
def mutation(crossover_li,length,muta_prob):
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

#遺傳演算 參數: 種群規模,基因(數組)長度,選代次數,交配機率,突變機率
def loop(arr,quantity,gene_length,times,cross_prob,muta_prob):
    """
    parameters
    arr is about raw input array or call they gene
    quantity is about total gene
    times is array

    """
    total_fitness_li = []
    aver_fitness_li = []
    best_fitness = []
    file=open('genetic_algorithm_data.txt','w')
    pop = gen_pop(arr,quantity,gene_length)
    #重複 選擇 交叉 突變
    for i in range(times):
        #評估
        eva_pop = evaluate_pop(pop)
        #分析
        analysis_fitness = AnalysisFitness(eva_pop,quantity)
        total_fitness_li.append(analysis_fitness.total_fitness)
        aver_fitness_li.append(analysis_fitness.aver_fitness)
        file.write(repr(analysis_fitness.best_fitness) + "\n")
        best_fitness.append(analysis_fitness.best_fitness)
        #選擇
        selection_li = selection(eva_pop,quantity,analysis_fitness)
        #交配
        crossover_li = crossover(selection_li,gene_length,cross_prob)
        #突變
        mutation_li = mutation(crossover_li,gene_length,muta_prob)
        #更換種群
        pop = mutation_li
    file.close()
    graph_draw(aver_fitness_li)

"""main"""
arr = read_arr()
quantity = 20
gene_length = len(arr)
times = 1000
cross_prob = 0.75
muta_prob = 0.01
loop(arr,quantity,gene_length,times,cross_prob,muta_prob)
