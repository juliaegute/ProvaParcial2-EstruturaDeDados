
class Pendencia:
    def __init__(self, local, descricao, tempo, prioridade):
        self.local = local
        self.descricao = descricao
        self.tempo = tempo
        self.prioridade = prioridade

    def __str__(self):
        return f"Local: {self.local} | Pendência: {self.descricao} | Tempo: {self.tempo} min | Prioridade: {self.prioridade}"


class No:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None


class Lista:
    def __init__(self):
        self.inicio = None   
        self.fim = None     
        self.atual = None    
        self.tamanho = 0    

    def inserir_final(self, valor):
        novo = No(valor)

        if self.tamanho == 0:
            self.inicio = novo
            self.fim = novo
            self.atual = novo

        else:
            self.fim.dir = novo
            novo.esq = self.fim
            self.fim = novo
            self.atual = novo

        self.tamanho += 1

    def inserir_apos_atual(self, valor):
        novo = No(valor)

        if self.tamanho == 0:
            self.inicio = novo
            self.fim = novo
            self.atual = novo

        elif self.atual == self.fim:
            self.fim.dir = novo
            novo.esq = self.fim
            self.fim = novo
            self.atual = novo

        else:
            proximo = self.atual.dir

            self.atual.dir = novo
            novo.esq = self.atual

            novo.dir = proximo
            proximo.esq = novo

            self.atual = novo

        self.tamanho += 1

    def avancar(self):
        if self.atual is not None and self.atual.dir is not None:
            self.atual = self.atual.dir
            print("\nAvançando para:")
            print(self.atual.dado)
        else:
            print("\nNão existe próximo ponto de vistoria.")

    def voltar(self):
        if self.atual is not None and self.atual.esq is not None:
            self.atual = self.atual.esq
            print("\nVoltando para:")
            print(self.atual.dado)
        else:
            print("\nNão existe ponto de vistoria anterior.")

    def exibir_atual(self):
        if self.atual is not None:
            print("\nPonto atual da vistoria:")
            print(self.atual.dado)
        else:
            print("\nNenhuma pendência cadastrada.")

    def remover_atual(self):
        if self.atual is None:
            print("\nNão há ponto atual para remover.")
            return

        removido = self.atual

        if self.tamanho == 1:
            self.inicio = None
            self.fim = None
            self.atual = None

        elif removido == self.inicio:
            self.inicio = removido.dir
            self.inicio.esq = None
            self.atual = self.inicio
            removido.dir = None

        elif removido == self.fim:
            self.fim = removido.esq
            self.fim.dir = None
            self.atual = self.fim
            removido.esq = None

        else:
            anterior = removido.esq
            proximo = removido.dir

            anterior.dir = proximo

            proximo.esq = anterior

            self.atual = proximo

            removido.esq = None
            removido.dir = None

        self.tamanho -= 1
        print("\nPendência removida com sucesso.")

    def exibir_roteiro(self):
        aux = self.inicio

        if self.tamanho == 0:
            print("\nRoteiro vazio.")
        else:
            print("\nRoteiro completo da vistoria:")

            while aux:
                if aux == self.atual:
                    print("-> ATUAL:", aux.dado)
                else:
                    print("          ", aux.dado)

                aux = aux.dir

    def calcular_tempo_total(self):
        aux = self.inicio
        soma = 0

        while aux:
            soma = soma + aux.dado.tempo
            aux = aux.dir

        return soma

    def contar_prioridade_alta(self):
        aux = self.inicio
        contador = 0

        while aux:
            if aux.dado.prioridade == "alta":
                contador += 1

            aux = aux.dir

        return contador


def cadastrar_pendencia():
    local = input("Nome do local vistoriado: ")
    descricao = input("Descrição da pendência: ")
    tempo = int(input("Tempo estimado de correção em minutos: "))
    prioridade = input("Prioridade (baixa, média ou alta): ")

    return Pendencia(local, descricao, tempo, prioridade)

def menu():
    print("\n--- ROTEIRO DE VISTORIA TÉCNICA ---")
    print("[1] Cadastrar nova pendência no final do roteiro")
    print("[2] Inserir nova pendência após o ponto atual")
    print("[3] Avançar para o próximo ponto")
    print("[4] Voltar para o ponto anterior")
    print("[5] Exibir ponto atual")
    print("[6] Remover ponto atual")
    print("[7] Exibir todo o roteiro")
    print("[8] Calcular tempo total de correção")
    print("[9] Contar pendências com prioridade alta")
    print("[10] Encerrar")


# Programa principal
def main():
    roteiro = Lista()

    while True:
        menu()
        opcao = int(input("Escolha uma opção: "))

        match opcao:

            case 1:
                pendencia = cadastrar_pendencia()
                roteiro.inserir_final(pendencia)
                print("\nPendência cadastrada no final do roteiro.")

            case 2:
                pendencia = cadastrar_pendencia()
                roteiro.inserir_apos_atual(pendencia)
                print("\nPendência inserida após o ponto atual.")

            case 3:
                roteiro.avancar()

            case 4:
                roteiro.voltar()

            case 5:
                roteiro.exibir_atual()

            case 6:
                roteiro.remover_atual()

            case 7:
                roteiro.exibir_roteiro()

            case 8:
                total = roteiro.calcular_tempo_total()
                print(f"\nTempo total estimado de correção: {total} minutos")

            case 9:
                qtd = roteiro.contar_prioridade_alta()
                print(f"\nQuantidade de pendências com prioridade alta: {qtd}")

            case 10:
                print("\nPrograma encerrado.")
                break

            case _:
                print("\nOpção inválida.")


if __name__ == "__main__":
    main()