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


