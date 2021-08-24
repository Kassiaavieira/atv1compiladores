
def verify_data(data):
    dia, mes, ano = map(int, data.split('/'))
    if mes < 1 or mes > 12 or ano <= 0:
        return False

    if mes in (1, 3, 5, 7, 8, 10, 12):
        ultimo_dia = 31
    elif mes == 2:
        if (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0):
            ultimo_dia = 29
        else:
            ultimo_dia = 28
    else:
        ultimo_dia = 30
    #verifica se o dia é válido
    if dia < 1 or dia > ultimo_dia:
        return False

    return True

print(verify_data("00/00/0000"))