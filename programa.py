import funcoes as fn
import random

frota = {}
navios = {
    "porta-aviões": [1,4],
    "navio-tanque": [2,3],
    "contratorpedeiro": [3,2],
    "submarino": [4,1]
}
for nome in navios:
    quantidade = navios.get(nome)[0]
    tamanho = navios.get(nome)[1]
    
    navios_colocados = 0
    while navios_colocados < quantidade:
        print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
        linha = int(input("Linha "))
        coluna = int(input("Coluna "))
        
        if nome != "submarino":
            orientacao = int(input("[1] Vertical [2] Horizontal "))
            if orientacao == 1:
                orientacao = "vertical"
            else:
                orientacao = "horizontal"
        else:
            orientacao = "horizontal" 

        if fn.posicao_valida(frota, linha, coluna, orientacao, tamanho) == False:
            print("Esta posição não está válida!") 
        else:
            fn.preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
            navios_colocados += 1

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
posicoes_ataque_oponente = [] 
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
    teste2 = False
    while teste2 == False:
        teste2 = True
        linha_ataque = int(input("Jogador, qual linha deseja atacar?"))
        while linha_ataque not in [0,1,2,3,4,5,6,7,8,9]:
            print('Linha inválida!')
            linha_ataque = int(input("Jogador, qual linha deseja atacar?"))

        coluna_ataque = int(input("Jogador, qual coluna deseja atacar?"))
        while coluna_ataque not in [0,1,2,3,4,5,6,7,8,9]:
                print('Linha inválida!')
                coluna_ataque = int(input("Jogador, qual coluna deseja atacar?"))

        posicao = [linha_ataque, coluna_ataque]
        if posicao not in posicao_ataque:
            posicao_ataque.append(posicao)
        else:
            print(f'A posição linha {linha_ataque} e coluna {coluna_ataque} já foi informada anteriormente!')
            teste2 = False

        tabuleiro_oponente = fn.faz_jogada(tabuleiro_oponente, linha_ataque, coluna_ataque)

        afundado = fn.afundados(frota_oponente, tabuleiro_oponente)

    if afundado == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!') 
        jogando = False
        
    else: 
        jogada_oponente_valida = False
        while jogada_oponente_valida == False:
            linha_oponente = random.randint(0, 9)
            coluna_oponente = random.randint(0, 9)
            
            if [linha_oponente, coluna_oponente] not in posicoes_ataque_oponente:
                posicoes_ataque_oponente.append([linha_oponente, coluna_oponente])
                jogada_oponente_valida = True
                
        print(f'Seu oponente está atacando na linha {linha_oponente} e coluna {coluna_oponente}')
        
        tabuleiro_jogador = fn.faz_jogada(tabuleiro_jogador, linha_oponente, coluna_oponente)
        
        afundados_jogador = fn.afundados(frota, tabuleiro_jogador)
        if afundados_jogador == 10:
            print('Xi! O oponente derrubou toda a sua frota =(')
            jogando = False