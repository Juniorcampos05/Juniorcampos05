print("Imc Calculator")
nome = input("Qual e o seu nome ?")
idade = input("Qual e o sua idade ?")
altura = float(input("Qual sua altura ? "))
peso = float(input("Qual e o seu peso ? "))

calculo = peso / (altura ** 2)

print(f"{nome} o seu imc foi de {calculo:.2f}")

if calculo <18:
    print("Seu imc está abaixo do ideal")
elif calculo > 25:
    print("Seu imc está acima do normal")
else:
    print("Seu peso está ideal")
    
    
print("Agora me deixe adivinhar o ano que nasceu ")
idade = int(input("Me fale apenas sua idade e vou adivinhar !! "))
ano_atual = 2024
formula =  2024 - idade
print(f"{nome} Voce nasceu no ano de {formula}")

if idade > 18:
    print("E voce tem mais de de 18 anos !!")
elif idade < 18:
    print("Voce não e maior de 18 anos !!")
    
print("Foi um prazer te ajudar atenciosamente PYTHON ")