#Trabalho enquete
def cadastrar_opcao(lista_opcoes, lista_votos):  #1. Cadastrar Opção
    opcao = input("Digite uma opção de voto: ")
    lista_opcoes.append(opcao) #lista_opcoes é a lista que vai armazenar as opções
    lista_votos.append(0) #lista_votos é a lista que vai armazenar a qtd de votos de cada opção

def registrar_voto(lista_opcoes, lista_votos): #3. Registrar Voto
    for i in range(len(lista_opcoes)):
            print(f"{i + 1} -> {opcoes[i]}")  #lista as opções com um número para votar em cada uma
    voto = int(input("Digite o seu voto: "))
    for i in range(len(lista_opcoes)):
        if voto == (i + 1):  #acha o índice da opção votada
            lista_votos[i] += 1  #o índice da lista_votos corresponde ao índice da lista_opcoes

def mostrar_resultado(lista_opcoes, lista_votos): #5. Mostrar Resultado
    for i in range(len(lista_opcoes)):
        porcentagem = (lista_votos[i] / sum(lista_votos)) * 100
        print(f"{lista_opcoes[i]} = {lista_votos[i]} votos ({porcentagem:.2f}%)")

def mostrar_vencedor(lista_opcoes, lista_votos): #6. Mostrar Opção Vencedora
    mais_votos = max(lista_votos)
    vencedores = []
    for i in range(len(lista_votos)):
        if lista_votos[i] == mais_votos:
            vencedores.append(lista_opcoes[i])
    if len(vencedores) == 1:
        porcentagem_vencedor = (mais_votos / sum(lista_votos)) * 100
        print(f"Vencedor: {vencedores[0]} com {mais_votos} votos ({porcentagem_vencedor:.2f}%)")
    else:
        print(f"Houve um empate entre {len(vencedores)} vencedores.")
        print(f"Vencedores: {vencedores} com {mais_votos} votos cada.")
        

opcoes = []
votos = []
escolha = 0
while escolha != 7:
    escolha = int(input("Digite um dos seguintes números para escolher uma opção: \n 1. Cadastrar Opção. \n 2. Listar Opções. \n 3. Registrar Voto \n 4. Consultar Quantidade de Votos. \n 5. Mostrar Resultado. \n 6. Mostrar Opção Vencedora \n 7. Encerrar \n\n> "))
    if escolha == 1:
        cadastrar_opcao(opcoes, votos)
    elif escolha == 2:
        print(f"lista atual de opções: {opcoes}\n")
    elif escolha == 3:
        registrar_voto(opcoes, votos)
    elif escolha == 4:
        print(f"{sum(votos)} votos totais.")
    elif escolha == 5:
        mostrar_resultado(opcoes, votos)
    elif escolha == 6:
        mostrar_vencedor(opcoes, votos)
    elif escolha == 7:
        print("Encerrando o programa...")
    else:
        print("Opção Inválida!")