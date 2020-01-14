#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import os
from xml.dom import minidom
import xml.etree.ElementTree as ET


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



outra_turma = 'Fez em outra turma'


#Defining Subjects
subjects = ["EB101", "SI100", "SI120", "SI201", "SI250"]

turmas = [1,2,1,2,3]





students = []

prereqs = ['SI100', 'SI250']







def scrambled(orig):
    dest = orig[:]
    random.shuffle(dest)
    return dest

def getting_subjects_config_from_file():
    tree = ET.parse('config.xml')
    root = tree.getroot()
    parsed_subjects = []
    for config_param in root.findall('subjects'):
        for subject in config_param.findall('subject'):
            for id in subject.findall('id'):
                parsed_subjects.append(id.text)
    #for x in root[0]: # access each subject
        #parsed_subjects.append(x[0].text) # every x is an element. 0 refers to the first element.
    print(parsed_subjects)
    return parsed_subjects

def getting_turmas_config_from_file():
    tree = ET.parse('config.xml')
    root = tree.getroot()
    parsed_turmas = []
    for config_param in root.findall('subjects'):
        for subject in config_param.findall('subject'): # access each subject
            individual_qtde_turmas = subject.findall('classes_no')
            for x in individual_qtde_turmas:
                parsed_turmas.append(int(x.text))
    print(parsed_turmas)
    return parsed_turmas

def getting_prereqs_config_from_file():
    tree = ET.parse('config.xml')
    root = tree.getroot()
    parsed_prereqs = []
    for config_param in root.findall('subjects'):
        for subject in config_param.findall('subject'):
            individual_parsed_prereq = subject.findall('pre_reqs')
            individual_parsed_subject_id = subject.findall('id')
            for x in individual_parsed_prereq:
                    if x.text is not None:
                        #prereq to add is equal to pre_reqs tag's text inside the current subject being parsed
                        parsed_prereqs.append(x.text)
                        #subject[0].text is equal to subject id
                        parsed_prereqs.append(individual_parsed_subject_id[0].text)

        print(parsed_prereqs)

    #print(parsed_prereqs)
    return parsed_prereqs

def getting_params_config_from_file():
    tree = ET.parse('config.xml')
    root = tree.getroot()
    parsed_params = []
    for config_param in root.findall('parameters'):
        for parameter in config_param.findall('parameter'):
            individual_parameter_name = parameter.findall('parameter_name')
            parsed_params.append(individual_parameter_name[0].text)
            individual_parameter_min_grade = parameter.findall('min_grade')
            parsed_params.append(int(individual_parameter_min_grade[0].text))
            individual_parameter_max_grade = parameter.findall('max_grade')
            parsed_params.append(int(individual_parameter_max_grade[0].text))
            individual_parameter_qtde_alunos = parameter.findall('qtde')
            parsed_params.append(int(individual_parameter_qtde_alunos[0].text))
    print(parsed_params)
    return parsed_params





#counters and variable for grades creation
a = 0
b = 0
newgradeline = []
grade = []

#cut is the min grade to be aproved
cut = 5

def new_simulation():

    sub = 0
    turm = 0
    subjects_with_turmas = []

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
    c = 0
    ## applying turmas
    grade[15][1] = 0
    already_sorted = []
    l = 0
    c = 0
    turmas_sorteadas = []
    while(l<len(students)):
        c = 0
        already_sorted = []
        while(c<len(subjects_with_turmas)):
            index_to_match = subjects.index(subjects_with_turmas[c][:5])
            turmas_sorteadas = []
            if turmas[index_to_match]>1 and subjects[index_to_match] not in already_sorted:
                    j = 0
                    turmas_sorteadas = random.sample(range(0,turmas[index_to_match]),turmas[index_to_match]-1)
                    while(j<len(turmas_sorteadas)):
                        grade[l][c+turmas_sorteadas[j]] = outra_turma
                        j = j +1
                    already_sorted.append(subjects[index_to_match])
                    c = c +1
            else:
                c = c+1
        l = l+1

