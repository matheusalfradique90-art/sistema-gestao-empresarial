funcionarios = []
clientes = []

# TODO: ---------------------------
# *!FUNÇÕES DO MODULO FUNCIONARIOS!
# TODO: ----------------------------

def cadastrar_funcionario(id, nome, salario, idade, funcao):

    funcionario = {
            'id': id,
            'nome': nome,
            'salario': salario,
            'idade': idade,
            'funcao': funcao
        }
    
    funcionarios.append(funcionario)

    print()
    print('FUNCIONÁRIO CADASTRADO COM SUCESSO')
    print()

    return funcionario

def listar_funcionarios():
    quantidade = len(funcionarios)
    
    if quantidade == 0:
        print('NENHUM FUNCIONÁRIO CADASTRADO')
        print()
                    
    else:
        for funcionario in funcionarios:
            print('ID', funcionario['id'], '|', 'nome: ', funcionario['nome'], '|',  'salario: ',  funcionario['salario'], '|', 'idade: ', funcionario['idade'], '|', 'função: ', funcionario['funcao'])
            print()

def editar_funcionario():
    id = int(input('Digite o ID do funcionário: '))
    print()

    encontrado = False

    for funcionario in funcionarios:
        

        if funcionario['id'] == id:
            
            print(
                'nome:', funcionario['nome'],
                '| salario:', funcionario['salario'],
                '| idade:', funcionario['idade'],
                '| função: ', funcionario['funcao']
            )
            print()


            print('OQUE DESEJA EDITAR? ')
            print()

            print('1- Nome')
            print('2- Salário')
            print('3- Idade')
            print('4- Função')

            escolha = int(
                input('Escolha uma opção: '
                    )
            )

            if escolha == 1:
                nome_editar = input('Digite o novo nome: ')
                funcionario['nome'] = nome_editar

            elif escolha == 2:
                salario_editar = float(input('Digite o novo salário: '))
                funcionario['salario'] = salario_editar

            elif escolha == 3:
                idade_editar = int(input('Digite a nova idade: '))
                funcionario['idade'] = idade_editar        

            elif escolha == 4:
                funcao_editar = input('Digite a nova função: ')
                funcionario['funcao'] = funcao_editar

            else:
                print('OPÇÃO INVÁLIDA!')
                return

            print()
            print('FUNCIONÁRIO EDITADO COM SUCESSO!')

    if encontrado == False:
        print('FUNCIONÁRIO NÃO ENCONTRADO!')
        print()

def excluir_funcionario():
    id = int(input('Digite o ID do fncionário: '))
    print()

    for funcionario in funcionarios:

        if funcionario['id'] == id:
            encontrado = True
        
            funcionarios.remove(funcionario)
            print('FUNCIONÁRIO DELETADO COM SUCESSO!')
            print()

        if encontrado == False:
            print('FUNCIONÁRIO NÃO ENCONTRADO!')
            print()

# TODO: ------------------------------------
# *! FIM DAS FUNÇÕES DO MODULO FUNCIONARIOS!
# TODO: ------------------------------------
    
def cadastrar_cliente(id, nome, cpf, telefone, email, ativo):
    cliente = {
        'id': id,
        'nome': nome,
        'cpf': cpf,
        'telefone': telefone,
        'email': email,
        'ativo': ativo
    }

    print()
    print('CLIENTE CADASTRADO COM SUCESSO!')
    print()

    clientes.append(cliente)

    return cliente

def listar_clientes():
    for cliente in clientes:
                    print('ID: ', cliente['id'], '|', 'nome: ', cliente['nome'], '|', 'CPF: ', cliente['cpf'], '|', 'Telefone: ', cliente['telefone'], '|', 'Email: ', cliente['email'], '|', 'ATIVO: ', cliente['ativo'])
                    print()
    
