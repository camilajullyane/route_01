from random import randint, choice
mapa = [["A","A","A","A","A", "" ,"" ,"A","A","A","A","A"],
        ["A","","","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","" ,"" ,"" ,"A","" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","E","E","E","A","E","E","E","G","G","G","A"],
        ["A","" ,"" ,"" ,"A","G","G","G","G","G","G","A"],
        ["A","E","E","E","A","G","G","G","G","G","G","A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"G","G","G","A"],
        ["A","A","E","E","E","A","A","A","G","G","G","A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","E","" ,"E","E","" ,"E","E","E","E","E","A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" , "A"],
        ["A","A","A","A","A","A","G","G","G","E","E","A"],
        ["A","" ,"" ,"" ,"" ,"" ,"G","G","G","" ,"" ,"A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","E","E","" ,"" ,"E","E","E","E","E","E","A"],
        ["A","" ,"G","G","G","G","" ,"" ,"G","G","G","A"],
        ["A","G","G","G","" ,"" ,"" ,"G","G","" ,"" ,"A"],
        ["A","A","A","A","A","A","G","A","A","A","A","A"]]
posicao = [19, 6]
pokemon = ['Ratata', 'Pidgey', 'Weedle', 'Caterpie', 'Paras', 'Charmander', 'Bulbasaur', 'Squirtle', 'Pikachu', 'Evee']
pokedex = {}

def mostrarMenu():
    print('''
    9 - Para abrir esse menu
    8 - Subir
    2- Descer
    4 - Ir para esquerda
    6 - Ir para direta
    5 - Abrir Pokedex
    0 - Sair do Jogo''')


def abrirPokedex():
    while True:
        print('As espécies já registradas na pokedex são: ', end='')
        print(*pokedex.keys())
        print('''
        1 para Listar Detalhes
        2 para Apagar Registro
        0 para voltar ao menu principal
        ''')
        escolha = verificarMenu('Escolha uma ação: ', [0, 1, 2], 1)
        match escolha:
            case 0:
                break
            case 1:
                escolha_pokemon = verificarMenu('Nome da espécie: ', pokedex, 2) 
                print(pokedex[escolha_pokemon])
            case 2:
                escolha_pokemon = verificarMenu('Nome da espécie: ', pokedex, 2) 
                del pokedex[escolha_pokemon]
                print(f'O pokemon {escolha_pokemon} foi apagado do registro da pokedex')


def verificarMenu(texto, lista, tipo):
    if tipo == 1:
        resposta = int(input(texto))
        while resposta not in lista:
            resposta = int(input(f'Tente novamente. {texto}'))
        return resposta
    if tipo == 2:
        resposta = input(texto).capitalize()
        while resposta not in lista:
            resposta = str(input(f'Tente novamente. {texto}')).capitalize()
        return resposta


def acharPokemon():
    chance = randint(0, 9)
    if chance >= 5:
        print('Um pokemon selvagem apareceu!')       
        pergunta = verificarMenu('Capturar ou correr? [1-Capturar ou 2-Correr]', [1, 2], 1)
        if pergunta == 1:
            sorteio = choice(pokemon)
            if sorteio in pokedex:
                print('Já existe essa espécie de pokemon na pokedex!')
            else:
                print(f'Pokemon adicionado na pokedex')
                pokedex[sorteio] = {
                    'HP': randint(0,100),
                    'Atk': randint(0,100),
                    'Def': randint(0,100),
                    'Sp. Atk': randint(0,100),
                    'Speed Def': randint(0,100),
                    'Speed': randint(0,100)
                }
        if pergunta == 2:
            print('Cagão')

        
def verificarPosicao(valor):
    if valor == 8:
        if posicao[0]-1 == -1:
            return False
        elif mapa[posicao[0]-1][posicao[1]] == 'G':
            acharPokemon()
            posicao[0] -= 1
        elif mapa[posicao[0]-1][posicao[1]] == "":
            posicao[0] -= 1
        
        else:
            print('BUMP!')

    if valor == 2:
        if posicao[0]+1 == 20:
            return False
        elif mapa[posicao[0]+1][posicao[1]] == 'E':
            posicao[0] += 2  
            if mapa[posicao[0]][posicao[1]] == 'G':
                acharPokemon()
        elif mapa[posicao[0]+1][posicao[1]] == "":
            posicao[0] += 1
        elif mapa[posicao[0]+1][posicao[1]] == 'G':
            acharPokemon()
            posicao[0] += 1
        else:
            print('BUMP!')

    if valor == 4:
        if mapa[posicao[0]][posicao[1]-1] == "":
            posicao[1] -= 1
        elif mapa[posicao[0]][posicao[1]-1] == 'G':
            posicao[1] -= 1
            acharPokemon()
        else:
            print('BUMP!')

    if valor == 6:
        if mapa[posicao[0]][posicao[1]+1] == "":
            posicao[1] += 1
        elif mapa[posicao[0]][posicao[1]+1] == 'G':
            posicao[1] += 1
            acharPokemon()
        else:
            print('BUMP!')

print('''
    Bem-vindo!
    A qualquer momento você pode escolher uma das opções:
    ''')
mostrarMenu()
print('Entrando na Rota 01')

while True:
    if len(pokedex) == 10:
        print('Parabéns! Você completou a pokedex.')
        break
    print(f'Sua posição atual: {posicao}')
    resposta = verificarMenu('Escolha uma opção: ', [9, 8, 2, 4, 6, 5, 0], 1)
    
    match resposta:
        case 8:
            rodar = verificarPosicao(8)   
        case 2:
            rodar = verificarPosicao(2)
        case 4:
            verificarPosicao(4)
        case 6:
            verificarPosicao(6)
        case 5:
            abrirPokedex()
            mostrarMenu()
        case 0:
            break
        case 9:
            mostrarMenu()
    if rodar == False:
        print('Você saiu da Route 01')
        break