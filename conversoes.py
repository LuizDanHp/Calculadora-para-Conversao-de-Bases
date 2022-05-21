import os

multiplicacao = 0

while True:
    os.system("cls" if os.name == "nt" else "clear")

    print("MENU PRINCIPAL: ")
    print("[1] Calculadora Decimal para outras bases")
    print("[2] Calculadora de outras bases para Decimal")
    print("[0] Sair")

    tipoCalc = int(input("Digite uma opção: "))

    if(tipoCalc == 0):
        break
    elif(tipoCalc == 1):
        while True:
            os.system("cls" if os.name == "nt" else "clear")

            print("Conversões da base decimal para outras bases: ")
            print("[1] Decimal para Binário")
            print("[2] Decimal para Hexadecimal")
            print("[3] Decimal para Octadecimal")
            print("[0] Voltar")
            op = int(input("Digite uma opção: "))

            if(op == 0):
                break

            elif(op == 1):  
                valor = int(input("Digite um número inteiro decimal: "))
                num = valor
                binario = ""

                while valor!=0:
                    r = valor%2
                    binario = str(r) + binario
                    valor = valor//2
                
                os.system("cls" if os.name == "nt" else "clear")

                print(f"O decimal {num} equivale a {binario} na base binário.")
                op = (input("Aperte ENTER para retornar ao menu: "))

            elif(op == 2):
                
                valor = input("Digite um número inteiro decimal: ")
                hex = ""

                listaHexa = ["0", "1", "2", "3", "4", "5", "6", "7", "8","9", 
                "A", "B", "C", "D", "E", "F",]
                            
                div = int(valor)
                resultado = div

                
                while (resultado >= 16):

                    resultado = div // 16
                    r = div % 16                   
                    div = resultado
                    hex += listaHexa[r]  

                hex += listaHexa[resultado]
                hex = hex[::-1]            
                
                print(f"O decimal {valor} equivale a {hex} na base hexadecimal.")
                op = (input("Aperte ENTER para retornar ao menu: "))

            elif(op == 3):
                valor = int(input("Digite um número inteiro decimal: "))
                num = valor
                div = ""
                while valor!=0:
                    r = valor%8
                    div = str(r) + div
                    valor = valor//8

                os.system("cls" if os.name == "nt" else "clear")
                print(f"O número decimal {num} equivale a {div} na base octadecimal.")
                op = (input("Aperte ENTER para retornar ao menu: "))
                
                
    elif(tipoCalc == 2):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print("Conversões de outras bases para Decimal: ")
            print("[1] Binario para Decimal")
            print("[2] Hexadecimal para Decimal")
            print("[3] Octadecimal para Decimal")
            print("[0] Voltar")
            op = int(input("Digite uma opção: "))
            if(op == 0):
                break

            elif(op == 1):
                valor = input("Digite um número binário: ")
                n = len(valor) -1

                for i in valor:
                    multiplicacao = multiplicacao + int(i)*2**n
                    n = n - 1

                os.system("cls" if os.name == "nt" else "clear")                
                print(f"O número binario {valor} equivale a {multiplicacao} na base decimal.")
                multiplicacao = 0
                op = (input("Aperte ENTER para retornar ao menu: "))

            elif(op == 2):
                listaHex = {"0": "0", "1": "1", "2": "2","3": "3", "4": "4","5": "5","6": "6", "7": "7", "8": "8","9": "9", 
                            "A": "10", "B": "11","C": "12", "D": "13", "E": "14", "F": "15"}

                valor = input("Digite um número hexadecimal: ")
                n = len(valor) -1
    
                for i in valor:
                    multiplicacao += int(listaHex[i.upper()])*16**n
                    n = n - 1

                os.system("cls" if os.name == "nt" else "clear")
                print(f"O número hexadecimal {valor} equivale a {multiplicacao} na base decimal.")
                multiplicacao = 0
                op = (input("Aperte ENTER para retornar ao menu: "))
            
            elif(op == 3):
                valor = input('Digite um número octadecimal: ')

                n = len(valor) - 1

                multiplicacao = 0

                for d in valor:
                    multiplicacao = multiplicacao + int(d)*8**n
                    n = n -1

                os.system("cls" if os.name == "nt" else "clear")
                print(f"O número octadecimal {valor} equivale a {multiplicacao} na base decimal.")
                op = (input("Aperte ENTER para retornar ao menu: "))
            
    
