def string_to_int(texto):
    for caractere_atual in list(texto):
        if not caractere_atual.isnumeric():
            return False
    return True, int(texto)


# Versão 01
print(string_to_int("abc123"))
print(string_to_int("123"))
print(string_to_int("010"))


