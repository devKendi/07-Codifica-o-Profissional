class Carro:
    def __init__(self, modelo, placa, ano, cor, quilometragem, valor_diario, observacao):
        self.modelo = modelo
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.quilometragem = quilometragem
        self.valor_diario = valor_diario
        self.observacao = observacao
        
class Esportivo(Carro):
    def __init__(self, modelo, placa, ano, cor, quilometragem, valor_diario, observacao, tempo, melhorias):
        super().__init__(modelo, placa, ano, cor, quilometragem, valor_diario, observacao)
        self.tempo = melhorias

class Utilitario(Carro):
    def __init__(self, modelo, placa, ano, cor, quilometragem, valor_diario, observacao, quantidade_passageiros, tamanho_bagageiro, km_litro):
        super().__init__(modelo, placa, ano, cor, quilometragem, valor_diario, observacao)
        self.quantidade_passageiros = quantidade_passageiros
        self.tamanho_bagageiro = tamanho_bagageiro
        self.km_litro = km_litro
        
class Reserva:
    def __init__(self, cpf_cliente, status, dt_inicio, dt_fim):
        self.cpf_cliente = cpf_cliente
        self.status = status
        self.dt_inicio = dt_inicio
        self.dt_fim = dt_fim
        
class Pessoa:
    def __init__(self, nome, cpf, emal, telefone, endereco):
        self.nome = nome
        self.cpf = cpf
        self.emal = emal
        self.telefone = telefone
        self.endereco = endereco

    def get_exibePessoa(self):
        print("O valor de self é: ", self)


        print(('Nome do cliente: %s') % self.nome)
        print(('CPF do cliente: %s') % self.cpf)
        print(('E-mail do cliente: %s') % self.emal)
        print(('Telefone do cliente: %s') % self.telefone)
        print(('Endereço completo  do cliente: %s') % self.endereco)

    def get_Pessoa_nome(self):
        return self.nome
    
    def get_Pessoa_cpf(self):
        return self.cpf
    
    def get_Pessoa_emal(self):
        return self.emal
    
    def get_Pessoa_telefone(self):
        return self.telefone
    
    def get_Pessoa_endereco(self):
        return self.endereco

        
class Funcionario(Pessoa):
    def __init__(self, nome, cpf, emal, telefone, endereco, idade, dt_contratacao, salario, qd_alugueis_mes = 0, status = False):
        super().__init__(nome, cpf, emal, telefone, endereco)
        self.idade = idade
        self.dt_contratacao = dt_contratacao
        self.salario = salario
        self.qd_alugueis_mes = qd_alugueis_mes
        self.status = status
          
class Cliente(Pessoa):
    def __init__(self, nome, cpf, emal, telefone, endereco, dt_nascimento, nu_carteira, foto_carteira, dt_vencimento_carteira):
        super().__init__(nome, cpf, emal, telefone, endereco)
        self.nome = nome
        self.cpf = cpf
        self.emal = emal
        self.telefone = telefone
        self.endereco = endereco
        
        self.dt_nascimento = dt_nascimento
        self.nu_carteira = nu_carteira
        self.foto_carteira = foto_carteira
        self.dt_vencimento_carteira = dt_vencimento_carteira
    
    def get_Exibe_cliente(self):
        print(('Nome do cliente: %s') % self.nome)
        print(('CPF do cliente: %s') % self.cpf)
        print(('E-mail do cliente: %s') % self.emal)
        print(('Telefone do cliente: %s') % self.telefone)
        print(('Endereço completo do cliente: %s') % self.endereco)
        print(('Data de nascimento do cliente: %s') % self.dt_nascimento)
        print(('Número da habilitação do cliente: %s') % self.nu_carteira)
        print(('Foto da habilitação do cliente: %s') % self.foto_carteira)
        print(('Data de vencimento da habilitação do cliente: %s') % self.dt_vencimento_carteira)
       
    def get_cliente_dt_nascimento(self):
        return self.dt_nascimento
    
    def get_cliente_nu_carteira(self):
        return self.nu_carteira
    
    def get_cliente_foto_carteira(self):
        return self.foto_carteira
    
    def get_cliente_dt_vencimento_carteira(self):
        return self.dt_vencimento_carteira

      
class Promocao:
    def __init__(self, titulo, descricao, dt_validade):
        self.titulo = titulo
        self.descricao = descricao
        self.dt_validade = dt_validade

if ((input("\nDeseja criar nova pessoa? S para sim: ") == 's')):
    # Coleta dados de pessoa nova
    nome = input("\n\nDigite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    emal = input("Digite o e-mail do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    endereco = input("Digite o endereço completo  do cliente: ")

    # Cria pessoa nova
    pessoaNova = Pessoa(nome, cpf, emal, telefone, endereco)
else:
     print("Aplicação em desenvolvimento\n")

if ((input("\n\nDeseja confirmar, na tela, a nova pessoa? S para sim: ") == 's')):
    pessoaNova.get_exibePessoa()
else:
     print("Aplicação em desenvolvimento\n")

if ((input("\nDeseja criar novo cliente? S para sim: ") == 's')):
    if (pessoaNova.get_Pessoa_cpf() == ""):
        print("Dados insuficientes não é possível criar novo cliente!\n\n")
    else:
        nome = pessoaNova.get_Pessoa_nome()
        cpf = pessoaNova.get_Pessoa_cpf()
        emal = pessoaNova.get_Pessoa_emal()
        telefone = pessoaNova.get_Pessoa_telefone()
        endereco = pessoaNova.get_Pessoa_endereco()
        dt_nascimento = input("Digite a data de nascimento  do cliente: ")
        nu_carteira = input("Digite o número da carteira de motorista do cliente: ")
        foto_carteira = input("Insira a foto da carteira de motorista do cliente: ")
        dt_vencimento_carteira = input("Digite a data de vencimento da carteira de motorista do cliente: ")
        novoCliente = Cliente(nome, cpf, emal, telefone, endereco, dt_nascimento, nu_carteira, foto_carteira, dt_vencimento_carteira)

        if ((input("\n\nDeseja confirmar, na tela, o novo cliente? S para sim: ") == 's')):
            novoCliente.get_Exibe_cliente()

else:
     print("Aplicação em desenvolvimento")