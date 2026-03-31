cateto1 = float(input("DIGITE O VALOR DO CATETO: "))
cateto2 = float(input("DIGITE O VALOR DO SEGUNDO CATETO: "))

hipotenuza= ((cateto1 * cateto1) + (cateto2 * cateto2)) ** (1/2)

print(f"SUA HIPOTENUZA É: {hipotenuza: .2f}")