#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random 
import os


# In[2]:

    
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


print("teste")

#defining parameters
bast_param = [0,5] #ba prefix for below average student
avst_param = [5,7] #av prefix for average student
aast_param = [7,10] #aa prefix for above average student


#defining parameters 2
menu_keep = 0
params = ["Below Average", 0, 5, 10, "Above Average", 5, 7, 10, "Average", 7, 10, 10]
params_total = len(params)/4









#students quantities per parameter
bast_qtd = 5 
avst_qtd = 3
aast_qtd = 8



#Defining Subjects
subjects = ["EB101", "SI100", "SI120", "SI201", "SI250"]

turmas = [1,2,1,2,3]

subjects_with_turmas = []

sub = 0
turm = 0

while(sub < len(subjects)):
    if turmas[sub] == 1:
        subjects_with_turmas.append(subjects[sub])
    else:
        turm = 0
        strturma = 65
        while (turm < turmas[sub]):
            subjects_with_turmas.append(subjects[sub] + ' '+chr(strturma))
            strturma = strturma + 1
            turm = turm + 1
    sub = sub+1    

students = []

prereqs = ['SI100', 'SI250']


new_prereqs = []

newer_prereqs = []

laco = 1

while (laco < len(prereqs)):
    subject_to_have_new_prereq = prereqs[laco]
    index_holder_to_match_turmas = subjects.index(subject_to_have_new_prereq)
    if turmas[index_holder_to_match_turmas] == 1:
        new_prereqs.append(prereqs[laco-1])
        new_prereqs.append(prereqs[laco])
    else:
        x = 1
        turm = 65
        while (x < turmas[index_holder_to_match_turmas]):
            new_prereqs.append(prereqs[laco-1] + ' '+chr(turm))
            new_prereqs.append(prereqs[laco])
            turm = turm+1
            x = x +1
    laco = laco + 2


laco2 = 1

while(laco2 < len(new_prereqs)):
    sub_with_prereq = new_prereqs[laco]
    index_holder_to_match_turmas = subjects.index(subject_to_have_new_prereq)
    if turmas[index_holder_to_match_turmas] == 1:
        newer_prereqs.append(new_prereqs[laco2-1])
        newer_prereqs.append(new_prereqs[laco2])
    else:
        x = 0
        turm = 65
        while (x < turmas[index_holder_to_match_turmas]):
            newer_prereqs.append(new_prereqs[laco2-1])
            newer_prereqs.append(new_prereqs[laco2]  + ' ' + chr(turm))
            turm = turm+1
            x = x+1
    laco2 = laco2 + 2





def scrambled(orig):
    dest = orig[:]
    random.shuffle(dest)
    return dest


#counters and variable for grades creation
a = 0
b = 0
newgradeline = []
grade = []

#cut is the min grade to be aproved
cut = 5

def new_simulation():
    print(chr(65))
    grade.clear()
    students.clear()
    params_sort = [x for x in params if not isinstance(x, str)]
    st_total = 0
    st = 3
    while(st < len(params)):
        total = params[st]
        st_total = st_total + total
        st = st + 4
    #creating students and grades
#counter for students ids creation
    i = 0
    j = 2 

    while(i < st_total):
        newstudent = random.randint(100000,199999)
        #excluding duplicates
        if newstudent not in students:
            students.append(newstudent)
            i = i+1    
    #now grades
    while(j<len(params_sort)):
        a = 0
        while(a < params_sort[j]):
            b = 0
            newgradeline = []
            grade.append(newgradeline)
            while(b < len(subjects_with_turmas)):
                
                gen_grade = round(random.uniform(params_sort[j-2],params_sort[j-1]),2)
                newgradeline.append(gen_grade)
                b = b +1
            a = a +1
        j = j + 3  

    
    k = 0
    l = 0
    m = 0
    ## applying prereqs
    #discovering which subject is prereq for which subject
    print(grade[15][1])
    grade[15][1] = 0
#checking for repeated turmas and 0 all
    k = 0
    x = 0
    j = 65




        


# In[4]:
#generating table
    #grade[0][1]=None

    print(subjects_with_turmas)
    print(new_prereqs)
    simulation = pd.DataFrame (scrambled(grade),index=students, columns=subjects_with_turmas)

    try:
        f = open("test.csv")
        os.remove("test.csv")
    except IOError:
        simulation.to_csv(r'test.csv')
        simulation.to_html(r'test.html')
        print(grade)
    finally:
        f.close()
        simulation.to_csv(r'test.csv')
        simulation.to_html(r'test.html')
        #print(grade)
        #print(grade[0][0])



