print ("****** CALCULADORA SIMPLES PYTHON *******")

op = 1
while(op !=0 ):
    print("\nEscolha uma opção:",
            "\n\t1 - Soma", 
            "\n\t2 - Subtração",
            "\n\t3 - Multiplicação", 
            "\n\t4 - Divisão", 
            "\n\t0 - Sair")
    op = int(input("Opção: "))

    
    if (op > 0 and op < 5):
        a = int(input("Digite o primeiro numero: "))
        b = int(input("Digite o segundo numero: "))

        res = 0
        if (op == 1):
            res = a + b
        elif (op == 2):
            res = a - b
        elif (op == 3):
            res = a * b
        elif (op == 4):
            if (b == 0):
                print ("\n\nERRO - IMPOSSIVEL DIVIDIR POR ZERO. Tente Novamente!")
                res = "INVALIDO"
            else:
                res = a / b
        print("\n\nRESULTADO:", res)
    elif (op == 0):
        print("\n\nSAINDO - MUITO OBRIGADO!\n\n\n")
    else: 
        print("\n\nERRO - OPÇÃO INVÁLIDA")
        

