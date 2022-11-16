import random
# Import random é utilizado para sortear o número de chave de segurança
i = 0
# Contador é utilizado para contar quantas resposta deram "sim"
while True:
    print("\33[0;31;40mCapitão Otavio:\33[m",
          "Boa tarde,responda as seguintes questões somente com sim ou não")
    print("\33[0;31;40mCapitão Otavio:\33[m",
          "O(A) senhor(a) é um(a) inspetor(a)?")
    pergunta = (input("\33[0;34;40mDigite sim ou nao :\33[m"))
    if pergunta == "nao":
    # Caso a resposta seja "nao" seu acesso será negado, assim encerrando o questionário
        print("\33[0;35;40mAcesso Negado\33[m")
        break
    if pergunta == "sim":
    # Respostas "sim" te levará para questão seguinte
        i += 1
        print("")
        print("\33[0;31;40mCapitão Otavio:\33[m",
              "Poderia mostrar sua credencial de inspetor(a)?")
        credencial = (input("\33[0;34;40mDigite sim ou nao :\33[m"))
        if credencial == "nao":
            print("\33[0;35;40mAcesso Negado\33[m")
            break
        if credencial == "sim":
            i += 1
            print("")
            print("\33[0;31;40mCapitão Otavio:\33[m",
                  "Ok, por razões de segurança possuimos uma palavra-chave para liberar o acesso ao navio")
            print("\33[0;31;40mCapitão Otavio:\33[m",
                  "Podemos seguir adiante?")
            registro = (input("\33[0;34;40mDigite sim ou nao :\33[m"))
            if registro == "nao":
                print("\33[0;35;40mAcesso Negado\33[m")
                break
            if registro == "sim":
                i += 1
                print("")
                # Cadeia de caracteres e números usados para gerar a palavra-chave e as mensagem cifradas e decifradas
                alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", ".", ",", "?", ":", ";", "!", "s", "t", "u", "v", "w", "x", "y", "z",
                            "5", "3", "8", "2", "7", "6", "1", "4", "9", "J", "K", "@", "#", "$", "%", "&", "*", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "D", "E", "C", "G", "I", "H", "F", "K", "J",
                            " "]
                lista = []
                mensagem = (input(
                    "\33[0;31;40mCapitão Otavio:\33[m" "" "Qual palavra-chave deseja utilizar: "))
                x = random.randint(1, 100)
                # Sorteador da chave de segurança
                chave = (x)
                # A chave é utilizada para localizar o indice da letra e substitui-lo
                print("\33[0;31;40mCapitão Otavio:\33[m",
                      "Sua chave de segurança é:", x)
            print("")
            print("\33[0;31;40mCapitão Otavio:\33[m",
                  "Por gentileza, jamais repasse sua palavra-chave e sua chave de segurança, pois através delas identificamos quem é você.")
            print("")
    if registro and credencial and pergunta == "sim":
        print("\33[0;31;40mCapitão Otavio:\33[m",
              "Acesso liberado, Deseja ir para o navio ?")
        navio = (input("\33[0;34;40mDigite sim ou nao :\33[m"))
        if navio == "nao":
            break
        if navio == "sim":
            i += 1
            print("──────██")
            print("─────████")
            print("────▄███")
            print("────▀▀████")
            print("──────▀▀████───────██")
            print("────────▀▀████───────██")
            print("──────────▀▀████───────██")
            print("────────────▀▀████───────██")
            print("──────────────▀▀████████───██")
            print("────────────────▀█████████───██")
            print("─────────────────████████████──██")
            print("──────────────────████████████───██")
            print("───────────────────███████████▄────██")
            print("────────────────█──█████████───█─────██")
            print("──────────────────█─▀██████────█───────██")
            print("────────────────────█─▀█████───█")
            print("──────────────────────█─▀████▄▀")
            print("────────────────────────█")
            print("──────────────────────────█")

            print("")
            print("")
            print("                 ───|─────────────────────────────────────")
            print("                 ───│────────▄▄───▄▄───▄▄───▄▄───────│────")
            print("                 ───▌────────▒▒───▒▒───▒▒───▒▒───────▌────")
            print("                 ───▌──────▄▀█▀█▀█▀█▀█▀█▀█▀█▀█▀▄─────▌────")
            print("                 ───▌────▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄───▋────")
            print("                 ▀██████████████████████████████████████▄─")
            print("                 ──▀███████████████████████████████████▀──")
            print("                 ─────▀██████████████████████████████▀────")
            print("                 ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
            print("                 ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
            print("                 ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
            # Ilustração representando a chegada ao navio
        print("")
        print("\33[0;35;40mVocê chegou no Navio\33m")
        print("")
        print("\33[0;35;40mDeseja enviar alguma mensagem criptografada para O Capitão Otavio ou descriptografar alguma mensagem recebida?\33[m")
        quest = (input("\33[0;34;40mDigite sim ou nao :\33[m"))
        if quest == "sim":
            i += 1
            print("")
        senhacorreta = (input("\33[0;31;40mCapitão Otavio:\33[m"""
                              "Por favor, informe sua palavra-chave:"))
        while senhacorreta != mensagem:
            senhacorreta = (input("\33[0;31;40mCapitão Otavio:\33[m"
                                  "Você digitou sua palavra-chave incorretamente,por favor, informe sua palavra-chave:"))
        chave = int(input("\33[0;31;40mCapitão Otavio:\33[m"
                          "Por favor ,Digite sua chave de segurança:"))
        while chave != x:
            chave = int(input(
                "\33[0;31;40mCapitão Otavio:\33[m""Você digitou sua chave de segurança incorretamente,por favor,informe sua chave de segurança:"))
        print("")
        if quest == "nao":
            print("Ok, volte outra hora")
            print("")
        break
# Se todas respostas foram atendidas corretamente seguirá para próxima etapa
# Onde ocorre a criptografia e a descriptografia da mensagem
while i >= 5:
    resposta = (
        input("\33[0;35;40mPara criptografar aperte c ,para descriptografar aperte d ou s para sair:\33[m"))
    if resposta == "s":
        break
# O processo se resume em a pessoa digitar a mensagem que deseja criptografar
# A chave é representada pelo x
    if resposta == "c":
# Com a resposta sendo "c" acontecerá a criptografia
        lista = []
        mensagem = (
            input("\33[0;35;40mQual palavra deseja criptografar:\33[m"))
        n = len(alfabeto)
# Depois, a palavra digitada terá seu indice contado representado por n
        cifrada = ""
        for letra in mensagem:
# Através da estrutura de repetição "for" cada letra da mensagem digitada é encontrada na cadeia de caracteres e números (alfabeto)
            indice = alfabeto.index(letra)
            nova_string = alfabeto[(indice + x) % n]
# A criptografia acontece capturando o (indice da letra + chave) %(resto) n
            cifrada = cifrada + nova_string
            lista.append(mensagem)
        print(
            "\33[0;35;40mSua mensagem criptografa enviada é:\33m", cifrada)
        print("")
    if resposta == "d":
# Com a resposta sendo "d" acontecerá a descriptografia
        lista = []
        mensagem = (
            input("\33[0;35;40mQual palavra deseja descriptografar:\33[m"))
        n = len(alfabeto)
        decifrada = ""
        for letra in mensagem:
            indice = alfabeto.index(letra)
            nova_string = alfabeto[(indice - x) % n]
# O calcúlo será (indice da letra - chave) %(resto) n, pois deve-se seguir o caminho reverso da criptografia
            decifrada = decifrada + nova_string
            lista.append(mensagem)
        print(
            "\33[0;35;40mSua mensagem descriptografada enviada é:\33m", decifrada)
        print("")