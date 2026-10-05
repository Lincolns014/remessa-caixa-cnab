import sys
from pathlib import Path

# 🔧 garante que o Python enxergue a raiz do projeto
sys.path.append(str(Path(__file__).resolve().parent))

from src.cnab import header, trailer
from src.processador import executar_processamento
from src.config import (
    ARQUIVO_SAIDA,
    CODIGO_INICIAL,
    ARQUIVO_PRINCIPAL,
    ARQUIVO_ADICOES
)


# ===============================
# FUNÇÃO DE FORMATAÇÃO BRASILEIRA
# ===============================

def formatar_numero(numero):
    return f"{numero:,}".replace(",", ".")


def formatar_moeda(valor_centavos):
    valor = valor_centavos / 100

    return (
        f"R$ {valor:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )


# ===============================
# PROCESSAMENTO
# ===============================

linhas = [header()]

(
    linhas_proc,
    qtd,
    soma,
    codigo_final,
    qtd_retro,
    qtd_principal
) = executar_processamento()

linhas += linhas_proc

linhas.append(trailer(qtd, soma))


# ===============================
# GERAR REMESSA
# ===============================

with open(ARQUIVO_SAIDA, "w", encoding="ascii") as f:
    f.write("\n".join(linhas) + "\n")


# ===============================
# DEFINIR MÊS DA REMESSA
# ===============================

MES_REFERENCIA = "OUTUBRO/2026"


# ===============================
# VALORES FORMATADOS
# ===============================

qtd_retro_formatada = formatar_numero(qtd_retro)
qtd_principal_formatada = formatar_numero(qtd_principal)
qtd_total_formatada = formatar_numero(qtd)

valor_total_formatado = formatar_moeda(soma)

codigo_final_real = codigo_final - 1
proximo_codigo = codigo_final


# ===============================
# GERAR RELATÓRIO
# ===============================

RELATORIO_SAIDA = (
    Path(__file__).resolve().parent / "relatório.txt"
)

relatorio = f"""========================================
REMESSA CAIXA - {MES_REFERENCIA}
========================================

Arquivo principal:
{ARQUIVO_PRINCIPAL.name}

Retroativos:
{ARQUIVO_ADICOES.name}

CPFs retroativos: {qtd_retro_formatada}
CPFs principal: {qtd_principal_formatada}

Registros gerados:
{qtd_total_formatada}

Valor total:
{valor_total_formatado}

Código inicial:
{CODIGO_INICIAL}

Código final:
{codigo_final_real}

Próximo código inicial:
{proximo_codigo}

========================================
STATUS: REMESSA GERADA COM SUCESSO
========================================
"""


# ===============================
# SALVAR RELATÓRIO
# ===============================

with open(RELATORIO_SAIDA, "w", encoding="utf-8") as f:
    f.write(relatorio)


# ===============================
# MENSAGEM FINAL
# ===============================

print("\n" + relatorio)

print(f"📄 Relatório salvo em: {RELATORIO_SAIDA}")
print(f"📁 Remessa salva em: {ARQUIVO_SAIDA}")