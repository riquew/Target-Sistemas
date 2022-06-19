def cria_lista(tamanho):
    lista = tamanho * [0]
    lista[1] = 1
    c = 1
    while c < (tamanho - 1):
        soma = lista[c] + lista[c - 1]
        lista[c + 1] = soma
        c += 1
    return lista


def confere_input(numero_conferir):
    while True:
        try:
            numero_conferir = int(input(numero_conferir))
        except ValueError:
            print('Ocorreu um erro de tipo, você deve digitar um número inteiro.')
        else:
            return numero_conferir


tamanho_inicial = 100
sequencia_fibonacci = cria_lista(tamanho_inicial)

numero_aprovado = confere_input('Digite o número que você deseja saber se faz parte da sequência de Fibonacci: ')

while numero_aprovado > sequencia_fibonacci[-1]:
    print(f'O número digitado {numero_aprovado} é maior que o último '
          f'número da sequência inicial. Aumentando o tamanho da lista')
    tamanho_inicial += 50
    sequencia_fibonacci = cria_lista(tamanho_inicial)

if numero_aprovado in sequencia_fibonacci:
    print(f'O número {numero_aprovado} faz parte da sequência de Fibonacci.')
else:
    print(f'O número {numero_aprovado} não faz parte da sequência de Fibonacci.')
