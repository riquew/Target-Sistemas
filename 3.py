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


def maior_faturamento(arquivo):
    dia_maior_faturamento = max(arquivo, key=arquivo.get)
    return dia_maior_faturamento


def menor_faturamento(arquivo):
    dict_exclui_dias_sem_faturamento = {k: v for k, v in arquivo.items() if v != 0}
    dia_menor_faturamento = min(dict_exclui_dias_sem_faturamento, key=dict_exclui_dias_sem_faturamento.get)
    return dia_menor_faturamento


def media_faturamento(arquivo):
    soma = 0
    contador_dia_faturamento = 0
    for v in arquivo_faturamento.values():
        if v != 0:
            soma += v
            contador_dia_faturamento += 1
    media = soma / contador_dia_faturamento
    return confere_dias_media(media)


def confere_dias_media(media):
    contador_dias_acima_media = 0
    for v in arquivo_faturamento.values():
        if v > media:
            contador_dias_acima_media += 1
    return contador_dias_acima_media


path_arquivo = 'faturamentoMaio.json'
arquivo_faturamento = abre_arquivo(path_arquivo)
print(f'O menor faturamento foi no {menor_faturamento(arquivo_faturamento)} '
      f'com o valor de R$ {arquivo_faturamento[menor_faturamento(arquivo_faturamento)]}.')
print(f'O maior faturamento foi no {maior_faturamento(arquivo_faturamento)} '
      f'com o valor de R$ {arquivo_faturamento[maior_faturamento(arquivo_faturamento)]}.')
print(f'A quantidade de dias em que o valor de faturamento '
      f'diário foi superior à média mensal foi de {media_faturamento(arquivo_faturamento)} dias.')

