def inverte_string(string):
    string_invertida = ''
    for letra in range(len(string), 0, -1):
        string_invertida += (string[letra - 1])
    print(string_invertida)


inverte_string(input('Digite a palavra ou frase que você quer que seja invertida: '))
