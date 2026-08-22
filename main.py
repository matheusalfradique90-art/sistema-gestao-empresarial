while True:
    print('='*40)
    print('             NEXORA')
    print('  sistema de gestão empresarial')
    print('='*40)
    print()

    print('1- Funcionarios')
    print('2- Clientes')
    print('3- Produtos')
    print('4- Estoque')
    print('5- Pedidos')
    print('6- Financeiro')
    print('0- SAIR')
    print()

    escolha = int(input('Escolha uma opção: '))

    if escolha == 1:
        print('Você escolheu funcionarios')

    elif escolha == 2:
        print('Você escolheu clientes')

    elif escolha == 3:
        print('Você escolheu produtos')

    elif escolha == 4:
        print('Você escolheu estoque')
    
    elif escolha == 5:
        print('Você escolheu pedidos')

    elif escolha == 6:
        print('Você escolheu financeiro')

    elif escolha == 0:
        print('ENCERRANDO SISTEMA!')
        break

    else:
        print('OPÇÃO INVALIDA!')