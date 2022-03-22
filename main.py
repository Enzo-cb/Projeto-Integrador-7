lexemas = []
tokens=[]
ct=1
lista_f = []
id = 1
operadores = ['+','*','=']
isalpha = []
while True:
    entrada = str(input('DIGITE UM LEXEMA'))
    lista = list(entrada)
    print(lista)
    for i in lista:
        if i == ' ':
            lista.remove(i)
        else:
            continue
    print(lista)

    for i in lista:
        if i.isalpha() == True and i not in isalpha:
            lista_f.append(f'<id,{ct}>')
            ct += 1
            isalpha.append(i)
        elif i.isdigit() == True:
            lista_f.append(f'<{i}>')
        elif i.isascii() == True and i in operadores:
           lista_f.append(f'<{i}>')
        elif i in isalpha:
            lista_f.append()
        else:
            lista_f.append('<erro>')
    break
for i in lista_f:
    print(i, end='')