while(menu_keep == 0):
    cls()
    menu1 = input("Selecione uma opção: \n 1. Nova simulação \n 2. Configurar parametros\n 3. Configurar disciplinas \n 4. Exportar parâmetros\n 5. Importar parâmetros\n 6. Sair\n\nEntrada do usuário: ")
    if menu1 == '1':
        #os.remove("test.csv")   
        print('New simulation')
        new_simulation()
        try:
            input("Simulação exportada como test.csv. Pressione qualquer tecla para continuar.")
        except SyntaxError:
            menu_keep = menu_keep + 1
            pass
    elif menu1 == '2':
        cls()
        menu2 = input("1. Listar parametros atuais \n2. Configurar novos parametros\n3.Fazer upload de parametros\n4. Voltar\n\nEntrada do usuário: ")
        if menu2 == '1':
            p = 0
            q = 0
            while(p<len(params)/4):
                while(q < len(params)):
                    print("Parametro: " + str(params[q]))
                    q = q +1 
                    print("Mínimo: " + str(params[q]))
                    q = q +1
                    print("Máximo: " + str(params[q]))
                    q = q+1
                    print("Qtde de alunos: " + str(params[q])+"\n\n")
                    q = q+1    
                p = p + 1
            print("Disciplinas: ")
            print(subjects)
            try:
                input("Pressione qualquer tecla para continuar.")
            except SyntaxError:
                pass
        elif menu2 == '2':
            cls()
            param_to_config = input("1. Adicionar faixas\n2. Remover faixas\n3. Alterar faixas\n\nEntrada do usuário: ")
            if param_to_config == '1':
                p = 0
                q = 0
                while(p<len(params)/4):
                    while(q < len(params)):
                        print("Parametro: " + str(params[q]))
                        q = q +1 
                        print("Mínimo: " + str(params[q]))
                        q = q +1
                        print("Máximo: " + str(params[q]))
                        q = q+1
                        print("Qtde de alunos: " + str(params[q])+"\n\n")
                        q = q+1    
                    p = p + 1
                new_param_name = input("Insira o nome da nova faixa: ")
                if new_param_name not in params:
                    params.append(new_param_name)
                    new_param_min = int(input("Mínimo: "), 10)
                    params.append(new_param_min)
                    new_param_max = int(input("Máximo: "), 10)
                    params.append(new_param_max)
                    new_param_qtd = int(input("Qtde de Alunos: "), 10)
                    params.append(new_param_qtd)
                try:
                    input("Pressione qualquer tecla para continuar.")
                except SyntaxError:
                    pass
            elif param_to_config == '2':
                p = 0
                q = 0
                while(p<len(params)/4):
                    while(q < len(params)):
                        print("Parametro: " + str(params[q]))
                        q = q +1 
                        print("Mínimo: " + str(params[q]))
                        q = q +1
                        print("Máximo: " + str(params[q]))
                        q = q+1
                        print("Qtde de alunos: " + str(params[q])+"\n\n")
                        q = q+1    
                    p = p + 1
                removed_param_name = input("Insira o nome da faixa a ser removida.\n\nEntrada do usuário: ")
                rm_index = [i for i, x in enumerate(params) if x == str(removed_param_name)]
                print(rm_index[0])
                params.pop(rm_index[0]+3)
                params.pop(rm_index[0]+2)
                params.pop(rm_index[0]+1)
                params.pop(rm_index[0])
                try:
                    input("Pressione qualquer tecla para continuar.")
                except SyntaxError:
                    pass
            elif param_to_config == '3':
                p = 0
                q = 0
                while(p<len(params)/4):
                    while(q < len(params)):
                        print("Parametro: " + str(params[q]))
                        q = q +1 
                        print("Mínimo: " + str(params[q]))
                        q = q +1
                        print("Máximo: " + str(params[q]))
                        q = q+1
                        print("Qtde de alunos: " + str(params[q])+"\n\n")
                        q = q+1    
                    p = p + 1
                altered_param_name = input("Insira o nome da faixa a ser alterada: ")
                rm_index = [i for i, x in enumerate(params) if x == str(altered_param_name)]
                param_new_name = input("Parametro encontrado. \n\nInsira o novo nome para o parâmetro ou N para manter o nome.\n\nEntrada do usuário: ")
                if param_new_name != 'N' and param_new_name != 'n':
                    paramidex = rm_index[0]
                    params[paramidex] = param_new_name
                param_new_min = int(input("\n\nInsira a nova nota mínima para o parâmetro ou -1 para mante-la.\n\nEntrada do usuário: "),10)
                if param_new_min != '-1':
                    paramidex = rm_index[0]
                    params[paramidex + 1] = param_new_min
                param_new_max = int(input("\n\nInsira a nova nota máxima para o parâmetro ou -1 para mante-la.\n\nEntrada do usuário: "),10)
                if param_new_max != '-1':
                    paramidex = rm_index[0]
                    params[paramidex + 2] = param_new_max
                param_new_std = int(input("\n\nInsira a nova qtde de alunos para o parâmetro ou -1 para mante-la.\n\nEntrada do usuário: "),10)
                if param_new_std != '-1':
                    paramidex = rm_index[0]
                    params[paramidex + 3] = param_new_std
                try:
                    input("Parâmetro alterado com sucesso!")
                except SyntaxError:
                    pass  





    elif menu1 == '3':
        cls()
        menu2 = input("1. Listar disicplinas\n2. Adicionar disciplinas\n3. Remover disciplinas\n4. Listar Pré-Requisitos\n5. Adicionar Pré-Requisito\n6. Remover Pré-Requisito\n\nEntrada do usuário: ")
        if menu2 == '1':
            print("\n\nDisciplinas cadastradas:\n")
            print(subjects)
            try:
                input("Pressione qualquer tecla para continuar.")
            except SyntaxError:
                pass

        if menu2 == '2':
            subject_added = input("Insira o nome da disciplina à ser adicionada: ")
            if subject_added not in subjects:
                subjects.append(subject_added)
                print("Disciplina adicionada com sucesso.")
        if menu2 == '3':
            print("\n\nDisciplinas cadastradas:\n")
            print(subjects)
            subject_removed = input("\n\nInsira o nome da disciplina a ser removido: ")
            if subject_removed in subjects:
                subjects.remove(subject_removed)
                print("\n\nDisciplina removida com sucesso.")
            else:
                print("Erro. Disciplina não encontrada.")
            try:
                input("Pressione qualquer tecla para continuar.")
            except SyntaxError:
                pass
        if menu2 == '4':
            subject_to_remove_prereqs = input('Insira a disciplina á remover os pré-requisitos: ')

            first_occurrence = prereqs.index(subject_to_remove_prereqs)

            subject_occurrences = [ i for i in range(len(prereqs)) if prereqs[i] == subject_to_remove_prereqs and i%2 != 0]

            print(subject_occurrences)

            x = len(subject_occurrences)-1

            individual_prereqs = []

            while(x>-1):
                individual_prereqs.append(prereqs[subject_occurrences[x]-1])
                x = x -1

            print('requisitos para disciplina:')
            print(individual_prereqs)
            try:
                input("Pré-requisitos listados com sucesso. Pressione qualquer tecla para continuar.")
            except SyntaxError:
                pass

        if menu2 == '5':
            subject_to_add_prereq = input("Insira o nome da disciplina a qual deseja adicionar o Pré-Requisito: ")
            subject_new_prereq = input("Insira o nome da disciplina que será o Pré-Requisito: ")
            prereqs.append(subject_new_prereq)
            prereqs.append(subject_to_add_prereq)
            try:
                input("Pré-requisito adicionado com sucesso. Pressione qualquer tecla para continuar.")
            except SyntaxError:
                pass
        if menu2 == '6':

            #check for all occurrences
            #remove even occurrences
            #remove last occurrence -1
            #remove last occurrence
            #keep removing while there is an ocurrence not removed
            subject_to_remove_prereqs = input('Insira a disciplina á remover os pré-requisitos: ')
            subject_occurrences = [ i for i in range(len(prereqs)) if prereqs[i] == subject_to_remove_prereqs and i%2 != 0]
            x = len(subject_occurrences)-1
            while(x>-1):
                del prereqs[subject_occurrences[x]-1:subject_occurrences[x]+1]
                x = x -1
            print(prereqs)
            try:
                input("Requisito(s) para xxxx removidos. Pressione qualquer tecla para continuar.")
            except SyntaxError:
                pass   
    elif menu1 == '4':
        cls()
        params_sort = [x for x in params if not isinstance(x, str)]
        st_total = 0
        st = 3
        while(st < len(params)):
            total = params[st]
            st_total = st_total + total
            st = st + 4
        params_total = len(params)/4
        f = open('config.txt', 'w').close()
        f= open("config.txt","w+")
        f=open("config.txt", "a+")
        f.write("Qtde de alunos: %d" % st_total)
        f.write("\nQtde de faixas: %d" % params_total)
        f.write("\nDisciplinas: %s" % subjects)
        f.write("\nParâmetros: %s" % params)
        f.write("\nPré-requisitos %s" % prereqs)
        f.flush() 
        f.close()
        try:
            input("Parametros foram exportados como 'config.txt'. Pressione qualquer tecla para continuar.")
        except SyntaxError:
            pass    
    elif menu1 == '5':
        try:
            input("Adicione o arquivo de configuração 'custom_config.txt' e pressione qualquer tecla para continuar.")
        except SyntaxError:
            pass          
    elif menu1 == '6':
        menu_keep = menu_keep + 1