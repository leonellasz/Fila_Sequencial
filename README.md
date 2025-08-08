# Fila Circular em Python

Implementação de uma estrutura de dados Fila usando vetor com incremento circular.

## O que é

Uma fila circular é uma estrutura de dados que funciona como uma fila normal (primeiro a entrar, primeiro a sair), mas reutiliza as posições do vetor quando elementos são removidos.

## Arquivos

- `queue.py` - Classe FilaCircular
- `main.py` - Programa principal com testes
- `teste.py` - Casos de teste
- `Makefile` - Comandos para executar (Linux/Mac)

## Como usar

### Executar o programa

```bash
python main.py
```

### Executar os testes

```bash
python teste.py
```

### Exemplo de código

```python
from queue import FilaCircular

# Criar fila com capacidade 5
fila = FilaCircular(5)

# Usar a fila
fila.inserir("A")
fila.inserir("B")
print(fila.consultar_inicio())  # A
elemento = fila.remover()       # A
print(fila.esta_vazia())        # False
print(fila.esta_cheia())        # False
```

## Operações disponíveis

- `inserir(elemento)` - Insere no fim da fila
- `remover()` - Remove do início da fila
- `consultar_inicio()` - Consulta o início sem remover
- `esta_vazia()` - Verifica se está vazia
- `esta_cheia()` - Verifica se está cheia
- `obter_tamanho()` - Retorna o tamanho atual

## Requisitos

- Python 3.6 ou superior

## Como funciona o incremento circular

Quando a fila fica cheia e você remove elementos do início, as posições liberadas são reutilizadas para novos elementos, evitando desperdício de espaço.

```
Exemplo:
[A][B][C][ ][ ] → remove A → [ ][B][C][ ][ ] → insere D → [D][B][C][ ][ ]
```
