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


####Check for error functions:
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
