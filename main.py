#email = 'abc.def@mail.c'
#email = 'abc.def@mail'
#email = 'abc-@mail.com'
#email = 'abc_def@mail.com' #tem q acc
#email = 'abc.def@mail-archive.com'  # tem q acc

# verifica email
#props serve p limitar a quantidade de parâmetros de função
def veriricar_email(email):
    dicionario = {
        "prefixo": {
            "modo": True,
            "validado": False,
        },
        "dominio": {
            "modo": False,
            "validado": False,
        },
        "caractere_unico": {
            "char": '@',
            "foi_encontrado": False,
        },
        "caractere_especial": ['@', '.', '-', '_'],
        "caractere_anterior": email[0],
        "caractere_atual": email[0],
        "caractere_inicial": email[0],
        "caractere_final": email[-1],
    }

    def verifica_caractere_valido(dicionario):
        caractere_atual = dicionario["caractere_atual"]

        caractere_anterior = dicionario["caractere_anterior"]

        caractere_especial = dicionario["caractere_especial"]

        caractere_inicial = dicionario["caractere_inicial"]

        caractere_final = dicionario["caractere_final"]

        caractere_inicial_e_especial = caractere_inicial in caractere_especial

        caractere_final_e_especial = caractere_final in caractere_especial

        caractere_e_especial = caractere_atual in caractere_especial

        caractere_anterior_e_especial = caractere_anterior in caractere_especial

        caractere_e_alfanumerico = caractere_atual.isalnum()

        caractere_e_valido = (caractere_e_alfanumerico or caractere_e_especial)

        sequencia_invalida = (caractere_anterior_e_especial and caractere_e_especial)

        caractere_e_invalido = not caractere_e_valido

        string_e_invalida = (caractere_e_valido and sequencia_invalida)

        aviso_caractere_e_invalida = f"Character {caractere_atual} é invalida"

        aviso_string_e_invalida = f"String é invalida: {caractere_anterior}{caractere_atual}"

        if caractere_inicial_e_especial:
            return False

        if caractere_final_e_especial:
            return False

        if caractere_e_invalido:
            print(aviso_caractere_e_invalida)
            return False

        if string_e_invalida:
            print(aviso_string_e_invalida)
            return False

        return True

    for caractere_atual in list(email):
        dicionario["caractere_atual"] = caractere_atual

        caractere_valido = verifica_caractere_valido(dicionario)

        caractere_invalido = not caractere_valido

        prefixo = dicionario["prefixo"]["modo"]

        dominio = dicionario["dominio"]["modo"]

        caractere_unico = dicionario["caractere_unico"]["char"]

        caractere_unico_foi_encontrado = dicionario["caractere_unico"]["foi_encontrado"]

        caractere_e_unico = (caractere_unico == caractere_atual)

        aviso_caractere_existente = f"Caractere existente: {caractere_unico}"

        if prefixo and caractere_invalido:
            return False, dicionario

        if caractere_e_unico and caractere_unico_foi_encontrado:
            print(aviso_caractere_existente)
            return False, dicionario

        if caractere_e_unico:
            dicionario["prefixo"]["modo"] = False

            dicionario["prefixo"]["validado"] = True

            dicionario["dominio"]["modo"] = True

            dicionario["caractere_unico"]["foi_encontrado"] = True

        if dominio and caractere_invalido:
            return False, dicionario

        dicionario["caractere_anterior"] = caractere_atual

    dicionario["dominio"]["validado"] = True
    return True, dicionario



email = "abc_def@mail.com"
print(veriricar_email(email))



