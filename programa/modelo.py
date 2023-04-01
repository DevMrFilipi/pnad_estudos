class Variavel:

    def __init__(self, posicao_inicial, tamanho, codigo, descricao):    #crio o método da class Variavel que irá
        self.posicao_inicial = posicao_inicial                          #estruturar os dados de acordo com cada
        self.tamanho = tamanho                                          #atributo neste passado.
        self.codigo = codigo
        self.descricao = descricao
        self.categoria = []                                             #Este é o objeto lista categoria que iremos utilizar para datar nossas últimas células

    def add_categoria(self, categoria):         #Definimos um método para adicionar esta categoria.
        self.categoria.append(categoria)

    def __str__(self):              #Definimos um método string que irá organizar as duas subcategorias de categoria.
        return self.codigo + " - " + self.descricao