#!/usr/bin/env python3
"""
Casos de teste unitários para a Fila Circular.
Utiliza o módulo unittest do Python.
"""

import unittest
from queue import FilaCircular


class TestFilaCircular(unittest.TestCase):
    """Classe de testes para a Fila Circular."""

    def setUp(self):
        """Configuração executada antes de cada teste."""
        self.fila = FilaCircular(5)
        self.fila_pequena = FilaCircular(2)

    def test_inicializacao(self):
        """Testa a inicialização da fila."""
        self.assertTrue(self.fila.esta_vazia())
        self.assertFalse(self.fila.esta_cheia())
        self.assertEqual(self.fila.obter_tamanho(), 0)
        self.assertEqual(self.fila.obter_capacidade(), 5)

    def test_inicializacao_invalida(self):
        """Testa inicialização com capacidade inválida."""
        with self.assertRaises(ValueError):
            FilaCircular(0)

        with self.assertRaises(ValueError):
            FilaCircular(-1)

    def test_inserir_elemento(self):
        """Testa inserção de elementos."""
        self.assertTrue(self.fila.inserir("A"))
        self.assertFalse(self.fila.esta_vazia())
        self.assertEqual(self.fila.obter_tamanho(), 1)

        self.assertTrue(self.fila.inserir("B"))
        self.assertEqual(self.fila.obter_tamanho(), 2)

    def test_inserir_fila_cheia(self):
        """Testa inserção quando fila está cheia."""
        # Encher a fila pequena
        self.assertTrue(self.fila_pequena.inserir(1))
        self.assertTrue(self.fila_pequena.inserir(2))
        self.assertTrue(self.fila_pequena.esta_cheia())

        # Tentar inserir quando cheia
        self.assertFalse(self.fila_pequena.inserir(3))
        self.assertEqual(self.fila_pequena.obter_tamanho(), 2)

    def test_remover_elemento(self):
        """Testa remoção de elementos."""
        self.fila.inserir("A")
        self.fila.inserir("B")

        elemento = self.fila.remover()
        self.assertEqual(elemento, "A")
        self.assertEqual(self.fila.obter_tamanho(), 1)

        elemento = self.fila.remover()
        self.assertEqual(elemento, "B")
        self.assertTrue(self.fila.esta_vazia())

    def test_remover_fila_vazia(self):
        """Testa remoção de fila vazia."""
        elemento = self.fila.remover()
        self.assertIsNone(elemento)
        self.assertTrue(self.fila.esta_vazia())

    def test_consultar_inicio(self):
        """Testa consulta do início da fila."""
        # Fila vazia
        self.assertIsNone(self.fila.consultar_inicio())

        # Com elementos
        self.fila.inserir("X")
        self.fila.inserir("Y")
        self.assertEqual(self.fila.consultar_inicio(), "X")

        # Consulta não deve alterar a fila
        self.assertEqual(self.fila.obter_tamanho(), 2)
        self.assertEqual(self.fila.consultar_inicio(), "X")

    def test_fifo_order(self):
        """Testa se a fila segue ordem FIFO (First In, First Out)."""
        elementos = ["primeiro", "segundo", "terceiro"]

        # Inserir elementos
        for elemento in elementos:
            self.fila.inserir(elemento)

        # Remover e verificar ordem
        for elemento_esperado in elementos:
            elemento_removido = self.fila.remover()
            self.assertEqual(elemento_removido, elemento_esperado)

    def test_incremento_circular(self):
        """Testa o comportamento circular da fila."""
        # Usar fila pequena para testar circularidade facilmente
        fila = FilaCircular(3)

        # Encher completamente
        fila.inserir(1)
        fila.inserir(2)
        fila.inserir(3)
        self.assertTrue(fila.esta_cheia())

        # Remover alguns elementos
        self.assertEqual(fila.remover(), 1)
        self.assertEqual(fila.remover(), 2)

        # Inserir novos elementos (deve usar posições circulares)
        fila.inserir(4)
        fila.inserir(5)
        self.assertTrue(fila.esta_cheia())

        # Verificar ordem correta
        self.assertEqual(fila.remover(), 3)
        self.assertEqual(fila.remover(), 4)
        self.assertEqual(fila.remover(), 5)
        self.assertTrue(fila.esta_vazia())

    def test_capacidade_unitaria(self):
        """Testa fila com capacidade 1."""
        fila_mini = FilaCircular(1)

        self.assertTrue(fila_mini.inserir("único"))
        self.assertTrue(fila_mini.esta_cheia())
        self.assertFalse(fila_mini.inserir("outro"))

        self.assertEqual(fila_mini.consultar_inicio(), "único")
        self.assertEqual(fila_mini.remover(), "único")
        self.assertTrue(fila_mini.esta_vazia())

    def test_operacoes_alternadas(self):
        """Testa operações de inserção e remoção alternadas."""
        # Padrão: inserir, inserir, remover, inserir, remover, remover
        self.fila.inserir("A")
        self.fila.inserir("B")
        self.assertEqual(self.fila.remover(), "A")

        self.fila.inserir("C")
        self.assertEqual(self.fila.remover(), "B")
        self.assertEqual(self.fila.remover(), "C")

        self.assertTrue(self.fila.esta_vazia())

    def test_listar_elementos(self):
        """Testa listagem de elementos."""
        self.assertEqual(self.fila.listar_elementos(), [])

        elementos = ["a", "b", "c"]
        for elemento in elementos:
            self.fila.inserir(elemento)

        self.assertEqual(self.fila.listar_elementos(), elementos)

    def test_str_representation(self):
        """Testa representação em string da fila."""
        # Fila vazia
        self.assertEqual(str(self.fila), "Fila vazia")

        # Com elementos
        self.fila.inserir(1)
        self.fila.inserir(2)
        self.assertIn("1 -> 2", str(self.fila))

    def test_tipos_diferentes(self):
        """Testa fila com diferentes tipos de dados."""
        elementos = [1, "string", [1, 2], {"key": "value"}, None]

        for elemento in elementos:
            self.fila.inserir(elemento)

        for elemento_esperado in elementos:
            elemento_removido = self.fila.remover()
            self.assertEqual(elemento_removido, elemento_esperado)


