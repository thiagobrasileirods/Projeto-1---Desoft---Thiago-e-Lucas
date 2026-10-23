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
print(frota)