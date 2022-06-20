import json


def abre_arquivo(nome_arquivo):
    while True:
        try:
            with open(nome_arquivo) as file:
                file = json.load(file)
        except FileNotFoundError:
            print('O arquivo não foi encontrado.')
            break
        else:
            print('Arquivo encontrado')
            return file


def retira_dias_sem_faturamento(arquivo):
    nova_lista = [elemento for elemento in arquivo if elemento['valor'] != 0]
    return nova_lista


def menor_faturamento(arquivo):
    menor_valor_faturamento = arquivo[0]['valor']
    dia_menor_faturamento = arquivo[0]['dia']

    for elemento in arquivo:
        if elemento['valor'] < menor_valor_faturamento:
            menor_valor_faturamento = elemento['valor']
            dia_menor_faturamento = elemento['dia']

    return [dia_menor_faturamento, menor_valor_faturamento]


def maior_faturamento(arquivo):
    maior_valor_faturamento = arquivo[0]['valor']
    dia_maior_faturamento = arquivo[0]['dia']

    for elemento in arquivo:
        if elemento['valor'] > maior_valor_faturamento:
            maior_valor_faturamento = elemento['valor']
            dia_maior_faturamento = elemento['dia']

    return [dia_maior_faturamento, maior_valor_faturamento]


def media_faturamento(arquivo):
    soma = 0
    contador_dia_faturamento = len(arquivo)
    for elemento in arquivo:
        soma += elemento['valor']
    media = soma / contador_dia_faturamento
    return confere_dias_media(media, arquivo)


def confere_dias_media(media, arquivo):
    contador_dias_acima_media = 0
    for elemento in arquivo:
        if elemento['valor'] > media:
            contador_dias_acima_media += 1
    return [media, contador_dias_acima_media]


path_arquivo = 'dados.json'
arquivo_faturamento = abre_arquivo(path_arquivo)
lista_exclui_dias_sem_faturamento = retira_dias_sem_faturamento(arquivo_faturamento)

dia_valor_menor_faturamento = menor_faturamento(lista_exclui_dias_sem_faturamento)
dia_valor_maior_faturamento = maior_faturamento(lista_exclui_dias_sem_faturamento)
media_mensal = media_faturamento(lista_exclui_dias_sem_faturamento)

print(f'O dia de menor faturamento foi o dia {dia_valor_menor_faturamento[0]},'
      f' com faturamento de R$ {dia_valor_menor_faturamento[1]:.2f}')
print(f'O dia de maior faturamento foi o dia {dia_valor_maior_faturamento[0]},'
      f' com faturamento de R$ {dia_valor_maior_faturamento[1]:.2f}')
print(f'A média mensal foi de R$ {media_mensal[0]:.2f},'
      f' e {media_mensal[1]} dias tiveram faturamento maior que a média mensal.')
