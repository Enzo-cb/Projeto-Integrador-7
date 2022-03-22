lexemas = []
tokens=[]
ct=1
lista_f = []
id = 1
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
        if i.isalpha() == True:
            lista_f.append(f'<id,{ct}>')
            ct += 1
        elif i.isdigit() == True:
            lista_f.append(f'{i}')
        elif i.isascii() == True:
           lista_f.append(f'<{i}>')
        elif i.isspace() == True:
            pass
        else:
            print('<erro>')
    break
for i in lista_f:
    print(i, end='')
