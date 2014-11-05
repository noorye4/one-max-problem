#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import Basic

import Hill_Climbing
import Tabu_Search
import Simulated_Annealing
import Genetic_Algorithm

import matplotlib.pyplot as plt
import sys
import getopt

#幫助
def Help():
    print """
      -r :Generate Array length
      -t :Select the number of generations
      -l :Tabu list length ,the parameter is required if adopt Tabu Search
      -T :Initial temperature ,the parameter is required if adopt Simulated Annealing
      -q :Population quantity ,the parameter is required if adopt Genetic Algorithm
      -c :Crossover probability recommend 0.6 ~ 0.8
      -m :Mutation probability recommend 0.01
      --HC :run 'Hill Climbing'
      --TS :run 'Tabu Search'
      --SA :run 'Simulated Annealing'
      --GA :run 'Genetic Algorithm'
      Usage : python Experiment.py -r 200 -t 1000 --HC
      Usage : python Experiment.py -r 200 -t 1000 -l 7 --TS
      Usage : python Experiment.py -r 200 -t 1000 -T 100 --SA
      Usage : python Experiment.py -r 200 -t 1000 -q 20 -c 0.75 -m 0.01 --GA
     """

#繪製圖表
def MatlabDraw(list):
    plt.plot(list)
    plt.xlabel('generation')
    plt.ylabel('fitness')
    plt.show()
#爬山 參數:數組,選代次數
def exp_HC(arr,times):
    #初始化 適應度list
    fitness_li = []
    #資料初始化
    individual = Hill_Climbing.Initial(arr)
    file=open('HC_data.txt','w')
    for i in range(times):
        individual = Hill_Climbing.HC(individual)
        file.write(repr(individual.fitness) + "\n")
        fitness_li.append(individual.fitness)
    file.close()
    MatlabDraw(fitness_li)
#禁忌搜尋 參數:數組,選代次數,禁忌表長度
def exp_TS(arr,times,tabu_len):
    fitness_li = []
    individual = Tabu_Search.Initial(arr,tabu_len)
    file=open('TS_data.txt','w')
    for i in range(times):
        individual = Tabu_Search.TS(individual)
        file.write(repr(individual.fitness) + "\n")
        fitness_li.append(individual.fitness)
    file.close()
    MatlabDraw(fitness_li)
#模擬退火 參數: 數組,選代次數,初始溫度
def exp_SA(arr,times,T):
    fitness_li = []
    individual = Simulated_Annealing.Initial(arr,T)
    file=open('SA_data.txt','w')
    for i in range(times):
        individual = Simulated_Annealing.SA(individual)
        file.write(repr(individual.fitness) + "\n")
        fitness_li.append(individual.fitness)
    file.close()
    MatlabDraw(fitness_li)
#遺傳演算 參數: 種群規模,基因(數組)長度,選代次數,交配機率,突變機率
def exp_GA(quantity,gene_length,times,cross_prob,muta_prob):
    total_fitness_li = []
    aver_fitness_li = []
    best_fitness = []
    file=open('GA_data.txt','w')
    pop = Genetic_Algorithm.Gen_pop(quantity,gene_length)
    #重複 選擇 交叉 突變
    for i in range(times):
        #評估
        eva_pop = Genetic_Algorithm.Evaluate(pop)
        #分析
        analysis_fitness = Genetic_Algorithm.AnalysisFitness(eva_pop,quantity)
        total_fitness_li.append(analysis_fitness.total_fitness)
        aver_fitness_li.append(analysis_fitness.aver_fitness)
        file.write(repr(analysis_fitness.aver_fitness) + "\n")
        best_fitness.append(analysis_fitness.better_fitness)
        #選擇
        selection_li = Genetic_Algorithm.Selection(eva_pop,quantity,analysis_fitness)
        #交配
        crossover_li = Genetic_Algorithm.Crossover(selection_li,gene_length,cross_prob)
        #突變
        mutation_li = Genetic_Algorithm.Mutation(crossover_li,gene_length,muta_prob)
        #更換種群
        pop = mutation_li
    file.close()
    #matlab繪圖
    MatlabDraw(aver_fitness_li)

#命令行參數
opts, args = getopt.getopt(sys.argv[1:], "hr:t:l:T:q:c:m:", ["HC", "TS","SA","GA"])
for op, value in opts:
    if op == "-h":
        input = value
        Help()
    elif op == "-r":
        gene_length = value
        gene_length = int(gene_length)
        print value
        arr = Basic.Gen_RandArr(gene_length)
    elif op == "-t":
        times = value
        times = int(times)
    elif op == "--HC":
        print "Run Hill Climbing..."
        print " "
        exp_HC(arr,times)
    elif op == "-T":
        T = value
        T = float(T)
        print "T "
        print T
    elif op == "-l":
        tabu_len = value
        tabu_len = int(tabu_len)
    elif op == "-q":
        quantity = value
        quantity = int(quantity)
    elif op == "-c":
        cross_prob = value
        cross_prob = float(cross_prob)
    elif op == "-m":
        muta_prob = value
        muta_prob = float(muta_prob)
    elif op == "--TS":
        print "Run Tabu Search..."
        print ""
        exp_TS(arr,times,tabu_len)
    elif op == "--SA":
        print "Run Simulated Annealing..."
        print ""
        exp_SA(arr,times,T)
    elif op == "--GA":
        print "Run Genetic Algorithm..."
        print ""
        exp_GA(quantity,gene_length,times,cross_prob,muta_prob)
