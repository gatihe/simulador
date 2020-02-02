try:
    new_param_name = input("Insira o nome do novo parâmetro: ")
    if new_param_name in params:
        raise
    min_grade = input("salve: ")
    float(min_grade)
    print("foi")
    print(teste)
except ValueError:
    print("não deu")
