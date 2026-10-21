print("=" *50)
print("   🤑 PLAY LAB - MISSAO : TEERMINAL MAL - ASSOMBRADO")


print ("=" *50)


print()


print("ripulante, um fantasma ewsta assombrando este terminal ")



print("ele deixou 3 enigmas escondido no sistema .")



print("sua missao: decifrar as pistas . o sistema vai calcular")



input ("pressione ENTER para iniciar o protocolo de acesso...")

print("|========================================|")
print("|      TERMINAL FANTASMA                 |")
print("|          PROTOCOLO COFR3_0903!         |")
print("|========================================|")



nome = input ("endentifique-se, hacker: ")

print()


print(nome + " ,o fantasma deixouy e enigmas antes do cofre abrir.")


print()


print ("ENIGMA !: `Sou o dobro de 21, menos a idade que voce tinha aos 7 anos multiplicada por 3 '")

resposta1 = int(input("suaresposta:"))

alvo1 = 42 - 21

erro1 = resposta1 - alvo1

erro_detectado1 = bool(erro1)

print()

print("ENIGMA 2: 'sou metade da temperatura de ebuliçao da agua em celsius, mais a quantidade de patas de uma aranha dividida por 2.'")

resposta2 = float(input("sua resposta:"))

alvo2= 50.0 + 4.0

erro2 = resposta2- alvo2

erro_detectado2 = bool(erro2)


pontuacao= 100-(erro1*erro1)-(erro2*erro2*100)

print()
print("="*30)

print("fim de jogo,", nome)
print("|__________________________________|")
print("pontuacaofinal foi :", pontuacao,"      |")
print("|__________________________________|")