def editar_cliente():
    id = int(input('ID do cliente: '))
    print()
    
    encontrado = False
    
    for cliente in clientes:
    
        if cliente['id'] == id:

            print(
                'nome:', cliente['nome'],
                '| CPF:', cliente['cpf'],
                '| Telefone:', cliente['telefone'],
                '| Email:', cliente['email']
            )
            print()

            print('OQUE DESEJA EDITAR?')
            print()
            
            print('1- Nome')
            print('2- Cpf')
            print('3- Telefone')
            print('4- Email')
            print('5- Ativo')


            escolha = int(input('Escolha uma opção: '))
            print()

            if escolha == 1:
                novo_nome = input('Novo nome: ')
                cliente['nome'] = novo_nome

            elif escolha == 2:
                novo_cpf = input('Novo CPF: ex:(xxx.xxx.xxx-xx): ')
                cliente['cpf'] = novo_cpf

            elif escolha == 3:
                novo_telefone = input('Novo telefone ex: (xx) xxxxx-xxxx: ')
                cliente['telefone'] = novo_telefone

            elif escolha == 4:
                novo_email = input('Novo email ex:(xxx.@gmail.com): ')
                cliente['email'] = novo_email

            elif escolha == 5:
                print('1- Ativar')
                print('2- Desativar')
                print()

                escolha_ativo = int(input('Escolha ima opção: '))

                if escolha_ativo == 1:
                    cliente['ativo'] = True

                elif escolha_ativo == 2:
                    cliente['ativo'] = False
            print()

            print()
            print('CLIENTE ATUALIZADO COM SUCESSO!')
            print()

        if encontrado == False:
            print('CLIENTE NÃO ENCONTRADO!')
            print()

def excluir_cliente():
    id = int(input('ID do cliente: '))

    for cliente in clientes:
        
        if cliente['id'] == id:
            encontrado = True

            print('EXCLUIR CLIENTE DE ID: ', id,'?')
            print()

            print('1- Sim')
            print('2- Não')
            print()

            escolha = int(input('Escolha uma opção: '))
            print()

            if escolha == 1:
                clientes.remove(cliente)
                print('CLIENTE EXCLUIDO COM SUCESSO!')
                print()

            elif escolha == 2:
                print('OPERAÇÃO CANCELADA!')
                print()

            if encontrado == False:
                print('CLIENTE NÂO ENCONTRADO!')
                print()

    


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
        print('3- Editar Funcionário')
        print('4- Excluir Funcionário')
        print()

        escolha1 = int(
            input('Escolha uma opção: '
                  )
        )
        print()

        if escolha1 == 1:

            id = len(funcionarios) + 1

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

            print('-' *40)
            print('        FUNÇÕES DA EMPRESSA')
            print('-' * 40)
            print()

            print('1- Repositor')
            print('2- Caixa')
            print('3- Açougue')
            print('4- Gerente')

            escolha_funcao = int(input('escolha uma função: '))

            if escolha_funcao == 1:
                funcao = 'Repositor'

            elif escolha_funcao == 2:
                funcao = 'Caixa'

            elif escolha_funcao == 3:
                funcao =  'Açougue'

            elif escolha_funcao == 4:
                funcao = 'Gerente'

            else:
                print('OPÇÃO INVALIDA!')

            cadastrar_funcionario(id, nome, salario, idade, funcao)
    
                            
        elif escolha1 == 2:
            listar_funcionarios()

        elif escolha1 == 3:
            editar_funcionario()

        elif escolha1 == 4:
            excluir_funcionario()

           
        else:
            print('VOCÊ DIGITOU ERRADO!')
            print()

    elif escolha == 2:
        print('1- Cadastrar Cliente')
        print('2- Listar Clientes')
        print('3- Editar Cliente')
        print('4- Excluir CLiente')
        print()

        escolha2 = int(input('Escolha uma opção: '))
        print()

        if escolha2 == 1:

            id = len(clientes) + 1

            nome = input('Nome do cliente: ')
            cpf = input('CPF: ex:(xxx.xxx.xxx-xx): ')
            telefone = input('telefone ex:(xx) xxxxx-xxxx: ')
            email = input('Email: ex:(xxx.gmail.com): ')
            ativo = True

            cadastrar_cliente(id, nome, cpf, telefone, email, ativo)

        elif escolha2 == 2:
            listar_clientes()

        elif escolha2 == 3:
            editar_cliente()

        elif escolha2 == 4:
            excluir_cliente()

        else:
            print('OPÇÃO INVALIDA!')
            

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