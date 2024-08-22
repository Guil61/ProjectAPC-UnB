from textos1 import texto_port, texto_ticuna, texto_instrucoes


print(texto_instrucoes)
print("1 - Traduzir frase em português para ticuna")
print("2 - Traduzir frase em ticuna para português")

escolha = input("Digite a opção desejada: ")

print("Siga as seguintes instruções: ")

frase = input("Insira a frase que deseja traduzir: ")

while len(frase) <= 4 or (texto_port.find(frase) == -1 and texto_ticuna.find(frase) == -1):
    if len(frase) <= 4:
        print("Frase muito curta, por favor, tente novamente.")
    elif texto_port.find(frase) == -1:
        print("A frase não está no texto, por favor, tente novamente.")
    elif escolha != 1 or escolha != 2 or escolha != 9:
        print("Opção inválida, tente novamente.")

    frase = input("Insira a frase que deseja traduzir: ")


if escolha == '1':       
    num = texto_port[texto_port.find(frase) - 3] + texto_port[texto_port.find(frase) - 2]

    num_ticuna = int(texto_ticuna.find(num))

    prox_num_ticuna = int(texto_ticuna.find(str(int(num) + 1)))

    tam_frase_ticuna = prox_num_ticuna - num_ticuna

    frase_traduzida =  texto_ticuna[num_ticuna + 2 : num_ticuna + tam_frase_ticuna - 1] 

    print(frase_traduzida)



if escolha == '2':
    num = texto_ticuna[texto_ticuna.find(frase) - 3] + texto_ticuna[texto_ticuna.find(frase) - 2]

    num_port = int(texto_port.find(num))

    prox_num_port = int(texto_port.find(str(int(num) + 1)))

    tam_frase_port = prox_num_port - num_port

    frase_traduzida =  texto_port[num_port + 2 : num_port + tam_frase_port - 1] 

    print(frase_traduzida)




