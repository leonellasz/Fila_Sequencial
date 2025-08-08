class FilaCircular:
    """
    Implementação de Fila usando vetor com incremento circular.
    """

    def __init__(self, capacidade):
        """
        Inicializa a fila circular com capacidade especificada.

        Args:
            capacidade (int): Capacidade máxima da fila
        """
        if capacidade <= 0:
            raise ValueError("Capacidade deve ser maior que zero")

        self.capacidade = capacidade
        self.vetor = [None] * capacidade
        self.inicio = 0
        self.fim = 0
        self.tamanho = 0

    def inserir(self, elemento):
        """
        Insere um elemento no fim da fila.

        Args:
            elemento: Elemento a ser inserido

        Returns:
            bool: True se inserido com sucesso, False se fila estiver cheia
        """
        if self.esta_cheia():
            return False

        self.vetor[self.fim] = elemento
        self.fim = (self.fim + 1) % self.capacidade
        self.tamanho += 1
        return True

    def remover(self):
        """
        Remove e retorna o elemento do início da fila.

        Returns:
            elemento: Elemento removido ou None se fila estiver vazia
        """
        if self.esta_vazia():
            return None

        elemento = self.vetor[self.inicio]
        self.vetor[self.inicio] = None  # Limpa a referência
        self.inicio = (self.inicio + 1) % self.capacidade
        self.tamanho -= 1
        return elemento

    def consultar_inicio(self):
        """
        Consulta o elemento do início da fila sem removê-lo.

        Returns:
            elemento: Elemento do início ou None se fila estiver vazia
        """
        if self.esta_vazia():
            return None
        return self.vetor[self.inicio]

    def esta_vazia(self):
        """
        Verifica se a fila está vazia.

        Returns:
            bool: True se vazia, False caso contrário
        """
        return self.tamanho == 0

    def esta_cheia(self):
        """
        Verifica se a fila está cheia.

        Returns:
            bool: True se cheia, False caso contrário
        """
        return self.tamanho == self.capacidade

    def obter_tamanho(self):
        """
        Retorna o tamanho atual da fila.

        Returns:
            int: Número de elementos na fila
        """
        return self.tamanho

    def obter_capacidade(self):
        """
        Retorna a capacidade total da fila.

        Returns:
            int: Capacidade máxima da fila
        """
        return self.capacidade

    def __str__(self):
        """
        Representação em string da fila para depuração.

        Returns:
            str: Representação da fila
        """
        if self.esta_vazia():
            return "Fila vazia"

        elementos = []
        pos = self.inicio
        for _ in range(self.tamanho):
            elementos.append(str(self.vetor[pos]))
            pos = (pos + 1) % self.capacidade

        return f"Fila: [{' -> '.join(elementos)}] (início -> fim)"

    def listar_elementos(self):
        """
        Retorna lista com todos os elementos na ordem da fila.

        Returns:
            list: Lista dos elementos do início ao fim
        """
        elementos = []
        pos = self.inicio
        for _ in range(self.tamanho):
            elementos.append(self.vetor[pos])
            pos = (pos + 1) % self.capacidade
        return elementos