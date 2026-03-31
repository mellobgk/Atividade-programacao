num1 = int(input("DIGITE O PRIMEIRO NÚMERO INTEIRO: "))
num2 = int(input("DIGITE O SEGUNDO NÚMERO INTEIRO: "))
num3 = int(input("DIGITE O TERCEIRO NÚMERO INTEIRO: "))

if num1 < num2 and num1 < num3:
    print("O PRIMEIRO NÚMERO É O MENOR")
elif num2 < num1 and num2 < num3:
    print("O NÚMERO DOIS É O MENOR")
elif num3 < num1 and num3 < num2:
    print("O TERCEIRO NÚMERO É O MENOR")

else: 
    if num1 == num2 == num3 : 
        print("OS TRÊS NÚMEROS SÃO IGUAIS")
    elif num1 == num2:
        print("O PRIMEIRO NÚMERO É IGUAL AO SEGUNDO NÚMERO")
    elif num1 == num3:
        print("O PRIMEIRO NÚMERO É IGAUL AO TERCEIRO NÚMERO")
    elif num2 == num3:
        print("O SEGUNDO NÚMERO É IGAUL AO TERCEIRO NÚMERO")