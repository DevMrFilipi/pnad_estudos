import xlrd

from programa.modelo import Variavel

planilha = xlrd.open_workbook("dados/dicionario_pessoas.xls")
primeira_aba = planilha.sheet_by_index(0)

variaveis = []
nova_variavel = None

for idx, linha in enumerate(primeira_aba.get_rows()):
    print(linha)
    primeira_aba = linha[0]
    if primeira_aba.ctype == 2:
        if nova_variavel:
            variaveis.append(nova_variavel)

        posicao_inicial = linha[0].value
        tamanho = linha[1].value
        codigo = linha[2].value
        descricao = linha[4].value
        nova_variavel = Variavel(posicao_inicial, tamanho, codigo, descricao)

        categoria_tipo = linha[5]
        categoria_descricao_tipo = linha[6].value
        nova_variavel.add_categoria(
            {'categoria_tipo': categoria_tipo, 'categoria_tipo_descricao': categoria_descricao_tipo})
    else:
        if nova_variavel:
            categoria_tipo = linha[5].value
            categoria_descricao_tipo = linha[6].value
            nova_variavel.add_categoria(
                {'categoria_tipo': categoria_tipo, 'categoria_tipo_descricao': categoria_descricao_tipo})

    #if idx > 50:
        #break
print('Total de variaveis: ', len(variaveis))
for variavel in variaveis:
    print(variavel)
    for categ in variavel.categoria:
        print('\t', categ)