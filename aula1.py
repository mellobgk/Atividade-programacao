#informações do usuário
from validate_docbr import CPF

cpf_validator = CPF()

nome = str(input("DIGITE SEU NOME: "))
nacionalidade = str(input("DIGITE SUA NACIONALIDADE:  (Brasileira ou estrangeira): ")).lower()

if nacionalidade == "brasileira" :
    cpf = str(input("DIGITE SEU CPF: "))
   
    if cpf_validator.validate(cpf):
        print("OLÁ, ", nome, "!!", "SUA INDÊNTIFICAÇÃO É ", cpf)

    else: 
        print("CPF INVÁLIDO!!!  VERIFIQUE OS NÚMEROS. ")

else:
    crnm = str(input("DIGITE SEU CRNM: "))
    print("OLÁ,", nome, "!! seu CRNM é", crnm)




