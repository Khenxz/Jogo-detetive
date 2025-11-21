# Mistério da Mansão São jose dos pinhais
# Autor: (Thiago ,Erick)
# Objetivo: jogo detetive aplicando logica

# -----------------------------
# Dicionário de pistas
# Cada chave é o código da pista (ex: "P1")
# Cada valor é uma lista
# estado: True = verdadeira, False = falsa, None = indeterminada
# -----------------------------
pistas = {
    "P1": ["A porta do escritório estava trancada.", True],
    "P2": ["Passos foram ouvidos na biblioteca.", True],
    "P3": ["Renato discutiu com Álvaro pela manhã.", True],
    "P4": ["A arma foi um castiçal.", True],

    "P7": ["Renato estava no escritório na hora do crime.", False],
    "P8": ["Camila estava dormindo durante o crime.", False],

    "P10": ["Pegadas molhadas no corredor.", None],
    "P12": ["O castiçal tinha digitais de duas pessoas.", None]
}

# -----------------------------
# Lista que guarda quais pistas o jogador "usou"
# Começa vazia; quando o jogador usa uma pista, adicionamos o código aqui.
# -----------------------------
usadas = []


# -----------------------------
# Função mostrar_pistas()
# Mostra na tela todas as pistas disponíveis (somente texto).
# Não revela se são verdadeiras/falsas — apenas lista para o jogador.
# -----------------------------
def mostrar_pistas():
    print("\n=== PISTAS ===")
    # Percorre as chaves do dicionário 'pistas' e imprime código + texto
    for pid in pistas:
        print(pid, "-", pistas[pid][0])
    print("==============\n")


# -----------------------------
# Função revelar(pid)
# Recebe um código de pista e mostra se ela é VERDADEIRA / FALSA / INDETERMINADA.
# Usa o segundo elemento da lista dentro do dicionário 'pistas'.
# -----------------------------
def revelar(pid):
    estado = pistas[pid][1]  # pega True/False/None
    if estado is True:
        print("Essa pista é VERDADEIRA.")
    elif estado is False:
        print("Essa pista é FALSA.")
    else:
        print("Essa pista é INDETERMINADA.")


# -----------------------------
# Função deduzir()
# Examina a lista 'usadas' (pistas registradas pelo jogador)
# e imprime deduções simples baseadas nas pistas usadas.
# -----------------------------
def deduzir():
    print("\n=== DEDUÇÕES ===")
    # Se o jogador usou P1 e P2, sugerimos passagem secreta
    if "P1" in usadas and "P2" in usadas:
        print("- Alguém pode ter usado passagem secreta.")
    # Se usou P8 (falsa) e P3 (verdadeira) mostramos que Camila mentiu + tinha motivo
    if "P8" in usadas and "P3" in usadas:
        print("- Camila mentiu e tinha motivo.")
    # Se usou P4, sabemos qual arma foi (castiçal)
    if "P4" in usadas:
        print("- A arma foi o castiçal.")
    print("================\n")


# -----------------------------
# Função menu()
# Implementa o fluxo principal do jogo
# - mostra opções ao jogador
# - lê um comando
# - executa ação correspondente
# - chama menu() novamente para continuar
# Caso base (condição de parada): o jogador digita "sair" ou acerta a solução.
# -----------------------------
def menu():
    # Mostra os comandos possíveis
    print("Comandos:")
    print("  pistas")
    print("  usar P?")
    print("  revelar P?")
    print("  deduzir")
    print("  responder")
    print("  sair\n")

    # Lê uma linha do jogador
    cmd = input("Digite: ")

    # Se o jogador digitar exatamente "sair", paramos (caso base)
    if cmd == "sair":
        print("Fim da investigação.")
        return  # retorna sem chamar menu() 

    # Se o jogador pedir "pistas", mostramos as pistas
    elif cmd == "pistas":
        mostrar_pistas()

    # Para comandos do tipo "usar P3" dividimos a string em partes
    # usando split() e verificamos manualmente (sem startswith)
    partes = cmd.split()

    # Se o jogador digitou duas palavras e a primeira é "usar", tratamos como usar uma pista
    if len(partes) == 2 and partes[0] == "usar":
        pid = partes[1].upper()  # transforma em maiúsculas para padronizar
        # Verifica se o código existe no dicionário de pistas
        if pid in pistas:
            # Se ainda não foi usada, adiciona em 'usadas'
            if pid not in usadas:
                usadas.append(pid)
                print("Pista registrada:", pid)
            else:
                # Se já foi usada antes, avisa o jogador
                print("Você já usou essa pista.")
        else:
            # Se o código não existe, avisa erro
            print("Pista inexistente.")

    # Se o jogador digitou duas palavras e a primeira é "revelar", mostramos o tipo da pista
    elif len(partes) == 2 and partes[0] == "revelar":
        pid = partes[1].upper()
        if pid in pistas:
            revelar(pid)  # chama função que revela True/False/None
        else:
            print("Pista inexistente.")

    # Se o jogador pediu "deduzir", rodamos a função de deduções (usa lista 'usadas')
    elif cmd == "deduzir":
        deduzir()

    # Se o jogador tentar responder o caso, pedimos culpado, arma e local
    elif cmd == "responder":
        culpado = input("Culpado: ").lower()
        arma = input("Arma: ").lower()
        local = input("Local: ").lower()

    # Gabarito
    certo_culpado = "camila"
    certo_arma = "castiçal"
    certo_local = "escritório"

    acertos = 0

    # Verifica cada parte separadamente
    if culpado == certo_culpado:
        print(" Culpado correto!")
        acertos += 1
    else:
        print(" Culpado incorreto.")

    if arma == certo_arma:
        print(" Arma correta!")
        acertos += 1
    else:
        print(" Arma incorreta.")

    if local == certo_local:
        print(" Local correto!")
        acertos += 1
    else:
        print("✘ Local incorreto.")

    print(f"\n Acertos totais: {acertos}/3\n")

    # Vitória somente se acertar tudo
    if acertos == 3:
        print("🎉 Caso resolvido! Você solucionou o crime!")
        return
    else:
        print("Continue investigando...\n")


    
    menu()


# -----------------------------
# Função iniciar()
# Apresenta o título e chama menu() pela primeira vez.
# -----------------------------
def iniciar():
    print("==============================")
    print(" Mistério da Mansão (Versão Curta)")
    print("==============================")
    menu()  # primeira chamada recursiva


# -----------------------------
# Ponto de entrada do programa
# -----------------------------
iniciar()
