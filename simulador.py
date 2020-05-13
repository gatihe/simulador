import pandas as pd
import random
import os
import time
from xml.dom import minidom
import xml.etree.ElementTree as ET
from input_handling import *


# In[2]:


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#defining parameters
bast_param = [0,5] #ba prefix for below average student
avst_param = [5,7] #av prefix for average student
aast_param = [7,10] #aa prefix for above average student

semoffers = []
cat_info = []
hard_passes = []
easy_passes = []
#defining parameters 2
menu_keep = 0
params = ["Below Average", 0, 5, 10, "Average", 5, 7, 10, "Above Average", 7, 10, 10]
params_total = len(params)/4
factors = []



outra_turma = 'Fez em outra turma'


#Defining Subjects
subjects = ["EB101", "SI100", "SI120", "SI201", "SI250"]

turmas = [1,2,1,2,3]





students = []

prereqs = ["SI100", "SI250"]

def scrambled(orig):
    dest = orig[:]
    random.shuffle(dest)
    return dest

def getting_subjects_config_from_file(filename):
    parsed_subjects = []
    tree = ET.parse(filename)
    root = tree.getroot()
    parsed_subjects = []
    for config_param in root.findall('subjects'):
        for subject in config_param.findall('subject'):
            for id in subject.findall('id'):
                parsed_subjects.append(id.text)
    return parsed_subjects

