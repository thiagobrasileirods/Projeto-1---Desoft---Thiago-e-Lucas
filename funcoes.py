def define_posicoes(linha, coluna, orientacao, tamanho):
    grid = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
  ]
    #o objetivo é, ao saber se e horizontal, a linha pe contante mas a coluna muda, e precisa s saber o tamanho para dar as
    #possíveis posições. Análogo para a vertical. Lina e coluna são as coordenadas da "cabeça" do barco.

    posicoes = []
    #entendendo orientação:
    if orientacao == "horizontal":
        for i in range(tamanho):
            posicoes.append([linha, coluna+i])
        return posicoes
    else:
        for i in range(tamanho):
            posicoes.append([linha+i, coluna])
        return posicoes


def preenche_frota(dicio, nome, linha, coluna, orientacao, tamanho):
        if nome not in dicio:
            dicio[nome] = []
        posicaonova = define_posicoes(linha, coluna, orientacao, tamanho)
        dicio[nome].append(posicaonova)
        return dicio 



def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] ==1:
        tabuleiro[linha][coluna] = "X"
    elif tabuleiro[linha][coluna] ==0:
        tabuleiro[linha][coluna] = "-"
    return tabuleiro


def posiciona_frota(frota):
    grid = [
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
    ]
    for lista in frota.values():
        for i in range(len(lista)):
            for j in range(len(lista[i])):
                linha = lista[i][j][0]
                coluna = lista[i][j][1]
                grid[linha][coluna] = 1
    return grid


