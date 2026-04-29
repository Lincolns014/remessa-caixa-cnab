from pathlib import Path

# ===============================
# DIRETÓRIOS
# ===============================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"

# ===============================
# ARQUIVOS
# ===============================

ARQUIVO_PRINCIPAL = DATA_DIR / "Maio_2026.xlsx"
ARQUIVO_ADICOES  = DATA_DIR / "Retroativos_julho_2025.xlsx"

ARQUIVO_SAIDA = OUTPUT_DIR / "CNT.PBS.PDPGT01.P01577.D260110.H090000.S00001.txt"

COLUNA_CPF = "CPF"

# ===============================
# HEADER CNAB
# ===============================

DATA_ARQ = "20260427"
HORA_ARQ = "125000"
REMESSA  = "000000011"
PROD_REF = "0157720260502"

# ===============================
# VALORES
# ===============================

VALOR_2025 = 227700
VALOR_2026 = 243150

# ===============================
# CONTROLE DE CÓDIGO
# ===============================

CODIGO_INICIAL = 219544

# ===============================
# 🚫 EXCLUSÃO MANUAL DE CPFs
# ===============================
# 👉 Use para remover CPFs com erro ou inconsistência
# 👉 Pode adicionar/remover sem mexer na lógica do sistema

CPFS_EXCLUIR = {
    "02022013760",
    "03093647797",
    "06452482661",
    "09479094606",
    "09880539770",
    "28222458787",
    "28958152672",
    "35072091287",
    "43386083668",
    "57845336734",
    "70060625600",
    "72676337734",
    "89131630715",
    "98765965787",
}

# ===============================
# 🔒 (OPCIONAL) CPFs BLOQUEADOS
# ===============================
# 👉 Se quiser separar bloqueados de exclusão manual

CPFS_BLOQUEADOS = {
    # "00000000000",
}