def getting_catalog_info_from_file(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    parsed_cat_info = []
    for cat in root.findall('cat_info'):
        for course_id in cat.findall('course_id'):
            parsed_cat_info.append(int(course_id.text))
        for year in cat.findall('year'):
            parsed_cat_info.append(int(year.text))
        for max_years in cat.findall('max_years'):
            parsed_cat_info.append(int(max_years.text))
    return parsed_cat_info


def export_subjects(subjects,credits, cat_info):
    tpds = []
    j = 0
    while(j<len(subjects)):
        info_line = []
        tpds.append(info_line)
        info_line.append(subjects[j])
        info_line.append(cat_info[1])
        info_line.append(credits[j])
        info_line.append('N')
        j = j+1
    return tpds

    #for x in root[0]: # access each subject
        #parsed_subjects.append(x[0].text) # every x is an element. 0 refers to the first element.


def getting_turmas_config_from_file(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    parsed_turmas = []
    for config_param in root.findall('subjects'):
        for subject in config_param.findall('subject'): # access each subject
            individual_qtde_turmas = subject.findall('classes_no')
            for x in individual_qtde_turmas:
                parsed_turmas.append(int(x.text))
    return parsed_turmas

def getting_credits_config_from_file(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    parsed_credits = []
    for config_param in root.findall('subjects'):
        for subject in config_param.findall('subject'): # access each subject
            individual_qtde_credits = subject.findall('credits')
            for x in individual_qtde_credits:
                parsed_credits.append(int(x.text))
    return parsed_credits

def getting_semoffer_config_from_file(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    parsed_semoffers = []
    for config_param in root.findall('subjects'):
        for subject in config_param.findall('subject'): # access each subject
            individual_semoffer = subject.findall('sem_offer')
            for x in individual_semoffer:
                parsed_semoffers.append(int(x.text))
    return parsed_semoffers

def getting_prereqs_config_from_file(filename):
    tree = ET.parse(filename)
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
    #print(parsed_prereqs)
    return parsed_prereqs

def getting_hard_pass_from_file(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    parsed_hard_pass = []
    for config_param in root.findall('subj_dificulty'):
        for hp in config_param.findall('hard_pass'):
            individual_hp = hp.findall('sub_id')
            for x in individual_hp:
                    if x.text is not None:
                        #prereq to add is equal to pre_reqs tag's text inside the current subject being parsed
                        parsed_hard_pass.append(x.text)
    return parsed_hard_pass

def getting_easy_pass_from_file(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    parsed_easy_pass = []
    for config_param in root.findall('subj_dificulty'):
        for hp in config_param.findall('easy_pass'):
            individual_ep = hp.findall('sub_id')
            for x in individual_ep:
                    if x.text is not None:
                        #prereq to add is equal to pre_reqs tag's text inside the current subject being parsed
                        parsed_easy_pass.append(x.text)
    return parsed_easy_pass

def getting_params_config_from_file(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    parsed_params = []
    for config_param in root.findall('parameters'):
        for parameter in config_param.findall('parameter'):
            individual_parameter_name = parameter.findall('parameter_name')
            parsed_params.append(individual_parameter_name[0].text)
            individual_parameter_min_grade = parameter.findall('min_grade')
            parsed_params.append(float(individual_parameter_min_grade[0].text))
            individual_parameter_max_grade = parameter.findall('max_grade')
            parsed_params.append(float(individual_parameter_max_grade[0].text))
            individual_parameter_qtde_alunos = parameter.findall('qtde')
            parsed_params.append(int(individual_parameter_qtde_alunos[0].text))
    return parsed_params

def getting_factors_config_from_file(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    parsed_factors = []
    for config_factor in root.findall('factors'):
        easy_pass_factor = config_factor.findall('easy_pass_factor')
        parsed_factors.append(float(easy_pass_factor[0].text))
        hard_pass_factor = config_factor.findall('hard_pass_factor')
        parsed_factors.append(float(hard_pass_factor[0].text))
    return parsed_factors

def listar_parametros():
    p = 0
    q = 0
    print('Parâmetros configurados:\n')
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
    return

def listar_disciplinas():
    print("Disciplinas cadastradas:\n")
    for x in subjects:
        print(x)
    print("\n")
    return

def ask_for_input_to_Continue():
    try:
        input("Pressione qualquer tecla para continuar.")
    except SyntaxError:
        pass
    return

#counters and variable for grades creation
a = 0
b = 0
newgradeline = []
grade = []

#cut is the min grade to be aproved
cut = 5
even_semester = []
odd_semester = []

def check_for_prereq(subject_to_check, prereqs_list):
    cont1 = 0
    prereqs_for_subject = []
    while (cont1 < len(prereqs_list)):
        if prereqs_list[cont1] == subject_to_check and cont1 % 2 != 0:
            prereqs_for_subject.append(prereqs_list[cont1 - 1])
        cont1 = cont1 + 1
    return prereqs_for_subject

def arrange_semesters(subjects, semoffers, even_semester, odd_semester):
    i = 0
    j = 0
    even_semester.clear()
    odd_semester.clear()
    for i, j in zip(semoffers, subjects):
        if i % 2 == 0:
            even_semester.append(j)
        if i % 2 != 0:
            odd_semester.append(j)
    return


def sort_turmas(subjects, turmas):
    sub = 0
    run_turma = 0
    subs_with_turmas = []
    subs_with_turmas.clear()
    while (sub < len(subjects)):
        subs_with_turmas.append('Turma')
        subs_with_turmas.append(subjects[sub])
        subs_with_turmas.append('Freq')
        sub = sub +1
    return subs_with_turmas

def check_prereqs_are_ok(disciplinas, already_passed): #if 1 ok if 0 not ok
    counter = 0
    ok_or_not = 1
    while(counter<len(disciplinas)):
        if disciplinas[counter] not in already_passed:
            ok_or_not = 0
    return ok_or_not

def new_simulation():
    arrange_semesters(subjects, semoffers, even_semester, odd_semester)
    max_years = 6
#intercalando semestres pra criar grade de ofertas
    all_subs = []
    all_subs.clear()
    i = 0
    while (i < 6):
        for odd_sem in odd_semester:
            all_subs.append(odd_sem)
        for even_sem in even_semester:
            all_subs.append(even_sem)
        i = i+1
    #print(all_subs)
    subss = []
    subss.clear()
    subss = sort_turmas(all_subs, turmas)
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
            while(b < len(subss)):
                #gen_grade = round(random.uniform(params_sort[j-2],params_sort[j-1]),2)
                gen_grade = -1
                newgradeline.append(gen_grade)
                b = b +1
            a = a +1
        j = j + 3




    m = 0
    subj_credits = []
    subj_credits.clear()
    while(m<len(subjects)):
        subj_credits.append(subjects[m])
        subj_credits.append(credits[m])
        m = m+1

    k = 0
    l = 0
    c = 0

#emptying values and sorting turmas
    l = 0



    while(l < len(students)):
        c = 0
        while (c < len(subss)):
            if subss[c] in subjects:
                turminha = subjects.index(subss[c])
                sorteio_de_turma = 0
                turma_sorteada = random.randint(0,turmas[turminha]-1)
                turma_sorteada = turma_sorteada + 65
                grade[l][c-1] = chr(turma_sorteada)
            c = c + 1
        l = l+1

    #identificar o que é um semestre na linha, manter primeiros
    #applying prereqs
    l = 0
    c = 0
    creditos_do_semestre = 0
    max_creditos = 28
    grades_to_handle = []
    already_passed = []
    handled_grades = []
    pendentes = []
    qtde_de_disciplinas_semestre_par = len(even_semester)
    qtde_de_disciplinas_semestre_impar = len(odd_semester)
    qtde_itens_na_disciplina = 7 #nome, turma, nota, creditos, semestre de oferta, liberado
    creditos_atuais = 0
    semestre_atual = []
    tempo_max_integralizacao = 12
    line = []
    alldata = []
    vetordeteste = [1,5,10,1,0,6]
    outrovetordeteste = []
    tpds = []

    aui = 2
    while(aui < len(params_sort)):
        aue = 0
        while(aue<params_sort[aui]):
            outrovetordeteste.append(params_sort[aui-2])
            outrovetordeteste.append(params_sort[aui-1])
            aue = aue + 1
        aui = aui + 3

    contest = 0
    while(contest<len(outrovetordeteste)):
        l = 0
        while(l<len(students)):
            index_inicial_do_semestre = 0
            index_final_do_semestre = -1
            inicio_semestre = 0
            contador_de_semestre = 1
            line.clear()
            pendentes.clear()
            c = 1
            already_passed.clear()
            sc_index = 0
            grades_to_handle.clear()
            while(c<len(subss)):
                pendentes.append(subss[c]) #nome
                pendentes.append(grade[l][c-1]) #turma
                pendentes.append(grade[l][c]) #nota
                sc_index = subj_credits.index(subss[c]) ##creditos
                pendentes.append(subj_credits[sc_index+1]) ##creditos
                if subss[c] in even_semester:
                    pendentes.append(2) #semestre de oferta, 1 impar, 2 par
                else:
                    pendentes.append(1)
                pendentes.append(1) #liberado para fazer ou não: 0 não (setup inicial), 1 sim
                pendentes.append(-1) #freq
                c = c +3
            ####\/ \/ \/ \/ VETOR PARA CONFIGURAR TUDO ESTA CRIADO, MAGICA ACONTECE LOGO ABAIXO \/ \/ \/ \/ CONFIRA:
            ## TRATAR VETOR PENDENTES
            j = 0
            instancias_eb101 = [i for i,d in enumerate(pendentes) if d=='EB101']
            instancias_eb102 = [i for i,d in enumerate(pendentes) if d=='EB102']
            while(contador_de_semestre<=tempo_max_integralizacao):
                index_inicial_do_semestre = index_final_do_semestre + 1
                if contador_de_semestre % 2 == 0:
                    index_final_do_semestre = index_final_do_semestre + (qtde_de_disciplinas_semestre_par * qtde_itens_na_disciplina)
                if contador_de_semestre % 2 != 0:
                    index_final_do_semestre = index_final_do_semestre + (qtde_de_disciplinas_semestre_impar * qtde_itens_na_disciplina)

                #percorrer pendentes inclusas no semestre do contador do semestre
                inicio_semestre = index_inicial_do_semestre
                fim_semestre = index_final_do_semestre
                semestre_atual.clear()
                #dividindo ofertas por semestre
                while(inicio_semestre<=fim_semestre):
                    semestre_atual.append(pendentes[inicio_semestre])
                    inicio_semestre = inicio_semestre + 1
                #bloqueando disciplinas que faltam prereqs ou que o aluno ja foi aprovado
                cont_sub = 0
                #somente bloqueando as que já foram feitas
                while(cont_sub<len(semestre_atual)):
                    if semestre_atual[cont_sub] in already_passed:
                        semestre_atual[cont_sub + 5] = 0
                    cont_sub = cont_sub +7
                #somente bloquando as que tem prereq nao cumprido
                cont_sub = 0
                while(cont_sub<len(semestre_atual)):
                    individual_prereqs = check_for_prereq(semestre_atual[cont_sub], prereqs)
                    if (len(individual_prereqs)>0):
                        novo_contador = 0
                        while(novo_contador<len(individual_prereqs)):
                            if individual_prereqs[novo_contador] not in already_passed:
                                semestre_atual[cont_sub+5] = 0
                            novo_contador = novo_contador + 1
                    cont_sub = cont_sub + 7

                creditos_atuais = 0
                cont_sub = 0
                while(cont_sub<(len(semestre_atual))):
                    test_creditos = 0
                    freq_instance = 100
                    if creditos_atuais + semestre_atual[cont_sub+3] < max_creditos and semestre_atual[cont_sub+5] == 1:
                        creditos_atuais = creditos_atuais+semestre_atual[cont_sub+3]
                        #sorteando nota
                        # print('parametros agora:')
                        # print(outrovetordeteste[contest])
                        # print(outrovetordeteste[contest+1])
                        freq_instance = round(freq_instance - random.uniform(0,40),2)
                        semestre_atual[cont_sub+6] = freq_instance
                        semestre_atual[cont_sub+2] = round(random.uniform(outrovetordeteste[contest],outrovetordeteste[contest+1]),2)
                        if semestre_atual[cont_sub] in hard_passes:
                            semestre_atual[cont_sub+2] = round(semestre_atual[cont_sub+2] - random.uniform(0,factors[1]),2)
                            print('hardpass bro')
                        if semestre_atual[cont_sub] in easy_passes:
                            semestre_atual[cont_sub+2] = round(semestre_atual[cont_sub+2] + random.uniform(0,factors[1]),2)
                            print('easypass bro')
                        if freq_instance < 65:
                            semestre_atual[cont_sub+2] = 0
                        if semestre_atual[cont_sub+2] >= 5:
                            already_passed.append(semestre_atual[cont_sub])
                            semestre_atual[cont_sub+5] = 0
                    cont_sub = cont_sub + 7

                count_line = 0
                while (count_line<len(semestre_atual)):
                    line.append(semestre_atual[count_line + 1])
                    alldata.append(semestre_atual[count_line + 1])
                    line.append(semestre_atual[count_line + 2])
                    alldata.append(semestre_atual[count_line + 2])
                    line.append(semestre_atual[count_line+6])
                    count_line = count_line + 7

                contador_de_semestre = contador_de_semestre + 1
            ## PEGAR PENDENTES E DEVOLVER PRAS NOTAS NORMAIS
            l = l+1
        print(hard_passes)
        print(easy_passes)
        maluco = 0
        while(maluco<len(line)):
            tpds.append(line[maluco])
            maluco = maluco +1
        contest = contest + 2
    l = 0


    #tirando -1 e turmas sem ter feito materia
    jua = 1
    while(jua<len(tpds)):
        if tpds[jua] == -1:
            tpds[jua] = '--'
            tpds[jua-1] = '--'
        jua = jua + 1


    #repassando tudo
    position = 0
    lensub = len(subss)

    while (l < len(students)):
        grade[l] = tpds[position:position+len(subss)]
        position = position + lensub
        l = l+1


    simulation = pd.DataFrame (scrambled(grade),index=students, columns=subss)
    timestr = time.strftime('%Y%m%d-%H%M%S')
    simulationcsv = timestr+'.csv'
    simulationhtml = timestr+'.csv'
    try:
        f = open("simulacao.csv")
        os.remove("simulacao.csv")
    except IOError:
        f = open("simulacao.csv", "+w")
    finally:
        f.close()
        simulation.to_csv(r'simulacao.csv')
        simulation.to_html(r'simulacao.html')

#TODO: PREVENT USER INPUT ERRORS TO ALL ITEMS
while(menu_keep == 0):
    cls()
    menu1 = input("Selecione uma opção: \n 1. Nova simulação \n 2. Configurar parametros\n 3. Configurar disciplinas \n 4. Importar parâmetros\n 5. Importar configuracoes adicionais\n 6. Sair\n\nEntrada do usuário: ")
    check_input_in_scope(1,6,menu1)
    if menu1 == '1':
        cls()
        #os.remove("test.csv")
        new_simulation()
        try:
            input("Simulação exportada como 'simulacao.csv' e 'simulacao.html'. Pressione qualquer tecla para continuar.")
        except SyntaxError:
            menu_keep = menu_keep + 1
            pass
    #sessao para configuração de parametros
    elif menu1 == '2':
        cls()
        menu2 = input("1. Listar parametros atuais \n2. Configuração de parametros\n3. Fazer upload de parametros\n4. Voltar\n\nEntrada do usuário: ")
        check_input_in_scope(1,4,menu2)
        if menu2 == '1':
            cls()
            listar_parametros()
            ask_for_input_to_Continue()
        elif menu2 == '2':
            cls()
            param_to_config = input("1. Adicionar parâmetro\n2. Remover parâmetro\n3. Alterar parâmetro\n\nEntrada do usuário: ")
            check_input_in_scope(1,3,param_to_config)
            if param_to_config == '1':
                cls()
                listar_parametros()
                params = set_new_parameter(params)
                listar_parametros()
                ask_for_input_to_Continue()
            elif param_to_config == '2':
                cls()
                listar_parametros()
                params = del_parameter(params)
                listar_parametros()
                ask_for_input_to_Continue()
            elif param_to_config == '3':
                cls()
                listar_parametros()
                params = change_parameter(params)
                listar_parametros()
                ask_for_input_to_Continue()
        elif menu2 == '3':
             params = getting_params_config_from_file()
             print("\nImportação realizada com sucesso. Os parâmetros foram atualizados.")
             ask_for_input_to_Continue()
    elif menu1 == '3':
        cls()
        menu2 = input("1. Listar disicplinas\n2. Adicionar disciplinas\n3. Remover disciplinas\n4. Alterar turmas\n5. Listar Pré-Requisitos\n6. Adicionar Pré-Requisito\n7. Remover Pré-Requisito\n8. Exportar disciplinas \n9. Voltar\n\nEntrada do usuário: ")
        check_input_in_scope(1,9,menu2)
        if menu2 == '1':
            cls()
            listar_disciplinas()
            ask_for_input_to_Continue()
        if menu2 == '2':
            cls()
            subjects, turmas = set_new_subject(subjects, turmas)
            listar_disciplinas()
            ask_for_input_to_Continue()
        if menu2 == '3':
            cls()
            listar_disciplinas()
            subjects, turmas = del_subject(subjects, turmas)
            listar_disciplinas()
            ask_for_input_to_Continue()
        if menu2 == '4':
            cls()
            listar_disciplinas()
            subjects, turmas = edit_turmas(subjects, turmas)
            ask_for_input_to_Continue()
        if menu2 == '5':
            cls()
            listar_disciplinas()
            prereqs_to_list = list_prereqs(prereqs, subjects)
            ask_for_input_to_Continue()
        if menu2 == '6':
            cls()
            listar_disciplinas()
            prereqs = add_prereqs(subjects, prereqs)
            ask_for_input_to_Continue()
        if menu2 == '7':
            cls()
            #check for all occurrences
            #remove even occurrences
            #remove last occurrence -1
            #remove last occurrence
            #keep removing while there is an ocurrence not removed
            subject_to_remove_prereqs = input('Insira a disciplina á remover os pré-requisitos ou ENTER para cancelar.\nEntrada do usuário: ')
            if subject_to_remove_prereqs   is not '':
                subject_occurrences = [ i for i in range(len(prereqs)) if prereqs[i] == subject_to_remove_prereqs and i%2 != 0]
                x = len(subject_occurrences)-1
                while(x>-1):
                    del prereqs[subject_occurrences[x]-1:subject_occurrences[x]+1]
                    x = x -1
                print("Requisito(s) para "+subject_to_remove_prereqs+" removidos.")
            else:
                cls()
                print("Operação cancelada.")
            ask_for_input_to_Continue()
        if menu2 == '8':
            opa = export_subjects(subjects,credits, cat_info)
            cls()
            print("Disciplinas exportadas como 'export_disciplinas.csv'.")
            ask_for_input_to_Continue()
            export = pd.DataFrame (opa,index=subjects, columns=['DISCIPLINA','ANO_CATALOGO', 'CREDITOS', 'FORMA_APROVACAO'])
            try:
              f = open("export_disciplinas.csv")
              os.remove("export_disciplinas.csv")
            except IOError:
              f = open("export_disciplinas.csv", "+w")
            finally:
              f.close()
              export.to_csv(r'export_disciplinas.csv', index=False)
              export.to_html(r'export_disciplinas.html')
    elif menu1 == '4':
        cls()
        filename = input("Insira o nome do arquivo XML à importar catalogo ou ENTER para cancelar.\nEntrada do usuário: ")
        if filename is not '':
            try:
                f=open(filename)
                subjects = getting_subjects_config_from_file(filename)
                turmas = getting_turmas_config_from_file(filename)
                prereqs = getting_prereqs_config_from_file(filename)
                params = getting_params_config_from_file(filename)
                semoffers = getting_semoffer_config_from_file(filename)
                credits = getting_credits_config_from_file(filename)
                cat_info = getting_catalog_info_from_file(filename)
                cls()
            except SyntaxError:
                print("\nProblema identificado ao importar. Verifique seu arquivo "+filename+".")
                pass
            except IOError:
                print("\nProblema identificado ao importar. Verifique seu arquivo "+filename+".")
                pass

        else:
            cls()
            print("Operação cancelada.")
        ask_for_input_to_Continue()
    elif menu1 == '5':
        cls()
        filename1 = input("Insira o nome do arquivo XML à importar configurações adicionais ou ENTER para cancelar.\nEntrada do usuário: ")
        if filename1 is not '':
            try:
                f=open(filename1)
                params = getting_params_config_from_file(filename1)
                factors = getting_factors_config_from_file(filename1)
                hard_passes = getting_hard_pass_from_file(filename1)
                easy_passes = getting_easy_pass_from_file(filename1)

                cls()
            except SyntaxError:
                print("\nProblema identificado ao importar. Verifique seu arquivo "+filename+".")
                pass
            except IOError:
                print("\nProblema identificado ao importar. Verifique seu arquivo "+filename+".")
                pass

        else:
            cls()
            print("Operação cancelada.")
        ask_for_input_to_Continue()
    elif menu1 == '6':
        menu_keep = menu_keep + 1
