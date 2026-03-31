num1 = float(input("DIGITE UM NÚMERO: "))
num2 = float(input("DIGITE UM NÚMERO: "))
num3 = float(input("DIGITE UM NÚMERO: "))

if num1 > num2 and num2 > num3 and num1 > num3 :
    print(num3, num2, num1)
elif num2 > num1 and num1 > num3 and num2 > num3 :
    print(num3, num1, num2)
elif num3 > num1 and num3 > num2 and num2 > num1 :
    print(num1, num2, num3)
elif num3 > num2 and num3 > num1 and num1 > num2 :
    print(num2, num1, num3)
elif num2 > num1 and num2 > num3 and num3 > num1 :
    print(num1, num3, num2)
elif num1 > num2 and num1 > num3 and num3 > num2 : 
    print(num2, num3, num1)
elif num1 == num2 == num3 : 
    print("OS TRÊS NÚMEROS SÃO IGUAIS")
elif num1 == num2 :
    print("O NÚMERO 1 É IGAUL AO NÚMERO DOIS")
elif num1 == num3 :
    print("O NÚMERO 1 É IGUAL O NÚMERO 3")
elif num2 == num3 :
    print("O NÚMERO 2 É IGAUL O NÚMERO 3")