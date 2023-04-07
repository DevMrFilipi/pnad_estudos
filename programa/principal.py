import xlrd
from modelo import Variavel


def extrair_variaveis(dicionario):
    planilha = xlrd.open_workbook(dicionario)
    primeira_aba = planilha.sheet_by_index(0)

    variaveis = []
    nova_variavel = None

    for idx, linha in enumerate(primeira_aba.get_rows()):
        primeira_celula = linha[0]
        if primeira_celula.ctype == 2:
            if nova_variavel:
                variaveis.append(nova_variavel)

            posicao_inicial = linha[0].value
            tamanho = linha[1].value
            codigo = linha[2].value
            descricao = linha[4].value
            nova_variavel = Variavel(posicao_inicial, tamanho, codigo, descricao)

            categoria_tipo = int(linha[5].value) if linha[5].ctype == 2 else linha[5].value
            categoria_descricao_tipo = int(linha[6].value) if linha[6].ctype == 2 else linha[6].value
            nova_variavel.add_categoria(
                {'categoria_tipo': categoria_tipo, 'categoria_descricao_tipo': categoria_descricao_tipo})
        else:
            if nova_variavel:
                if primeira_celula.ctype == 0:
                    categoria_tipo = int(linha[5].value) if linha[5].ctype == 2 else linha[5].value
                    categoria_descricao_tipo = int(linha[6].value) if linha[6].ctype == 2 else linha[6].value
                    nova_variavel.add_categoria(
                        {'categoria_tipo': categoria_tipo, 'categoria_descricao_tipo': categoria_descricao_tipo})

        #if idx > 50:
            #break
    return variaveis
