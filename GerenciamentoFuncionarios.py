class GerenciadorDeFuncionarios:
    def __init__(self):
        self.funcionarios = {}  # Dicionário para armazenar os funcionários

    def adicionar_funcionario(self, id, nome, cargo, salario):
        """Método para adicionar um novo funcionário ao dicionário."""
        if id in self.funcionarios:
            print("Funcionário com este ID já existe.")
        else:
            # Adiciona um novo funcionário ao dicionário de funcionários
            self.funcionarios[id] = {
                'nome': nome,
                'cargo': cargo,
                'salário': salario
            }
            print("Funcionário adicionado com sucesso.")

    def remover_funcionario(self, id):
        """Método para remover um funcionário do dicionário."""
        if id in self.funcionarios:
            del self.funcionarios[id]  # Remove o funcionário pelo ID
            print("Funcionário removido com sucesso.")
        else:
            print("Funcionário não encontrado.")

    def atualizar_funcionario(self, id, nome=None, cargo=None, salario=None):
        """Método para atualizar as informações de um funcionário."""
        if id in self.funcionarios:
            # Atualiza as informações do funcionário se os novos valores forem fornecidos
            if nome:
                self.funcionarios[id]['nome'] = nome
            if cargo:
                self.funcionarios[id]['cargo'] = cargo
            if salario:
                self.funcionarios[id]['salário'] = salario
            print("Informações do funcionário atualizadas com sucesso.")
        else:
            print("Funcionário não encontrado.")

    def visualizar_funcionario(self, id):
        """Método para exibir as informações de um funcionário."""
        if id in self.funcionarios:
            # Exibe as informações do funcionário pelo ID
            funcionario = self.funcionarios[id]
            print(f"ID: {id}")
            print(f"Nome: {funcionario['nome']}")
            print(f"Cargo: {funcionario['cargo']}")
            print(f"Salário: {funcionario['salário']}")
        else:
            print("Funcionário não encontrado.")

    def listar_funcionarios(self):
        """Método para listar todos os funcionários cadastrados."""
        if not self.funcionarios:
            print("Nenhum funcionário cadastrado.")
        else:
            # Percorre o dicionário de funcionários e exibe as informações de cada um
            for id, detalhes in self.funcionarios.items():
                print(f"ID: {id}, Nome: {detalhes['nome']}, Cargo: {detalhes['cargo']}, Salário: {detalhes['salário']}")


def main():
    gerenciador = GerenciadorDeFuncionarios()  # Instancia a classe GerenciadorDeFuncionarios

    while True:
        print("\nMenu:")
        print("1. Adicionar Funcionário")
        print("2. Remover Funcionário")
        print("3. Atualizar Funcionário")
        print("4. Visualizar Funcionário")
        print("5. Listar Funcionários")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")  # Solicita ao usuário escolher uma opção do menu

        if escolha == '1':  # Opção para adicionar funcionário
            id = int(input("Digite o ID do funcionário: "))
            nome = input("Digite o nome do funcionário: ")
            cargo = input("Digite o cargo do funcionário: ")
            salario = float(input("Digite o salário do funcionário: "))
            gerenciador.adicionar_funcionario(id, nome, cargo, salario)

        elif escolha == '2':  # Opção para remover funcionário
            id = int(input("Digite o ID do funcionário a ser removido: "))
            gerenciador.remover_funcionario(id)

        elif escolha == '3':  # Opção para atualizar informações de funcionário
            id = int(input("Digite o ID do funcionário a ser atualizado: "))
            nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ")
            cargo = input("Digite o novo cargo (ou pressione Enter para manter o atual): ")
            salario = input("Digite o novo salário (ou pressione Enter para manter o atual): ")
            gerenciador.atualizar_funcionario(
                id,
                nome if nome else None,
                cargo if cargo else None,
                float(salario) if salario else None
            )

        elif escolha == '4':  # Opção para visualizar informações de funcionário
            id = int(input("Digite o ID do funcionário a ser visualizado: "))
            gerenciador.visualizar_funcionario(id)

        elif escolha == '5':  # Opção para listar todos os funcionários
            gerenciador.listar_funcionarios()

        elif escolha == '6':  # Opção para sair do programa
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")  # Mensagem para opções inválidas


if __name__ == "__main__":
    main()  # Chama a função principal ao executar o script
