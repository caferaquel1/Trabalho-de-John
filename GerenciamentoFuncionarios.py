class GerenciadorDeFuncionarios:
    def __init__(self):
        self.funcionarios = {}

    def adicionar_funcionario(self, id, nome, cargo, salario):
        if id in self.funcionarios:
            print("Funcionário com este ID já existe.")
        else:
            self.funcionarios[id] = {
                'nome': nome,
                'cargo': cargo,
                'salário': salario
            }
            print("Funcionário adicionado com sucesso.")

    def remover_funcionario(self, id):
        if id in self.funcionarios:
            del self.funcionarios[id]
            print("Funcionário removido com sucesso.")
        else:
            print("Funcionário não encontrado.")

    def atualizar_funcionario(self, id, nome=None, cargo=None, salario=None):
        if id in self.funcionarios:
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
        if id in self.funcionarios:
            funcionario = self.funcionarios[id]
            print(f"ID: {id}")
            print(f"Nome: {funcionario['nome']}")
            print(f"Cargo: {funcionario['cargo']}")
            print(f"Salário: {funcionario['salário']}")
        else:
            print("Funcionário não encontrado.")

    def listar_funcionarios(self):
        if not self.funcionarios:
            print("Nenhum funcionário cadastrado.")
        else:
            for id, detalhes in self.funcionarios.items():
                print(f"ID: {id}, Nome: {detalhes['nome']}, Cargo: {detalhes['cargo']}, Salário: {detalhes['salário']}")

def main():
    gerenciador = GerenciadorDeFuncionarios()

    while True:
        print("\nMenu:")
        print("1. Adicionar Funcionario")
        print("2. Remover Funcionario")
        print("3. Atualizar Funcionario")
        print("4. Visualizar Funcionario")
        print("5. Listar Funcionarios")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            id = int(input("Digite o ID do funcionário: "))
            nome = input("Digite o nome do funcionário: ")
            cargo = input("Digite o cargo do funcionário: ")
            salario = float(input("Digite o salário do funcionário: "))
            gerenciador.adicionar_funcionario(id, nome, cargo, salario)


        elif escolha == '2':
            id = int(input("Digite o ID do funcionário a ser removido: "))
            gerenciador.remover_funcionario(id)

        elif escolha == '3':
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

        elif escolha == '4':
            id = int(input("Digite o ID do funcionário a ser visualizado: "))
            gerenciador.visualizar_funcionario(id)

        elif escolha == '5':
            gerenciador.listar_funcionarios()

        elif escolha == '6':
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()