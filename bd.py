class CustomException(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem
        super().__init__(mensagem)

def obterProdutoID(conbd,nome):
    myCursor = conbd.cursor()
    try:
        if(type(nome) != str):
            raise CustomException('O nome deve ser do tipo string')

        sql = "SELECT ID_Produto FROM Produtos WHERE Nome = %s"
        myCursor.execute(sql, (nome,))
        resultado = myCursor.fetchone()

        if resultado:
            return resultado[0]
        else:
            return None
    except Exception as e:
        print(f"Erro encontrado : {e}")
        return None
    finally:
         myCursor.close()


def cadastrarProdutos(conbd, nomeP, descricaoP, precoP, nomeC, descricaoC, qtd , nomeF , contatoF , enderecoF, temCategoria, temFornecedor):
    myCursor = conbd.cursor()

    if(type(nomeP) != str):
            raise CustomException('O nomeP deve ser do tipo string')
    
    if(type(descricaoP) != str):
            raise CustomException('A descricaoP deve ser do tipo string')
    
    if(type(precoP) != float):
            raise CustomException('O precoP deve ser do tipo number')
    
    if(type(nomeC) != str):
            raise CustomException('O nomeC deve ser do tipo string')
    
    if(type(descricaoC) != str):
            raise CustomException('a descricaoC deve ser do tipo string')
    
    if(type(qtd) != int):
            raise CustomException('a qtd deve ser do tipo string')
    
    if(type(nomeF) != int):
            raise CustomException('o nomeF deve ser do tipo string')

    if(type(contatoF) != int):
            raise CustomException('o contatoF deve ser do tipo string')
    
    if(type(enderecoF) != int):
            raise CustomException('o enderecoF deve ser do tipo string')
    
    if(type(temCategoria) != bool):
            raise CustomException('o temCategoria deve ser do tipo boolean')
    
    if(type(temFornecedor) != bool):
            raise CustomException('o temFornecedor deve ser do tipo boolean')

    categoria_id = ''
    fornecedor_id = ''

    try:
        if temCategoria == False:
            sql = "INSERT INTO categoriasprodutos(Nome, Descricao) VALUES (%s,%s)"
            valores = (nomeC, descricaoC, )
            myCursor.execute(sql,valores)
            categoria_id = myCursor.lastrowid
        else:
            sql = "SELECT ID_Categoria from categoriasprodutos WHERE Nome= %s"
            valores = (nomeC, )
            myCursor.execute(sql,valores)
            categoria_id = myCursor.fetchone()[0]
            
        if temFornecedor == False:
            sql = "INSERT INTO fornecedores(Nome,Contato,Endereco) VALUES (%s, %s, %s)"
            valores = (nomeF, contatoF, enderecoF)
            myCursor.execute(sql,valores)
            fornecedor_id = myCursor.lastrowid 
        else:
            sql = "SELECT ID_Fornecedor from fornecedores WHERE Nome= %s"
            valores = (nomeF, )
            myCursor.execute(sql,valores)
            fornecedor_id = myCursor.fetchone()[0]
        
        
        sql = "INSERT INTO produtos(Nome,Descricao,Preco,ID_Categoria,ID_Fornecedor) VALUES (%s, %s, %s, %s, %s)"
        valores = (nomeP, descricaoP, precoP, categoria_id, fornecedor_id)
        myCursor.execute(sql, valores)

        produto_id = myCursor.lastrowid

        sql2 = "INSERT INTO estoque(ID_Produto, Quantidade) VALUES(%s, %s)"
        valores2 = (produto_id, qtd)
        myCursor.execute(sql2,valores2)

        conbd.commit()
        
        print("Produto cadastrado com sucesso!")
        myCursor.close()
    except Exception as e:
        print(f"Algo deu errado: {e}" )

def listarProdutos(conbd):
    myCursor = conbd.cursor()
    try:
        sql = "SELECT * FROM produtos"
        myCursor.execute(sql)
        result = myCursor.fetchall()

        for i in result:
            print(i)  

    except Exception as e:
        print(f"Algo deu errado: {e}")
    finally:
        myCursor.close()

def atualizarProduto(conbd, nomeAntigo, nomeNovo, descricaoNova, precoNovo):
    myCursor = conbd.cursor()
    try:
        sql = "UPDATE produtos SET Nome = %s, Descricao = %s, Preco = %s WHERE Nome = %s"
        valores = (nomeNovo, descricaoNova, precoNovo, nomeAntigo)
        myCursor.execute(sql, valores)
        conbd.commit()
        print("Produto atualizado!")
    except Exception as e:
        print(f"Algo deu errado: {e}")
    finally:
        myCursor.close() 


def deletarProduto(conbd, nome):
    try:
        produto_id = obterProdutoID(conbd,nome)
        if not produto_id:
            return
    
        conbd.start_transaction()
        with conbd.cursor() as cursor:
            sql = 'DELETE FROM detalhespedido WHERE ID_Produto = %s'
            cursor.execute(sql,(produto_id,))

        with conbd.cursor() as cursor:
            sql = 'DELETE FROM estoque WHERE ID_Produto = %s'
            cursor.execute(sql,(produto_id,))
            
        with conbd.cursor() as cursor:
            sql = 'DELETE FROM precos WHERE ID_Produto = %s'
            cursor.execute(sql,(produto_id,))

        with conbd.cursor() as cursor:
            sql = 'DELETE FROM produtos WHERE ID_Produto = %s'
            cursor.execute(sql,(produto_id,))

        conbd.commit()
        print("Produto deleteado com sucesso")
    except Exception as e:
        conbd.rollback()
        print(f"Ocorreu um erro: {e}")
    finally:
        conbd.close()

def cadastrarFuncionarios(conbd, nome, departamento, cargo):
    myCursor = conbd.cursor()
    try:
        sql = "INSERT INTO funcionarios(Nome,Departamento,Cargo) VALUES (%s, %s, %s)"
        valores = (nome, departamento, cargo)
        myCursor.execute(sql, valores)
        conbd.commit()
        print("Funcionario cadastrado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        myCursor.close()


def listarFuncionarios(conbd):
    myCursor = conbd.cursor()
    try:
        sql = "SELECT * FROM funcionarios"
        myCursor.execute(sql)
        result = myCursor.fetchall()

        for i in result:
            print(i)

    except Exception as e:
         print(f"Algo deu errado: {e}")
    finally:
         myCursor.close()

def atualizarFuncionario(conbd, nomeAntigo, nomeNovo, cargoNovo, departamentoNovo):
    myCursor = conbd.cursor()
    try:
        sql = "UPDATE funcionarios SET Nome = %s, Cargo = %s, Departamento = %s WHERE Nome = %s"
        valores = (nomeNovo, cargoNovo, departamentoNovo, nomeAntigo)
        myCursor.execute(sql, valores)
        conbd.commit()
        print("Funcionario atualizado com sucesso")
    except Exception as e:
        print(f"Algo deu errado: {e}")
    finally:
        myCursor.close()


def deletarFuncionario(conbd, nome):
    myCursor = conbd.cursor()
    try:
        sql = "DELETE FROM funcionarios WHERE Nome = %s"
        valores = (nome, )
        myCursor.execute(sql, valores)
        conbd.commit()
        print("Funcionario deletado com sucesso") 
    except Exception as e:
        print(f"Algo deu errado: {e}")
    finally:
         myCursor.close()

def cadastrarClientes(conbd, nome, sobrenome, cidade, codigoPostal, endereco):
    myCursor = conbd.cursor()
    try:
        sql = "INSERT INTO clientes(Nome,Sobrenome,Cidade,CodigoPostal, Endereco) VALUES (%s, %s, %s, %s, %s)"
        valores = (nome, sobrenome, cidade, codigoPostal, endereco)
        myCursor.execute(sql, valores)
        conbd.commit()
        print("Cliente cadastrado com sucesso!")
    except Exception as e:
        print(f"Algo deu errado: {e}")
    finally:
        myCursor.close()

def listarClientes(conbd):
    myCursor = conbd.cursor()
    try:
        sql = "SELECT * FROM clientes"
        myCursor.execute(sql)
        result = myCursor.fetchall()

        for i in result:
            print(i)    
    except Exception as e:
        print(f"Algo deu errado: {e}")
    finally:
         myCursor.close()


def atualizarCliente(
    conbd,
    nomeAntigo,
    nomeNovo,
    sobrenomeNovo,
    cidadeNova,
    codigoPostalNovo,
    enderecoNovo,
):
    myCursor = conbd.cursor()
    try:
        sql = "UPDATE clientes SET Nome = %s, Sobrenome = %s, Cidade = %s, CodigoPostal = %s, Endereco = %s WHERE Nome = %s"
        valores = (
            nomeNovo,
            sobrenomeNovo,
            cidadeNova,
            codigoPostalNovo,
            enderecoNovo,
            nomeAntigo,
        )
        myCursor.execute(sql, valores)
        conbd.commit()
        print("Cliente atualizado com sucesso!")
    except Exception as e:
        print(f"Algo deu errado: {e}")
    finally:
        myCursor.close() 

def deletarCliente(conbd, nome):
    myCursor = conbd.cursor()
    try:
        sql = "DELETE FROM clientes WHERE Nome = %s"
        valores = (nome, ) 
        myCursor.execute(sql, valores)
        conbd.commit()
        print("Cliente excluido com sucesso")    
    except Exception as e:
        print(f"Algo deu errado: {e}")
    finally:
        myCursor.close()

def cadastrarFornecedores(conbd, nome, contato, endereco):
    myCursor = conbd.cursor()
    try:
        sql = "INSERT INTO fornecedores(Nome,Contato,Endereco) VALUES (%s, %s, %s)"
        valores = (nome, contato, endereco)
        myCursor.execute(sql, valores)
        conbd.commit()
        print("Fornecedor cadastrado com sucesso!")
    except Exception as e:
        print(f"Algo deu errado: {e}")
    finally:
        myCursor.close()


def listarFornecedores(conbd):
    myCursor = conbd.cursor()
    try:
        sql = "SELECT * FROM fornecedores"
        myCursor.execute(sql)
        result = myCursor.fetchall()

        for i in result:
            print(i)
    except Exception as e:
        print(f"Algo deu errado: {e}")
    finally:
        myCursor.close()


def atualizarFornecedor(conbd, nomeAntigo, nomeNovo, contatoNovo, enderecoNovo):
    myCursor = conbd.cursor()
    try:
        sql = (
            "UPDATE fornecedores SET Nome = %d, Contato = %s, Endereco = %s WHERE nome = %s"
        )
        valores = (conbd, nomeNovo, contatoNovo, enderecoNovo, nomeAntigo)
        myCursor.execute(sql, valores)
        conbd.commit()
        print("Fornecedor atualizado com sucesso!")
    except Exception as e:
        print(f"Algo deu errado: {e}")
    finally:
        myCursor.close()



def deletarFornecedor(conbd, nome):
    myCursor = conbd.cursor()
    try:
        sql = "DELETE FROM fornecedores WHERE Nome = %s"
        valores = nome
        myCursor.execute(sql, valores)
        conbd.commit()
        print("Fornecedor deletado com sucesso")
    except Exception as e:
        print(f"Algo deu errado: {e}")
    finally:
        myCursor.close()


def cadastrarPromacoes(conbd, nome, descricao, dataInicio, dataFim):
    myCursor = conbd.cursor()
    try:
        sql = "INSERT INTO promocoes(Nome,Descricao, DataInicio, DataFim) VALUES (%s, %s, %s, %s)"
        valores = (nome, descricao, dataInicio, dataFim)
        myCursor.execute(sql, valores)
        conbd.commit()
        print("Promoção cadastrado com sucesso!")
    except Exception as e:
        print(f"Algo deu errado: {e}")
    finally:
        myCursor.close()


def listarPromocoes(conbd):
    myCursor = conbd.cursor()
    try:
        sql = "SELECT * FROM promocoes"
        myCursor.execute(sql)
        result = myCursor.fetchall()

        for i in result:
            print(i)

    except Exception as e:
        print(f"Algo deu errado: {e}")
    finally:
        myCursor.close()


def atualizarPromocao(
    conbd, nomeAntigo, nomeNovo, novaDescricao, novaDataInicio, novaDataFim
):
    myCursor = conbd.cursor()
    try:
        sql = "UPDATE promocoes SET Nome = %s, Descricao = %s, DataInicio = %s, DataFim = %s WHERE Nome = %s"
        valores = (nomeNovo, novaDescricao, novaDataInicio, novaDataFim, nomeAntigo)
        myCursor.execute(sql, valores)
        conbd.commit()
        print("Promoção atualizada com sucesso!")
    except Exception as e:
        print(f"Algo deu errado: {e}")
    finally:
        myCursor.close()


def deletarPromocao(conbd, nome):
    myCursor = conbd.cursor()
    try:
        sql = "DELETE FROM promocoes WHERE Nome = %s"
        valores = (nome, )
        myCursor.execute(sql, valores)
        myCursor.commit()
        print("Promoção deletada com sucesso")
    except Exception as e:
        print(f"Algo deu errado: {e}")
    finally:
        myCursor.close()

def fazerPedido(conbd, nomeP, qtd, nomeC,sobrenomeC,cidadeC,codigoPostalC, enderecoC,clienteExiste,avaliacaoCA,comentarioCA,dataCA,dataP,metodoP):
    myCursor = conbd.cursor()
    try:
        id_produto = obterProdutoID(conbd, nomeP,)
        id_cliente = ''
    
        sqlPreco = "SELECT * FROM produtos WHERE ID_Produto = %s"
        valorPreco = (id_produto,)
        myCursor.execute(sqlPreco, valorPreco)
        preco = myCursor.fetchone()[3]

        total = preco * qtd

        if clienteExiste == False:
            sql = "INSERT INTO clientes(Cidade,CodigoPostal,Endereco,Nome,Sobrenome) VALUES (%s,%s,%s,%s,%s)"
            valores = (cidadeC, codigoPostalC, enderecoC, nomeC, sobrenomeC)
            myCursor.execute(sql, valores)
            id_cliente = myCursor.lastrowid
        else:
            sql = "SELECT * FROM clientes WHERE Nome = %s AND Sobrenome = %s"
            valores = (nomeC, sobrenomeC)
            myCursor.execute(sql, valores)
            id_cliente = myCursor.fetchone()[0]

        sql = "INSERT INTO pedidos(Data_Pedido, ID_Cliente, Total) VALUES(%s,%s,%s)"
        valores = (dataP, id_cliente, total)
        myCursor.execute(sql, valores)
        id_pedido = myCursor.lastrowid

        sql1 = "INSERT INTO detalhespedido(ID_Pedido, ID_Produto, Quantidade) VALUES(%s, %s, %s)"
        valores1 = (id_pedido, id_produto, qtd)
        myCursor.execute(sql1, valores1)

        sql2 = "INSERT INTO comentariosavaliacoes(Avaliacao,Comentario,Data,ID_Cliente,ID_Produto) VALUES (%s,%s,%s,%s,%s)"
        valores2 = (avaliacaoCA, comentarioCA, dataCA, id_cliente, id_produto)
        myCursor.execute(sql2, valores2)

        sql3 = "UPDATE estoque SET Quantidade = Quantidade - %s WHERE ID_Produto = %s"
        valores3 = (qtd, id_produto)
        myCursor.execute(sql3, valores3)

        sql4 = "INSERT INTO vendas(Data, ID_Cliente, MetodoPagamento, Total) VALUES(%s,%s,%s,%s)"
        valores4 = (dataP, id_cliente , metodoP, total)
        myCursor.execute(sql4, valores4)
        id_venda = myCursor.lastrowid

        sql5 = "INSERT INTO pagamentos(ID_Venda, Data, Valor) VALUES(%s,%s,%s)"
        valores5 = (id_venda, dataP, total)
        myCursor.execute(sql5, valores5)

        conbd.commit()
        print("Pedido feito com sucesso!")
    except Exception as e:
        print(f"Algo deu errado: {e}")
    finally:
        myCursor.close()