import os
#######INPUT ERROR HANDLING

####Especial error types:
class Error(Exception):
    pass

#option not available
class NotInScope(Error):
    pass

#grade input impossible (x<0 or x>10)
class NotPossibleGrade(Error):
    pass

#maxgrade < mingrade
class InvalidMaxGrade(Error):
    pass

class DuplicateParameter(Error):
    pass

class InvalidParameter(Error):
    pass

class InvalidSubjectCode(Error):
    pass


####Check for error functions:
def edit_turmas(subjects, turmas):
    try:
        subject_to_edit_turmas = input("\n Insira o código da disciplina à alterar as turmas ou ENTER para cancelar.\nEntrada do usuário: ")
        if subject_to_edit_turmas is not '':
            if subject_to_edit_turmas in subjects:
                index_to_edit_turmas = subjects.index(subject_to_edit_turmas)
                new_turmas_qtt = int(input("\n Insira a nova quantidade de turmas para a disciplina: "))
                turmas[index_to_edit_turmas] = new_turmas_qtt
                print("Quantidade de turmas alterada com sucesso. Nova quantidade de turmas para "+str(subject_to_edit_turmas)+": "+str(turmas[index_to_edit_turmas]))
            else:
                print("Disciplina não encontrada.")
    except ValueError:
        print("Valor inválido. Operação cancelada.")
    return subjects, turmas

def del_subject(subjects, turmas):
    try:
        subject_removed = input("\nInsira o código da disciplina a ser removida ou ENTER para cancelar.\nEntrada do usuário: ")
        if subject_removed is not '':
            if subject_removed in subjects:
                subject_index = subjects.index(subject_removed)
                turmas.pop(subject_index)
                subjects.remove(subject_removed)
                print("\n\nDisciplina removida com sucesso.")
            else:
                print("Erro. Disciplina não encontrada.")
        else:
            cls()
            print("Operação cancelada.")
    except ValueError:
        print("Operação inválida.")
    return subjects, turmas

def set_new_subject(subjects, turmas):
    try:
        new_subject = input("O código da disciplina deve seguir o seguinte padrão. ABXXX sendo AB duas letras quaisquer e XXX 3 números quaisquer. \nInsira o código da disciplina à ser adicionada ou Enter para cancelar.\nEntrada do usuário: ")
        if len(new_subject) != 5:
            raise InvalidSubjectCode
        new_subject = new_subject.upper()
        print(new_subject)
        int(new_subject[-3:])
        if new_subject not in subjects and new_subject is not '':
            no_turmas = int(input("Insira a quantidade de turmas para esta disciplina. \nEntrada do usuário: "))
            subjects.append(new_subject)
            turmas.append(abs(no_turmas))
            print("Disciplina adicionada com sucesso.")
        elif new_subject in subjects:
            print("Disciplina já cadastrada.")
    except ValueError:
        print("Valor inválido. Operação cancelada.")
    except InvalidSubjectCode:
        print("Código de disciplina inválido. Operação cancelada.")
    return subjects, turmas

def set_new_parameter(params):
    try:
        new_param_name = input("Insira o nome do novo parâmetro ou ENTER para cancelar.\n\n Entrada do usuário: ")
        if new_param_name not in params and new_param_name is not '':
            new_param_min = input("Nota mínima: ")
            float(new_param_min)
            new_param_max = input("Nota máxima: ")
            float(new_param_max)
            new_param_qtd = input("Qtde de alunos: ")
            int(new_param_qtd)
            params.append(new_param_name)
            params.append(float(new_param_min))
            params.append(float(new_param_max))
            params.append(int(new_param_qtd))
            print("Parametros foram adicionados.\n")
            print(params)
        elif new_param_name in params:
            raise DuplicateParameter
        else:
            cls()
            print("Operação cancelada")
    except DuplicateParameter:
        cls()
        print("Este parâmetro já existe")
    except ValueError:
        cls()
        print("Valor inserido inválido")
    return params

def del_parameter(params):
    try:
        removed_param_name = input("Insira o nome do parâmetro à ser removido ou enter para cancelar.\n\nEntrada do Usuário: ")
        if removed_param_name not in params and removed_param_name is not '':
            raise InvalidParameter
        elif removed_param_name is '':
            print("Operação cancelada.")
        elif removed_param_name in params:
            rm_index = [i for i, x in enumerate(params) if x == str(removed_param_name)]
            print(rm_index[0])
            params.pop(rm_index[0]+3)
            params.pop(rm_index[0]+2)
            params.pop(rm_index[0]+1)
            params.pop(rm_index[0])
            cls()
            print("Parâmetro removido com sucesso.")
    except InvalidParameter:
        cls()
        print("Parâmetro não existe.")
    return params

def change_parameter(params):
    try:
        altered_param_name = input("Insira o nome do parâmetro à ser alterado ou enter para cancelar. \n\nEntrada do usuário: ")
        if altered_param_name not in params and altered_param_name is not '':
            raise InvalidParameter
        elif altered_param_name is '':
            print("Operação cancelada.")
        elif altered_param_name in params:
            cls()
            print("Parâmetro encontrado.")
            rm_index = [i for i, x in enumerate(params) if x == str(altered_param_name)]
            paramindex = rm_index[0]
            param_new_name = input("Insira o novo nome para o parâmetro ou ENTER para manter o nome.\nEntrada do usuário: ")
            param_new_min = input("Insira a nova nota mínima para o parâmetro ou -1 para mantê-la.\nEntrada do usuário: ")
            float(param_new_min)
            param_new_max = input("Insira a nova nota máxima para o parâmetro ou -1 para mantê-la.\nEntrada do usuário: ")
            float(param_new_max)
            param_new_std = input("Insira a nova quantidade de alunos para o parâmetro ou -1 para mantê-la.\nEntrada do usuário: ")
            int(param_new_std)
            ## gravando alterações
            if param_new_name is not '':
                params[paramindex] = param_new_name
            if float(param_new_min) != -1.0:
                params[paramindex+1] = float(param_new_min)
            if float(param_new_max) != -1.0:
                params[paramindex+2] = float(param_new_max)
            if int(param_new_std) != -1:
                params[paramindex+3] = int(param_new_std)
    except ValueError:
        print("Valor inválido. Operação cancelada.")
    except InvalidParameter:
        print("Parâmetro não existe.")
    return params



def check_input_in_scope (a,b,user_input):
    try:
        menu_input = int(user_input)
        if menu_input < a or menu_input > b:
            raise NotInScope
    except NotInScope:
        new_param_checklist = 1
        print("Insira uma opção válida")
        ask_for_input_to_Continue()
    except ValueError:
        new_param_checklist = 1
        print("Insira uma opção válida")
        ask_for_input_to_Continue()
    return
########

#check for int between params
def check_for_int(a):
    try:
        menu_input = int(a)
    except ValueError:
        new_param_checklist = 1
        print("Insira uma opção válida!")
    return


def ask_for_input_to_Continue():
    try:
        input("Pressione qualquer tecla para continuar.")
    except SyntaxError:
        pass
    return


def cls():
    os.system('cls' if os.name=='nt' else 'clear')
