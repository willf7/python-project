from conexaoBd import connect
from bd import *
from datetime import datetime, date

conbd = connect()

while True:
    print(
        "1. Produtos 2. Funcionarios 3. Clientes 4. Fornecedores 5. Promoção 6. Fazer pedido 7.Finalizar programa"
    )
    choice = int(input("Digite sua escolha: "))
    if choice == 1:
        while True:
            print("1. Criar 2. Listar 3. Editar 4. Deletar 5. Voltar ao inicio")
            choiceProduto = int(input("Digite sua escolha: "))
            if choiceProduto == 1:
                nomeP = input("Digite o nome: ")
                descricaoP = input("Digite a descrição: ")
                precoP = int(input("Digite o preco: "))
                qtd = int(input("Digite a quantidade do produto: "))
                temC = int(input("1. Criar categoria 2. Adicionar existente"))
                if temC == 1:
                    nomeC = input("Digite o nome da categoria: ")
                    descricaoC = input("Digite a descrição da categoria: ")
                    temCBool = False
                elif temC == 2:
                    nomeC = input("Digite o nome da categoria: ")
                    descricaoC = ''
                    temCBool = True
                temF = int(input("1. Criar fornecedor 2. Adicionar existente: "))
                if temF == 1:
                    nomeF = input("Digite o nome do fornecedor: ")
                    contatoF = input("Digite o contato: ")
                    enderecoF = input("Digite o endereço: ")
                    temFBool = False
                elif temF == 2:
                    nomeF = input("Digite o nome do fornecedor: ")
                    contatoF = ""
                    enderecoF = ""
                    temFBool = True
                cadastrarProdutos(conbd, nomeP, descricaoP, precoP, nomeC, descricaoC, qtd, nomeF, contatoF, enderecoF, temCBool, temFBool)
            elif choiceProduto == 2:
                listarProdutos(conbd)
            elif choiceProduto == 3:
                nomeAntigo = input("Digite o nome do produto que você deseja editar: ")
                nomeNovo = input("Digite o novo nome: ")
                novaDescricao = input("Digite a nova descrição: ")
                novoPreco = int(input("Digite o novo preço: "))
                atualizarProduto(conbd, nomeAntigo, nomeNovo, novaDescricao, novoPreco)
            elif choiceProduto == 4:
                nome = input("Digite o nome do produto que você deseja deletar: ")
                deletarProduto(conbd, nome)
            elif choiceProduto == 5:
                break
    elif choice == 2:
        while True:
            print("1. Criar 2. Listar 3. Editar 4. Deletar 5. Voltar ao inicio")
            choiceFuncionario = int(input("Digite sua escolha: "))
            if choiceFuncionario == 1:
                nome = input("Digite o nome: ")
                departamento = input("Digite o departamento: ")
                cargo = input("Digite o cargo: ")
                cadastrarFuncionarios(conbd, nome, departamento, cargo)
            elif choiceFuncionario == 2:
                listarFuncionarios(conbd)
            elif choiceFuncionario == 3:
                nomeAntigo = input(
                    "Digite o nome do Funcionario que você deseja editar: "
                )
                nomeNovo = input("Digite o nome novo: ")
                cargoNovo = input("Digite o cargo novo: ")
                departamentoNovo = input("Digite o departamento novo: ")
                atualizarFuncionario(
                    conbd, nomeAntigo, nomeNovo, cargoNovo, departamentoNovo
                )
            elif choiceFuncionario == 4:
                nome = input("Digite o nome do funcionario que você deseja deletar: ")
                deletarProduto(conbd, nome)
            elif choiceFuncionario == 5:
                break
    elif choice == 3:
        while True:
            print("1. Criar 2. Listar 3. Editar 4. Deletar 5. Voltar ao inicio")
            choiceCliente = int(input("Digite sua escolha: "))
            if choiceCliente == 1:
                nome = input("Digite o nome: ")
                sobrenome = input("Digite o sobrenome: ")
                cidade = input("Digite a cidade: ")
                codigoPostal = input("Digite o codigo postal: ")
                endereco = input("Digite o endereço: ")
                cadastrarClientes(
                    conbd, nome, sobrenome, cidade, codigoPostal, endereco
                )
            elif choiceCliente == 2:
                listarClientes(conbd)
            elif choiceCliente == 3:
                nomeAntigo = input("Digite o nome do cliente que você deseja editar: ")
                nomeNovo = input("Digite o novo nome: ")
                sobrenomeNovo = input("Digite o novo sobrenome: ")
                cidadeNova = input("Digite a cidade nova: ")
                codigoPostalNovo = input("Digite o novo codigo postal: ")
                enderecoNovo = input("Digite o novo endereço: ")
                atualizarCliente(
                    conbd,
                    nomeAntigo,
                    nomeNovo,
                    sobrenomeNovo,
                    cidadeNova,
                    codigoPostalNovo,
                    enderecoNovo,
                )
            elif choiceCliente == 4:
                nomeExcluir = input("Digite o nome do cliente que você deseja deletar: ")
                deletarCliente(conbd, nomeExcluir)
            elif choiceCliente == 5:
                break
    elif choice == 4:
        while True:
            print("1. Criar 2. Listar 3. Editar 4. Deletar 5. Voltar ao inicio")
            choiceFornecedor = int(input("Digite sua escolha: "))
            if choiceFornecedor == 1:
                nome = input("Digite o nome: ")
                contato = input("Digite o contato: ")
                endereco = input("Digite o endereco: ")
                cadastrarFornecedores(conbd, nome, contato, endereco)
            elif choiceFornecedor == 2:
                listarFornecedores(conbd)
            elif choiceFornecedor == 3:
                nomeAntigo = input(
                    "Digite o nome do fornecedor que você deseja alterar: "
                )
                contatoNovo = input("Digite o novo contato: ")
                enderecoNovo = input("Digite o endereço novo: ")
                atualizarFornecedor(
                    conbd, nomeAntigo, nomeNovo, contatoNovo, enderecoNovo
                )
            elif choiceFornecedor == 4:
                nome = input("Digite o nome do fornecedor que você deseja deletar: ")
                deletarFornecedor(conbd, nome)
            elif choiceFornecedor == 5:
                break
    elif choice == 5:
        while True:
            print("1. Criar 2. Listar 3. Editar 4. Deletar 5. Voltar ao inicio")
            choicePromocao = int(input("Digite sua escolha: "))
            if choicePromocao == 1:
                nome = input("Digite o nome: ")
                descricao = input("Digite a descricao DD-MM-AAAA :")
                dataInicio = input("Digite a data do inicio: ")
                dataInicio= datetime.strptime(dataInicio, "%d-%m-%Y").strftime("%Y-%m-%d")
                dataFim = input("Digite a data do fim DD-MM-AAAA :")
                dataFim= datetime.strptime(dataFim, "%d-%m-%Y").strftime("%Y-%m-%d")
                cadastrarPromacoes(conbd, nome, descricao, dataInicio, dataFim)
            elif choicePromocao == 2:
                listarPromocoes()
            elif choicePromocao == 3:
                nomeAntigo = input("Digite o nome do usuario que você deseja editar: ")
                novoNome = input("Digite o novo nome: ")
                novaDescricao = input("Digite a nova descrição: ")
                novaDataInicio = input("Digite a nova data de inicio: ")
                novaDataFim = input("Digite a nova data de inicio: ")
                atualizarPromocao(
                    conbd,
                    nomeAntigo,
                    nomeNovo,
                    novaDescricao,
                    novaDataInicio,
                    novaDataFim,
                )
            elif choicePromocao == 4:
                nome = input("Digite o nome da promoção que você deseja deletar: ")
                deletarPromocao(conbd, nome)
            elif choicePromocao == 5:
                break
    elif choice == 6:
        while True:
            nomeP = input("Digite o nome do produto: ")
            qtd = int(input("Digite a quantidade dos produtos: "))
            dataP = input("Digite a data do pedido DD-MM-AAAA : ")
            dataP = datetime.strptime(dataP, "%d-%m-%Y").strftime("%Y-%m-%d")
            clienteExiste = int(input("1. Cadastrar cliente 2. Cliente existente: "))
            if clienteExiste == 1:
                clienteExBool = False
                nomeC = input("Digite o nome do cliente: ")
                sobrenomeC = input("Digite o sobrenome do cliente: ")
                cidadeC = input("Digite a cidade do cliente: ")
                codigoPostalC = input("Digite o codigo postal do cliente: ")
                enderecoC = input("Digite o endereço do cliente: ")
            elif clienteExiste == 2:
                clienteExBool = True
                nomeC = input("Digite o nome do cliente: ")
                sobrenomeC = input("Digite o sobrenome do cliente: ")
                cidadeC = ''
                codigoPostalC = ''
                enderecoC = ''
            dataV = input("Digite a data da venda DD-MM-AAAA : ")
            dataV = datetime.strptime(dataV, "%d-%m-%Y").strftime("%Y-%m-%d")
            metodoP = input("Digite o metodo do pagamento: ")
            avaliacaoCA = int(input("Digite a avaliação de 1 a 5: "))
            comentarioCA = input("Digite o comentario do cliente: ")
            dataCA = input("Digite a data do comentario DD-MM-AAAA : ")
            dataCA = datetime.strptime(dataCA, "%d-%m-%Y").strftime("%Y-%m-%d")
            fazerPedido(conbd,nomeP,qtd,nomeC,sobrenomeC,cidadeC,codigoPostalC,enderecoC,clienteExBool,avaliacaoCA,comentarioCA,dataCA,dataP, metodoP)            
    elif choice == 7:
        print("Finalizando o programa...")
        break
