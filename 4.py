def valor_total_faturamento(arquivo):
    total = 0
    for k, v in faturamento_mensal_estado.items():
        total += v
    return dividindo_por_uf(total)


def dividindo_por_uf(valor):
    faturamento_porcentual_estado = {}
    for k, v in faturamento_mensal_estado.items():
        porcentagem = (v / valor) * 100
        faturamento_porcentual_estado.update({k: porcentagem})
    return faturamento_porcentual_estado


def imprime_valores(arquivo):
    for k, v in arquivo.items():
        if k != 'Outros':
            print(f'O estado {k} representa {v:.2f} % do faturamento mensal.')
        else:
            print(f'Os {k} estados representam {v:.2f} % do faturamento mensal.')


faturamento_mensal_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

valores_porcentagem = valor_total_faturamento(faturamento_mensal_estado)
imprime_valores(valores_porcentagem)
