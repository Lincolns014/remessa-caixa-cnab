import sys
from pathlib import Path

# 🔧 garante que o Python enxergue a raiz do projeto
sys.path.append(str(Path(__file__).resolve().parent))

from src.cnab import header, trailer
from src.processador import executar_processamento
from src.config import ARQUIVO_SAIDA, CODIGO_INICIAL

linhas = [header()]

linhas_proc, qtd, soma, codigo_final = executar_processamento()

linhas += linhas_proc

linhas.append(trailer(qtd, soma))

with open(ARQUIVO_SAIDA, "w", encoding="ascii") as f:
    f.write("\n".join(linhas) + "\n")

print("\n✅ REMESSA GERADA COM SUCESSO")
print(f"Registros: {qtd}")
print(f"Valor: R$ {soma/100:,.2f}")
print(f"Código inicial: {CODIGO_INICIAL}")
print(f"Código final: {codigo_final-1}")