funcionarios = []

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
    print()

    if escolha == 1:
        print('1- Cadastrar Funcionario')
        print('2- Listar Funcoinários')
        print()

        escolha1 = int(
            input('Escolha uma opção: '
                  )
        )
        print()

        if escolha1 == 1:
            nome = input('Nome do funcionario: '
                        )
            salario = float(
                input('Salario do funcionario: '
                    )
            )
            idade = int(
                input('Idade do funcionario: '
                    )
            )
            funcao = input('Função do funcionario: '
                        )

            funcionario = {
                'nome': nome,
                'salario': salario,
                'idade': idade,
                'funcao': funcao
            }

            funcionarios.append(funcionario)
            print()
            print('FUNCIONÁRIO CADASTRADO COM SUCESSO')
            print()

        elif escolha1 == 2:

            quantidade = len(funcionarios)

            if quantidade == 0:
                print('NENHUM FUNCIONÁRIO CADASTRADO')
                print()
                
            else:
                for funcionario in funcionarios:
                    print('nome: ', funcionario['nome'], '|',  'salario: ',  funcionario['salario'], '|', 'idade: ', funcionario['idade'], '|', 'função: ', funcionario['funcao'])
                    print()

        else:
            print('VOCÊ DIGITOU ERRADO!')
            print()

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