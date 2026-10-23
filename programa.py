import funcoes as fn
frota = {}
count =  0
navios = {
    "porta-aviões": [1,4],
    "navio-tanque": [2,3],
    "contratorpedeiro": [3,2],
    "submarino": [4,1]

}

for nome in navios:
    quantidade = navios.get(nome)[0]
    tamanho = navios.get(nome)[1]
    teste = False
    while teste == False:
        teste = True
        for i in range(quantidade):
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
            linha = int(input("Linha "))
            coluna = int(input("Coluna "))
            if nome != "submarino":
                orientacao = int(input("[1] Vertical [2] Horizontal "))
                if orientacao ==1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"
            else:
                orientacao = "horizontal" #indiferente mas precisa ter pra função funcionar

            if fn.posicao_valida(frota, linha, coluna, orientacao, tamanho) == False:
                teste = False
                print("Esta posição não está válida!") #tem que resolver essa buceta aqui 
                quantidade = quantidade - count
                break
            else:
                fn.preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                count+=1
        count = 0



frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = fn.posiciona_frota(frota_oponente)
tabuleiro_jogador = fn.posiciona_frota(frota)

posicao_ataque = []
afundado = 0
jogando = True
while jogando == True:
    def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
        texto = ''
        texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
        texto += '_______________________________      _______________________________\n'

        for linha in range(len(tabuleiro_jogador)):
            jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
            oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
            texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
        return texto
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    teste2 =False
    while teste2 == False:
        teste2 = True
        linha_ataque = int(input("Jogador, qual linha deseja atacar?"))
        while linha_ataque not in [0,1,2,3,4,5,6,7,8,9,]:
            print('Linha inválida!')
            linha_ataque = int(input("Jogador, qual linha deseja atacar?"))

        coluna_ataque = int(input("Jogador, qual coluna deseja atacar?"))
        while coluna_ataque not in [0,1,2,3,4,5,6,7,8,9]:
            print('Coluna inválida!')
            coluna_ataque = int(input("Jogador, qual coluna deseja atacar?"))

        posicao = [linha_ataque, coluna_ataque]
        if posicao not in posicao_ataque:
            posicao_ataque.append(posicao)
        else:
            print(f'A posição linha {linha_ataque} e coluna {coluna_ataque} já foi informada anteriormente!')
            teste2 = False

        tabuleiro_oponente = fn.faz_jogada(tabuleiro_oponente, linha_ataque, coluna_ataque)

        afundado=fn.afundados(frota_oponente, tabuleiro_oponente)

    if afundado ==10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!') 
        jogando = False

