import pandas as pd
from pathlib import Path
from tqdm import tqdm

# =============================== #
#   CONFIGURAÇÕES                 #
# =============================== #

arquivo_principal = "Maio_2026.xlsx"
arquivo_adicoes  = "Retroativos_julho_2025.xlsx"

coluna_cpf = "CPF"

# Saída
nome_saida = "CNT.PBS.PDPGT01.P01577.D260110.H090000.S00001.txt"
txt_path   = Path().resolve() / nome_saida

# HEADER
DATA_ARQ = "20260331"
HORA_ARQ = "155500"
REMESSA  = "000000010"
PROD_REF = "0157720260402"

# Valores
VALOR_2025 = 227700
VALOR_2026 = 243150

codigo_pagamento_inicial = 197894

# Datas
datas = {
    "10": ("202604", "20260410", "20260420"),
    "01": ("202507", "20260410", "20260420"),
    "02": ("202508", "20260410", "20260420"),
    "03": ("202509", "20260410", "20260420"),
    "04": ("202510", "20260410", "20260420"),
    "05": ("202511", "20260410", "20260420"),
    "06": ("202512", "20260410", "20260420"),
    "07": ("202601", "20260410", "20260420"),
    "08": ("202602", "20260410", "20260420"),
    "09": ("202603", "20260410", "20260420"),
}

# 🔒 BLOQUEADOS (APENAS NA PRINCIPAL)
CPFS_BLOQUEADOS = {
    "07944734746","14436297748","98212630706","13287813722",
    "14760225773","14138194789","62166735720","10926469738"
}

# =============================== #
#   FUNÇÕES                       #
# =============================== #

def normalizar_cpf(cpf: str) -> str:
    cpf = str(cpf).strip().replace(".", "").replace("-", "")
    cpf = ''.join(filter(str.isdigit, cpf))
    return cpf.zfill(11)

def mk_header() -> str:
    return (
        "0" + DATA_ARQ + HORA_ARQ + " ".ljust(5)
        + REMESSA + PROD_REF + " " * 258
    )[:300]

def mk_detalhe(cpf, cod, parcela, valor):
    comp, dt_ger, dt_venc = datas[parcela]

    linha = (
        "2" + "1" + cpf + "0"*14
        + str(cod).zfill(18)
        + str(valor).zfill(12)
        + comp + dt_ger + dt_venc
        + parcela + " "*20 + "0000" + "00000" + "0000"
        + "0000000000000" + " "*173
    )
    return linha[:300]

def mk_trailer(qtd, soma):
    return (
        "9"
        + str(qtd).zfill(9)
        + str(soma).zfill(18)
        + " "*272
    )[:300]

# =============================== #
#   PROCESSAMENTO                 #
# =============================== #

linhas = [mk_header()]

qtd_total = 0
soma_total = 0

codigo_atual = codigo_pagamento_inicial

primeiro_codigo = None
ultimo_codigo = None

# CONTROLE
cpfs_principal = set()

qtd_abril = 0
valor_abril = 0

qtd_retro = 0
valor_retro = 0

# ===============================
# 1. ABRIL (LISTA PRINCIPAL)
# ===============================

df_principal = pd.read_excel(arquivo_principal)
df_principal_original = df_principal.copy()

df_principal = df_principal[df_principal[coluna_cpf].notna()]
df_principal[coluna_cpf] = df_principal[coluna_cpf].map(normalizar_cpf)

# 🔒 BLOQUEIO AQUI (CORRETO)
df_principal = df_principal[
    ~df_principal[coluna_cpf].isin(CPFS_BLOQUEADOS)
]

bloqueados_principal = len(df_principal_original) - len(df_principal)

for cpf in tqdm(df_principal[coluna_cpf], desc="Abril"):

    linhas.append(mk_detalhe(cpf, codigo_atual, "10", VALOR_2026))

    cpfs_principal.add(cpf)

    if primeiro_codigo is None:
        primeiro_codigo = codigo_atual
    ultimo_codigo = codigo_atual

    codigo_atual += 1
    qtd_total += 1
    qtd_abril += 1
    soma_total += VALOR_2026
    valor_abril += VALOR_2026

# ===============================
# 2. RETROATIVO (ADIÇÕES)
# ===============================

parcelas_retro = [
    ("01", VALOR_2025),
    ("02", VALOR_2025),
    ("03", VALOR_2025),
    ("04", VALOR_2025),
    ("05", VALOR_2025),
    ("06", VALOR_2025),
    ("07", VALOR_2026),
    ("08", VALOR_2026),
    ("09", VALOR_2026),
    ("10", VALOR_2026),
]

df_add = pd.read_excel(
    arquivo_adicoes,
    sheet_name="Adições FalaBR Abril 2026"
)

df_add = df_add[df_add[coluna_cpf].notna()]
df_add[coluna_cpf] = df_add[coluna_cpf].map(normalizar_cpf)

# 🚫 NÃO REMOVE BLOQUEADOS AQUI (REGRA CORRETA)

# 🔥 REMOVE QUEM JÁ RECEBEU ABRIL
df_add = df_add[
    ~df_add[coluna_cpf].isin(cpfs_principal)
]

for cpf in tqdm(df_add[coluna_cpf], desc="Retroativo"):

    for parcela, valor in parcelas_retro:

        linhas.append(
            mk_detalhe(cpf, codigo_atual, parcela, valor)
        )

        ultimo_codigo = codigo_atual

        codigo_atual += 1
        qtd_total += 1
        qtd_retro += 1
        soma_total += valor
        valor_retro += valor

# ===============================
# FINALIZAÇÃO
# ===============================

linhas.append(mk_trailer(qtd_total, soma_total))

with open(txt_path, "w", encoding="ascii") as f:
    f.write("\n".join(linhas) + "\n")

# ===============================
# RELATÓRIO
# ===============================

print("\n\n✅ ARQUIVO GERADO COM SUCESSO!")
print("========================================")
print(f"📄 Arquivo: {txt_path}")

print("\n--- ABRIL ---")
print(f"CPFs pagos: {qtd_abril}")
print(f"Bloqueados: {bloqueados_principal}")
print(f"Valor: R$ {valor_abril/100:,.2f}")

print("\n--- RETROATIVO ---")
print(f"Parcelas geradas: {qtd_retro}")
print(f"Valor: R$ {valor_retro/100:,.2f}")

print("\n--- TOTAL ---")
print(f"Registros: {qtd_total}")
print(f"Valor total: R$ {soma_total/100:,.2f}")

print(f"🔢 Código inicial: {primeiro_codigo}")
print(f"🔢 Código final:   {ultimo_codigo}")
print("========================================")