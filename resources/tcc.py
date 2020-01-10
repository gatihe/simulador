#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random 


# In[2]:

    



#defining parameters
bast_param = [0,5] #ba prefix for below average student
avst_param = [5,7] #av prefix for average student
aast_param = [7,10] #aa prefix for above average student


#defining parameters 2
bast_param1 = ["Below Average",0,5] #ba prefix for below average student
avst_param1 = ["Above Average",5,7] #av prefix for average student
aast_param1 = ["Average",7,10] #aa prefix for above average student
menu_keep = 0


#students quantities per parameter
bast_qtd = 5 
avst_qtd = 3
aast_qtd = 8
st_total = bast_qtd + avst_qtd + aast_qtd

#Defining Subjects
subjects = ["Disciplina 1", "Disciplina 2", "Disciplina 3", "Disciplina 4", "Disciplina 5"]

students = []

#counter for students ids creation
i = 0

#counters and variable for grades creation
a = 0
b = 0
newgradeline = []

grade = []

while(menu_keep == 0):
    menu1 = input("Selecione uma opção \n 1. Nova simulação \n 2. Configurar parametros\n 3. Configurar alunos \n 4. Configurar disciplinas\n 5. Exportar parâmetros\n\n")
    if menu1 == 1:
        print('New simulation')
        menu_keep = menu_keep + 1
        continue
    elif menu1 == '2':
        menu2 = input("1. Listar parametros atuais \n2. Configurar novos parametros\n 3. Fazer upload de parametros")
        if menu2 == '1':
            print("Parametro: " + bast_param1[0] + "\n Mínimo: " + str(bast_param1[1]) + "\n Máximo: " + str(bast_param1[2]))
            continue           
    elif menu1 == '3':
        menu2 = input("1. Mostrar configuração atual \n2. Nova configuração")
        if menu2 == '1':
            print("Mostrando configuração")
            pass
    elif menu1 == '4':
        print("okay")
    elif menu1 == '5':
        menu_keep = menu_keep + 1
        continue


#creating students and grades
while(i < st_total):
    newstudent = random.randint(100000,199999)
    #excluding duplicates
    if newstudent not in students:
        students.append(newstudent)
        i = i+1    


# In[3]:


#below averagge students
while (a < bast_qtd):
    b = 0
    newgradeline = []
    grade.append(newgradeline)
    while (b<len(subjects)):
        gen_grade = round(random.uniform(bast_param[0],bast_param[1]),2)
        newgradeline.append(gen_grade)
        b = b+1
    a = a +1
a = 0

#average students
while (a < avst_qtd):
    b = 0
    newgradeline = []
    grade.append(newgradeline)
    while (b<len(subjects)):
        gen_grade = round(random.uniform(avst_param[0],avst_param[1]),2)
        newgradeline.append(gen_grade)
        b = b+1
    a = a +1
a = 0

#above average students
while (a < aast_qtd):
    b = 0
    newgradeline = []
    grade.append(newgradeline)
    while (b<len(subjects)):
        gen_grade = round(random.uniform(aast_param[0],aast_param[1]),2)
        newgradeline.append(gen_grade)
        b = b+1
    a = a +1


# In[4]:


#generating table
simulation = pd.DataFrame (grade,index=students, columns=subjects)

simulation

simulation.to_csv(r'test.csv')

