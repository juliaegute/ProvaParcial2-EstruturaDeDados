from collections import deque 

class Bobina:
    def __init__(self, codigo: str, peso: float, tempo: int):
        self.codigo = codigo
        self.peso = peso
        self.tempo = tempo

    def __str__(self):
        return f"Código: {self.codigo} | Peso: {self.peso} toneladas | Tempo: {self.tempo} segundos"

def push(pilha, bobina):
    pilha.append(bobina)

def pop(pilha):
    if not pilha:
        return None

    return pilha.pop()

def calcular_peso_total(pilha):
    total = 0

    for bobina in pilha:
        total = total + bobina.peso

    return total

def calcular_tempo_total(pilha):
    total = 0

    for bobina in pilha:
        total = total + bobina.tempo

    return total


def exibir_pilha(pilha):
    if not pilha:
        print("\nFosso vazio.")
    else:
        print("\nEstado atual do fosso:")
        print("PORTA / TOPO")
        print("↓")

        i = len(pilha) - 1

        while i >= 0:
            print(pilha[i])
            i = i - 1

        print("↓")
        print("FUNDO / BASE")


def gerar_menu():
    print("\n>>>>>>>>> MENU <<<<<<<<<")
    print("[1] Guardar bobina")
    print("[2] Retirar bobina")
    print("[3] Consultar próxima bobina a sair")
    print("[4] Inspecionar fosso")
    print("[5] Exibir resumo do fosso")
    print("[6] Finalizar")


# programa principal

pilha = deque()

peso_retirado = 0

tempo_liberado = 0

while True:
    gerar_menu()
    opcao = int(input("Escolha uma opção: "))
    match opcao:

        case 1:
            codigo = input("Informe o código da bobina: ")
            peso = float(input("Informe o peso da bobina em toneladas: "))
            tempo = int(input("Informe o tempo de movimentação em segundos: "))

            bobina = Bobina(codigo, peso, tempo)

            push(pilha, bobina)

            print("\nBobina guardada com sucesso!")
            exibir_pilha(pilha)

        case 2:
            bobina = pop(pilha)

            if bobina is None:
                print("\nNão é possível retirar. O fosso está vazio.")
            else:
                peso_retirado = peso_retirado + bobina.peso
                tempo_liberado = tempo_liberado + bobina.tempo

                print("\nBobina retirada:")
                print(bobina)
                print(f"Tempo liberado com essa retirada: {bobina.tempo} segundos")

                exibir_pilha(pilha)

        case 3:
            if not pilha:
                print("\nO fosso está vazio. Não existe bobina na porta.")
            else:
                print("\nPróxima bobina a sair:")
                print(pilha[-1])

        case 4:
            exibir_pilha(pilha)

        case 5:
            print("\nResumo do fosso:")
            print(f"Bobinas armazenadas: {len(pilha)}")
            print(f"Peso total armazenado: {calcular_peso_total(pilha)} toneladas")
            print(f"Tempo total de movimentação das bobinas armazenadas: {calcular_tempo_total(pilha)} segundos")
            print(f"Peso total retirado: {peso_retirado} toneladas")
            print(f"Tempo total liberado nas retiradas: {tempo_liberado} segundos")

        case 6:
            print("\nResumo final:")
            print(f"Bobinas armazenadas ao final: {len(pilha)}")
            print(f"Peso total armazenado: {calcular_peso_total(pilha)} toneladas")
            print(f"Tempo total das bobinas armazenadas: {calcular_tempo_total(pilha)} segundos")
            print(f"Peso total retirado: {peso_retirado} toneladas")
            print(f"Tempo total liberado nas retiradas: {tempo_liberado} segundos")
            print("\nPrograma finalizado.")
            break

        case _:
            print("\nOpção inválida.")