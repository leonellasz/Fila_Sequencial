# Makefile para o projeto Fila Circular
# Configurações
PYTHON = python3
MAIN = main.py
TESTS = test_queue.py
QUEUE_MODULE = queue.py

# Cores para output
RED = \033[0;31m
GREEN = \033[0;32m
YELLOW = \033[1;33m
BLUE = \033[0;34m
NC = \033[0m # No Color

# Alvo padrão
.PHONY: all
all: test run

# Executar o programa principal
.PHONY: run
run:
	@echo "$(BLUE)Executando programa principal...$(NC)"
	$(PYTHON) $(MAIN)

# Executar apenas os testes
.PHONY: test
test:
	@echo "$(YELLOW)Executando casos de teste...$(NC)"
	$(PYTHON) $(TESTS)

# Executar testes com unittest discovery
.PHONY: unittest
unittest:
	@echo "$(YELLOW)Executando testes com unittest discovery...$(NC)"
	$(PYTHON) -m unittest discover -v

# Verificar sintaxe dos arquivos Python
.PHONY: check
check:
	@echo "$(BLUE)Verificando sintaxe dos arquivos...$(NC)"
	$(PYTHON) -m py_compile $(QUEUE_MODULE)
	$(PYTHON) -m py_compile $(MAIN)
	$(PYTHON) -m py_compile $(TESTS)
	@echo "$(GREEN)✅ Sintaxe OK!$(NC)"

# Executar análise de código com flake8 (se disponível)
.PHONY: lint
lint:
	@echo "$(BLUE)Executando análise de código...$(NC)"
	@if command -v flake8 >/dev/null 2>&1; then \
		flake8 *.py --max-line-length=100 --ignore=E203,W503; \
		echo "$(GREEN)✅ Análise concluída!$(NC)"; \
	else \
		echo "$(YELLOW)⚠️  flake8 não encontrado. Instale com: pip install flake8$(NC)"; \
	fi

# Executar testes com cobertura (se disponível)
.PHONY: coverage
coverage:
	@echo "$(BLUE)Executando testes com análise de cobertura...$(NC)"
	@if command -v coverage >/dev/null 2>&1; then \
		coverage run --source=. $(TESTS); \
		coverage report -m; \
		coverage html; \
		echo "$(GREEN)✅ Relatório de cobertura gerado em htmlcov/$(NC)"; \
	else \
		echo "$(YELLOW)⚠️  coverage não encontrado. Instale com: pip install coverage$(NC)"; \
	fi

# Demonstração interativa da fila
.PHONY: demo
demo:
	@echo "$(GREEN)Iniciando demonstração interativa...$(NC)"
	@$(PYTHON) -c "from $(MAIN:%.py=%) import menu_interativo; menu_interativo()"

# Executar apenas testes básicos sem menu interativo
.PHONY: test-auto
test-auto:
	@echo "$(YELLOW)Executando testes automatizados...$(NC)"
	@$(PYTHON) -c "from $(MAIN:%.py=%) import *; testar_operacoes_basicas(); testar_fila_cheia(); testar_fila_vazia(); testar_incremento_circular(); testar_casos_extremos(); print('\\n$(GREEN)✅ Testes automatizados concluídos!$(NC)')"

# Limpar arquivos temporários
.PHONY: clean
clean:
	@echo "$(BLUE)Limpando arquivos temporários...$(NC)"
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	rm -rf htmlcov/ .coverage
	@echo "$(GREEN)✅ Limpeza concluída!$(NC)"

# Instalar dependências de desenvolvimento
.PHONY: install-dev
install-dev:
	@echo "$(BLUE)Instalando dependências de desenvolvimento...$(NC)"
	pip install flake8 coverage
	@echo "$(GREEN)✅ Dependências instaladas!$(NC)"

# Criar documentação
.PHONY: docs
docs:
	@echo "$(BLUE)Gerando documentação...$(NC)"
	$(PYTHON) -c "import $(QUEUE_MODULE:%.py=%); help($(QUEUE_MODULE:%.py=%).FilaCircular)" > docs.txt
	@echo "$(GREEN)✅ Documentação salva em docs.txt$(NC)"

# Executar benchmark simples
.PHONY: benchmark
benchmark:
	@echo "$(BLUE)Executando benchmark simples...$(NC)"
	@$(PYTHON) -c "\
import time; \
from $(QUEUE_MODULE:%.py=%) import FilaCircular; \
fila = FilaCircular(1000); \
start = time.time(); \
for i in range(10000): \
	if not fila.esta_cheia(): fila.inserir(i); \
	if not fila.esta_vazia(): fila.remover(); \
end = time.time(); \
print(f'Tempo para 10000 operações: {end-start:.4f}s')"

# Validar implementação completa
.PHONY: validate
validate: check test lint
	@echo "$(GREEN)✅ Validação completa realizada!$(NC)"

# Ajuda
.PHONY: help
help:
	@echo "$(BLUE)Comandos disponíveis:$(NC)"
	@echo "  $(GREEN)make run$(NC)        - Executar o programa principal"
	@echo "  $(GREEN)make test$(NC)       - Executar casos de teste"
	@echo "  $(GREEN)make all$(NC)        - Executar testes + programa principal"
	@echo "  $(GREEN)make check$(NC)      - Verificar sintaxe dos arquivos"
	@echo "  $(GREEN)make lint$(NC)       - Análise de código com flake8"
	@echo "  $(GREEN)make coverage$(NC)   - Executar testes com cobertura"
	@echo "  $(GREEN)make demo$(NC)       - Demonstração interativa"
	@echo "  $(GREEN)make test-auto$(NC)  - Testes automatizados (sem interação)"
	@echo "  $(GREEN)make unittest$(NC)   - Testes com unittest discovery"
	@echo "  $(GREEN)make benchmark$(NC)  - Benchmark simples de performance"
	@echo "  $(GREEN)make clean$(NC)      - Limpar arquivos temporários"
	@echo "  $(GREEN)make install-dev$(NC) - Instalar dependências de desenvolvimento"
	@echo "  $(GREEN)make docs$(NC)       - Gerar documentação"
	@echo "  $(GREEN)make validate$(NC)   - Validação completa (check + test + lint)"
	@echo "  $(GREEN)make help$(NC)       - Mostrar esta ajuda"
	@echo ""
	@echo "$(YELLOW)Exemplos de uso:$(NC)"
	@echo "  make all          # Executa tudo"
	@echo "  make test-auto    # Só testes sem interação"
	@echo "  make validate     # Validação completa"