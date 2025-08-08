#!/usr/bin/env python3
"""
Arquivo principal para testar a implementação da Fila Circular.
"""

from queue import FilaCircular


def imprimir_separador(titulo):
    """Imprime um separador visual com título."""
    print(f"\n{'=' * 50}")
    print(f" {titulo}")
    print(f"{'=' * 50}")


def testar_operacoes_basicas():
    """Testa as operações básicas da fila."""
    imprimir_separador("TESTE DE OPERAÇÕES BÁSICAS")

    print("Criando fila com capacidade 5...")
    fila = FilaCircular(5)

    print(f"Fila está vazia? {fila.esta_vazia()}")
    print(f"Fila está cheia? {fila.esta_cheia()}")
    print(f"Tamanho atual: {fila.obter_tamanho()}")

    print("\nInserindo elementos: A, B, C...")
    print(f"Inserir 'A': {fila.inserir('A')}")
    print(f"Inserir 'B': {fila.inserir('B')}")
    print(f"Inserir 'C': {fila.inserir('C')}")
    print(fila)

    print(f"\nConsultar início: {fila.consultar_inicio()}")
    print(f"Tamanho atual: {fila.obter_tamanho()}")

    print(f"\nRemover elemento: {fila.remover()}")
    print(f"Consultar início: {fila.consultar_inicio()}")
    print(fila)


def testar_fila_cheia():
    """Testa comportamento quando a fila está cheia."""
    imprimir_separador("TESTE DE FILA CHEIA")

    print("Criando fila pequena com capacidade 3...")
    fila = FilaCircular(3)

    print("Enchendo a fila completamente...")
    elementos = [1, 2, 3]
    for elemento in elementos:
        resultado = fila.inserir(elemento)
        print(f"Inserir {elemento}: {resultado}")

    print(fila)
    print(f"Fila está cheia? {fila.esta_cheia()}")

    print("\nTentando inserir mais um elemento...")
    resultado = fila.inserir(4)
    print(f"Inserir 4: {resultado}")
    print("Fila continua: ", fila)


def testar_fila_vazia():
    """Testa comportamento quando a fila está vazia."""
    imprimir_separador("TESTE DE FILA VAZIA")

    fila = FilaCircular(3)

    print(f"Fila vazia - Consultar início: {fila.consultar_inicio()}")
    print(f"Fila vazia - Remover: {fila.remover()}")
    print(f"Está vazia? {fila.esta_vazia()}")

    print("\nAdicionando e removendo todos os elementos...")
    fila.inserir("X")
    fila.inserir("Y")
    print(f"Após inserir X e Y: {fila}")

    print(f"Removendo: {fila.remover()}")
    print(f"Removendo: {fila.remover()}")
    print(f"Estado atual: {fila}")

    print(f"Tentando remover de fila vazia: {fila.remover()}")


def testar_incremento_circular():
    """Testa o comportamento circular da fila."""
    imprimir_separador("TESTE DE INCREMENTO CIRCULAR")

    print("Criando fila com capacidade 4...")
    fila = FilaCircular(4)

    print("Enchendo a fila...")
    for i in range(1, 5):
        fila.inserir(f"Item{i}")
        print(f"Inserido Item{i}: {fila}")

    print("\nRemoções e inserções para testar circularidade...")
    print(f"Removido: {fila.remover()}")
    print(f"Removido: {fila.remover()}")
    print(f"Estado após remoções: {fila}")

    print(f"\nInserindo novos elementos...")
    fila.inserir("NovoA")
    print(f"Inserido NovoA: {fila}")
    fila.inserir("NovoB")
    print(f"Inserido NovoB: {fila}")

    print(f"\nFila está cheia? {fila.esta_cheia()}")
    print(f"Lista de elementos: {fila.listar_elementos()}")


def testar_casos_extremos():
    """Testa casos extremos e validações."""
    imprimir_separador("TESTE DE CASOS EXTREMOS")

    print("Testando criação com capacidade inválida...")
    try:
        fila_invalida = FilaCircular(0)
    except ValueError as e:
        print(f"Erro capturado: {e}")

    try:
        fila_invalida = FilaCircular(-1)
    except ValueError as e:
        print(f"Erro capturado: {e}")

    print("\nTestando fila com capacidade 1...")
    fila_mini = FilaCircular(1)
    print(f"Inserir 'único': {fila_mini.inserir('único')}")
    print(f"Está cheia? {fila_mini.esta_cheia()}")
    print(f"Tentar inserir outro: {fila_mini.inserir('outro')}")
    print(f"Consultar: {fila_mini.consultar_inicio()}")
    print(f"Remover: {fila_mini.remover()}")
    print(f"Está vazia? {fila_mini.esta_vazia()}")


def menu_interativo():
    """Menu interativo para testar manualmente a fila."""
    imprimir_separador("MENU INTERATIVO")

    capacidade = int(input("Digite a capacidade da fila: "))
    fila = FilaCircular(capacidade)

    while True:
        print(f"\n{fila}")
        print("\nOpções:")
        print("1 - Inserir elemento")
        print("2 - Remover elemento")
        print("3 - Consultar início")
        print("4 - Verificar se está vazia")
        print("5 - Verificar se está cheia")
        print("6 - Mostrar tamanho")
        print("7 - Listar elementos")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            elemento = input("Digite o elemento a inserir: ")
            resultado = fila.inserir(elemento)
            print(f"Resultado: {resultado}")

        elif opcao == '2':
            elemento = fila.remover()
            print(f"Elemento removido: {elemento}")

        elif opcao == '3':
            elemento = fila.consultar_inicio()
            print(f"Início da fila: {elemento}")

        elif opcao == '4':
            print(f"Fila está vazia: {fila.esta_vazia()}")

        elif opcao == '5':
            print(f"Fila está cheia: {fila.esta_cheia()}")

        elif opcao == '6':
            print(f"Tamanho atual: {fila.obter_tamanho()}/{fila.obter_capacidade()}")

        elif opcao == '7':
            elementos = fila.listar_elementos()
            print(f"Elementos: {elementos}")

        elif opcao == '0':
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


def main():
    """Função principal que executa todos os testes."""
    print("IMPLEMENTAÇÃO DE FILA CIRCULAR")
    print("Estrutura de dados usando vetor com incremento circular")

    # Executar todos os testes automatizados
    testar_operacoes_basicas()
    testar_fila_cheia()
    testar_fila_vazia()
    testar_incremento_circular()
    testar_casos_extremos()

    # Perguntar se o usuário quer testar interativamente
    resposta = input("\nDeseja executar o menu interativo? (s/n): ").lower()
    if resposta in ['s', 'sim', 'y', 'yes']:
        menu_interativo()

    print("\nTestes concluídos!")


if __name__ == "__main__":
    main()