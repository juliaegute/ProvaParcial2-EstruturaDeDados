from collections import deque

class Solicitacao:
    def __init__(self, aluno: str, peca: str, tempo: int, custo: float):
        self.aluno = aluno
        self.peca = peca
        self.tempo = tempo
        self.custo = custo

    def __str__(self):
        return f"Aluno: {self.aluno} | Peça: {self.peca} | Tempo: {self.tempo} min | Custo: R$ {self.custo:.2f}"


def enqueue(fila, solicitacao):
    fila.append(solicitacao)

def dequeue(fila):
    if not fila:
        return None

    return fila.popleft()

def exibir_fila(fila):
    if not fila:
        print("\nFila vazia.")
    else:
        print("\nEstado atual da fila de impressão:")
        print("INÍCIO DA FILA")

        for solicitacao in fila:
            print(solicitacao)

        print("FIM DA FILA")

def cadastrar_solicitacao(fila):
    aluno = input("Informe o nome do aluno: ")
    peca = input("Informe o nome da peça: ")
    tempo = int(input("Informe o tempo estimado de impressão em minutos: "))
    custo = float(input("Informe o custo do material: R$ "))

    solicitacao = Solicitacao(aluno, peca, tempo, custo)

    enqueue(fila, solicitacao)

    print("\nSolicitação cadastrada com sucesso!")


def imprimir_proxima(fila):
    solicitacao = dequeue(fila)

    if solicitacao is None:
        print("\nNão há solicitações na fila.")
        return None

    print("\nPeça impressa:")
    print(solicitacao)

    return solicitacao


def gerar_menu():
    print("\n>>>>>> MENU <<<<<<")
    print("[1] Cadastrar solicitação de impressão")
    print("[2] Imprimir próxima peça")
    print("[3] Exibir fila de impressão")
    print("[4] Exibir resumo das impressões")
    print("[5] Finalizar")


# programa principal

def main():
    fila = deque()

    total_impressoes = 0
    tempo_total = 0
    custo_total = 0

    while True:
        gerar_menu()
        opcao = int(input("Escolha uma opção: "))

        match opcao:
            case 1:
                cadastrar_solicitacao(fila)

            case 2:
                solicitacao = imprimir_proxima(fila)

                if solicitacao is not None:
                    total_impressoes = total_impressoes + 1
                    tempo_total = tempo_total + solicitacao.tempo
                    custo_total = custo_total + solicitacao.custo

            case 3:
                exibir_fila(fila)

            case 4:
                print(f"\nTotal de peças impressas: {total_impressoes}")
                print(f"Tempo total de impressão: {tempo_total} minutos")
                print(f"Custo total de material: R$ {custo_total:.2f}")

            case 5:
                print("\nPrograma finalizado.")
                break

            case _:
                print("\nOpção inválida.")


if __name__ == "__main__":
    main()