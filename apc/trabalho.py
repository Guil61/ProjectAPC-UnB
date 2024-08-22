from textos import texto_port, texto_ticuna, texto_instrucoes


print("Seja bem-vindo(a) ao nosso correlacionador de frases português/ticuna.\n")
print("1 - Traduzir frase em português para ticuna")
print("2 - Traduzir frase em ticuna para português")
print("9 - Sair do programa")

escolha = input("\nDigite a opção desejada: ")

if escolha != '1' and escolha != '2' and escolha != '9':
        print("Opção inválida, tente novamente.")
        escolha = input("\nDigite a opção desejada: ")
elif escolha == '9':
    quit()

print("Siga as seguintes instruções: \n", texto_instrucoes)
frase = input("Insira a frase que deseja traduzir: ")

while len(frase) <= 4 or (texto_port.find(frase) == -1 and texto_ticuna.find(frase) == -1):
    if len(frase) <= 4:
        print("Frase muito curta, por favor, tente novamente.")
    elif texto_port.find(frase) == -1:
        print("A frase não está no texto, por favor, tente novamente.")

    frase = input("Insira a frase que deseja traduzir: ")


if escolha == '1':       
    num = texto_port[texto_port.find(frase) - 3] + texto_port[texto_port.find(frase) - 2]

    pos_num_ticuna = int(texto_ticuna.find(num))

    pos_prox_num_ticuna = int(texto_ticuna.find(str(int(num) + 1)))

    tam_frase_ticuna = pos_prox_num_ticuna - pos_num_ticuna

    frase_traduzida =  texto_ticuna[pos_num_ticuna + 2 : pos_num_ticuna + tam_frase_ticuna - 1] 
    
    if tam_frase_ticuna > len(frase):
        print("\nA frase está incompleta, mas corresponde à parte da seguinte frase em ticuna: \n")
    
    else:
        print("\n A frase corresponde em ticuna é: \n")
    
    print(frase_traduzida)



if escolha == '2':
    num = texto_ticuna[texto_ticuna.find(frase) - 3] + texto_ticuna[texto_ticuna.find(frase) - 2]

    pos_num_port = int(texto_port.find(num))

    pos_prox_num_port = int(texto_port.find(str(int(num) + 1)))

    tam_frase_port = pos_prox_num_port - pos_num_port

    frase_traduzida =  texto_port[pos_num_port + 2 : pos_num_port + tam_frase_port - 1]
    
    if tam_frase_port > len(frase):
        print("\nA frase está incompleta, mas corresponde à parte da seguinte frase em português: \n")
    
    else:
        print("\n A frase corresponde em português é: \n")
    
    print(frase_traduzida)



