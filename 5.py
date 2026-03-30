#IMC

peso = float(input("DIGITE SEU PESO: "))
altura = float(input("DIGITE SUA ALTURA EM CENTÍMETRO: "))
altura_metros = altura / 100

imc = peso / altura_metros ** 2 

print(f"O SEU IMC É, {imc: .2f}")

if float(imc <= 18.5):
    print("VOCÊ ESTÁ ABAIXO DO PESO")

elif float(imc > 18.5 or imc >= 24.9):
    print("PESO NORMAL")

elif float(imc >= 25.0 or imc <= 29.9):
    print("SOBREPESO")

else:
    print("OBESIDADE")
