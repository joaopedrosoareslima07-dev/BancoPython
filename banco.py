def detail():
    print("-----------------------------")


tentativas = 0
saldo = 1000

extrato = []
usuarios = {"João123": 1607, "adm123":1234, "dalz":3210}

while True:
    usuario = input("Digite seu usuário: ")
    senha = int(input("Digite sua senha: "))
    
    if usuario in usuarios and usuarios[usuario] == senha:
         
     while True:
            print(f"Bem Vindo ao Banco, {usuario}!")
            
            #Menu 
            detail()
            print("Ver Saldo [01]")
            print("Adicionar valor [02]")
            print("Resgatar [03]")
            print("Ver extrato  [04]")
            print("Sair [05]")
            detail()
            opc = int(input("Digite uma opção "))
            
            #casos
           
            
            match opc:
                case 1:
                    detail()
                    print(f"Seu saldo atual é {saldo:.2f}")
                    detail()
                
                case 2:
                    
                    valorAdc = float(input("Digite o valor que você deseja adicionar "))
                    saldo += valorAdc
                    extrato.append(f" + {valorAdc}")
                    detail()
                    print("Valor adicionado com sucesso!")
                    detail()
                
                case 3:
                    
                    
                    valorRet= float(input("Digite o valor que você deseja retirar "))
                    
                    if valorRet > saldo:
                        detail()
                        print("Não é possivel realizar a operação ")
                        detail()
                        
                    else: 
                        saldo -= valorRet
                        detail()
                        print("Valor retirado ")
                        detail()
                        
                        extrato.append(f" - {valorRet}")
                        
                case 4:
                    detail()
                    print("Sua movimentação ")
                    print(extrato)
                    detail()
                   
                        
                        
                case 5:
                    detail()
                    print("Saindo....")
                    break
                case _:
                    print("Valor não encontrado!")  
                    
     break                  
                
    else :
        
        print("Senha incorreta! Tente novamente!")
        tentativas += 1
    
        if tentativas >= 3:
            print("Você atingiu o limite de tentativas ")
            break