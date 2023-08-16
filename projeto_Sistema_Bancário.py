menu = """
    Escolha uma das operações abaixo:

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair

"""

LIMITE_DE_SAQUES = 3

limite_do_cliente = 500
saldo_do_cliente = 0
extrato_do_cliente = ""
numero_de_saques_do_cliente_hoje = 0

realizar_operações = True

while realizar_operações == True:

    opção = int(input(menu))
    if opção == 1:
        valor_depositado = float(input("Digite a quantia que deseja depositar: "))
        if valor_depositado > 0:
            saldo_do_cliente += valor_depositado
            extrato_do_cliente += f"Valor depositado: +R${valor_depositado:.2f}\n"
            print("Depósito realisado. Retornando ao menu inicial.")

        else: print("Valor de depósito inválido. Retornando ao menu inicial.")

    elif opção == 2:
        if numero_de_saques_do_cliente_hoje == LIMITE_DE_SAQUES:
            print("Limite diário de saques atingido, a operação não pode ser realizada hoje. Retornando ao menu inicial.")
        else:
            valor_sacado = float(input("Digite a quantia que deseja sacar: "))
            if (valor_sacado <= saldo_do_cliente):
                if (valor_sacado <= limite_do_cliente):
                    saldo_do_cliente -= valor_sacado
                    extrato_do_cliente += f"Valor sacado: -R${valor_sacado:.2f}\n"
                    print("Saque realisado. Retornando ao menu inicial.")
                    numero_de_saques_do_cliente_hoje += 1
                else: print("Seus saques não podem ultrapassar o limite de {limite}. A operação não pôde ser relizada. Retornando ao menu inicial." .format(limite = limite_do_cliente))
            else: print("Saldo Insuficiente. A operação não pôde ser realizada. Retornando ao menu inicial.")
    
    elif opção == 3:
        output_do_extrato = f"{extrato_do_cliente}\nSaldo atual: R$ {saldo_do_cliente:.2f}\nRetornando ao menu inicial."
        print(output_do_extrato)

    elif opção == 4:
        print("Encerrando operações. Obrigado pela preferência.")
        realizar_operações = False

    else:
        print("Opção inválida, favor selecionar uma das operações disponíveis.")

### NOTAS:###
# 1) Aguardando instruções para erro de tipo de dado de entrada nas opções de menu e nos valores. IMPLEMENTAR MAIS TARDE.
# 2) O controle de quantidade de casa decimal dos valores só é realizado para a impressão (duas casas decimais),
#    os valores aceitam qualquer quantidade de casas decimais. AGUARDANDO INTRUÇÕES ADICIONAIS DE IMPLEMENTAÇÃO.
# 3) output_do_extrato editado com aspas simples para facilitar leitura do código. IMPLEMENTAR ASPAS TRIPLAS CASO 
#    FUNÇÕES SEJAM UTILIZADAS FUNÇÕES EVENTUALMENTE.
# 4) Tentar diminuir quantidade de identações mais tarde para facilitar leitura de código. 
#    Talvez após implementação de listas e de funções.
# 5) 
#############

    