class TestFilaCircularIntegracao(unittest.TestCase):
    """Testes de integração e cenários complexos."""

    def test_uso_intensivo(self):
        """Testa uso intensivo da fila com muitas operações."""
        fila = FilaCircular(10)

        # Fazer muitas inserções e remoções
        for i in range(100):
            # Inserir alguns elementos
            for j in range(5):
                fila.inserir(f"item_{i}_{j}")

            # Remover alguns elementos
            for _ in range(3):
                fila.remover()

        # Fila deve estar funcional
        self.assertFalse(fila.esta_vazia())
        self.assertIsNotNone(fila.consultar_inicio())

    def test_cenario_producao_consumo(self):
        """Simula cenário de produção e consumo."""
        fila = FilaCircular(5)

        # Simular produtor adicionando itens
        items_produzidos = []
        for i in range(10):
            item = f"produto_{i}"
            items_produzidos.append(item)

            if not fila.esta_cheia():
                fila.inserir(item)
            else:
                # Consumir um item para fazer espaço
                fila.remover()
                fila.inserir(item)

        # Consumir todos os itens restantes
        items_consumidos = []
        while not fila.esta_vazia():
            item = fila.remover()
            items_consumidos.append(item)

        # Verificar se os últimos itens produzidos estão nos consumidos
        for item in items_consumidos:
            self.assertIn(item, items_produzidos)


def executar_testes():
    """Executa todos os testes e exibe relatório."""
    print("EXECUTANDO CASOS DE TESTE DA FILA CIRCULAR")
    print("=" * 50)

    # Criar suite de testes
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Adicionar classes de teste
    suite.addTests(loader.loadTestsFromTestCase(TestFilaCircular))
    suite.addTests(loader.loadTestsFromTestCase(TestFilaCircularIntegracao))

    # Executar testes com verbose
    runner = unittest.TextTestRunner(verbosity=2)
    resultado = runner.run(suite)

    # Relatório final
    print("\n" + "=" * 50)
    print("RELATÓRIO FINAL")
    print(f"Testes executados: {resultado.testsRun}")
    print(f"Falhas: {len(resultado.failures)}")
    print(f"Erros: {len(resultado.errors)}")

    if resultado.wasSuccessful():
        print("TODOS OS TESTES PASSARAM!")
    else:
        print(" ALGUNS TESTES FALHARAM!")

    return resultado.wasSuccessful()


if __name__ == "__main__":
    executar_testes()