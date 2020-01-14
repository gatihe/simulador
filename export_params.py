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