#applyin prereqs
#discovering which subject is prereq for which subject
    l = 0
    while(l < len(students)):
        to_be_checked_prereqs = []
        to_cancel_due_to_prereq =[]
        laco3 = 1
        while (laco3<len(prereqs)):
            for disciplina_com_prereq in subjects_with_turmas:
                if prereqs[laco3] in disciplina_com_prereq:
                    current_prereqs_on_table = []
                    #print("Disciplina tem pre-req, vamos descobrir qual disciplina é:")
                    #print(prereqs[laco3-1])
                    #descobrindo atraves de iteracão quais índices de prereqs
                    print('descobrindo to_be_checked_prereqs: ')
                    to_be_checked_prereqs = [i for i in range(len(subjects_with_turmas)) if prereqs[laco3-1] in subjects_with_turmas[i]]
                    print(to_be_checked_prereqs)
                    #armazenando disciplinas que teriam que ser anuladas caso prereqs não sejam atendidos
                    print('descobrindo to_cancel_due_to_prereq: ')
                    to_cancel_due_to_prereq = [i for i in range(len(subjects_with_turmas)) if prereqs[laco3] in subjects_with_turmas[i]]
                    print(to_cancel_due_to_prereq)

                    #iteration to set 'Faltam prereqs' on subjects that have only 'Faltam prereqs' on its prereqs grades
                    i = 0
                        #it will alert if there are only texts in the array
                    is_there_int=0
                    for i in to_be_checked_prereqs:
                        if isinstance(grade[l][i], str) == False:
                            is_there_int = 1
                    if is_there_int == 0:
                        for x in to_cancel_due_to_prereq:
                            grade[l][x] = 'Faltam prereqs 2'

                    #identifyin indexes of possible pre-requisites with its turmas on the table
                    i = 0
                    while(i<len(to_be_checked_prereqs)):
                        if isinstance(grade[l][to_be_checked_prereqs[i]], str) == False and grade[l][to_be_checked_prereqs[i]] < cut:
                            sera_cancelado = 0
                            while(sera_cancelado<len(to_cancel_due_to_prereq)):
                                grade[l][to_cancel_due_to_prereq[sera_cancelado]] = 'Faltam prereqs'
                                sera_cancelado = sera_cancelado + 1
                            #print('achamos algo')
                            #adicionar logica que se houverem x(qtde de materias com turmas de prereq) em texto, alterar nota para faltam prereqs
                        #if isinstance(grade[l][to_be_checked_prereqs[i]], str) == False
                        i = i + 1
            laco3 = laco3 +2
        l = l+1
    print(to_be_checked_prereqs)
# In[4]:
#generating table
    #grade[0][1]=None

    print(subjects_with_turmas)
    print(prereqs)
    simulation = pd.DataFrame (scrambled(grade),index=students, columns=subjects_with_turmas)

    try:
        f = open("simulacao.csv")
        os.remove("simulacao.csv")
    except IOError:
        simulation.to_csv(r'simulacao.csv')
        simulation.to_html(r'simulacao.html')
        print(grade)
    finally:
        f.close()
        simulation.to_csv(r'simulacao.csv')
        simulation.to_html(r'simulacao.html')
        #print(grade)
        #print(grade[0][0])


#TODO: PREVENT USER INPUT ERRORS TO ALL ITEMS
while(menu_keep == 0):
    cls()
    menu1 = input("Selecione uma opção: \n 1. Nova simulação \n 2. Configurar parametros\n 3. Configurar disciplinas \n 4. Importar parâmetros\n 5. Sair\n\nEntrada do usuário: ")
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
                if param_new_min != -1:
                    paramidex = rm_index[0]
                    params[paramidex + 1] = param_new_min
                param_new_max = int(input("\n\nInsira a nova nota máxima para o parâmetro ou -1 para mante-la.\n\nEntrada do usuário: "),10)
                if param_new_max != -1:
                    paramidex = rm_index[0]
                    params[paramidex + 2] = param_new_max
                param_new_std = int(input("\n\nInsira a nova qtde de alunos para o parâmetro ou -1 para mante-la.\n\nEntrada do usuário: "),10)
                if param_new_std != -1:
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
                qtde_turmas = int(input("Insira a qtde de turmas para esta disciplina"))
                turmas.append(qtde_turmas)
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
            subject_to_remove_prereqs = input('Insira a disciplina á listar os pré-requisitos: ')

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
        try:
            subjects = getting_subjects_config_from_file()
            turmas = getting_turmas_config_from_file()
            prereqs = getting_prereqs_config_from_file()
            params = getting_params_config_from_file()
            input("Adicione o arquivo de configuração 'custom_config.txt' e pressione qualquer tecla para continuar.")
        except SyntaxError:
            pass
    elif menu1 == '5':
        menu_keep = menu_keep + 1
