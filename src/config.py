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

ARQUIVO_PRINCIPAL = DATA_DIR / "Outubro_2026.xlsx"
ARQUIVO_ADICOES  = DATA_DIR / "Retroativos_Outubro_2026.xlsx"

ARQUIVO_SAIDA = OUTPUT_DIR / "CNT.PBS.PDPGT01.P01577.D260110.H090000.S00001.txt"

COLUNA_CPF = "CPF"

# ===============================
# HEADER CNAB
# ===============================

DATA_ARQ = "20261005"
HORA_ARQ = "153500"
REMESSA  = "000000016"
PROD_REF = "0157720261002"

# ===============================
# VALORES
# ===============================

VALOR_2025 = 227700
VALOR_2026 = 243150

# ===============================
# CONTROLE DE CÓDIGO
# ===============================

CODIGO_INICIAL = 327691

# ===============================
# 🚫 EXCLUSÃO MANUAL DE CPFs
# ===============================
# 👉 Use para remover CPFs com erro ou inconsistência
# 👉 Pode adicionar/remover sem mexer na lógica do sistema

CPFS_EXCLUIR = {        
        #  "00000000000",
       
 
}

# ===============================
# 🔒 (OPCIONAL) CPFs BLOQUEADOS
# ===============================
# 👉 Se quiser separar bloqueados de exclusão manual

CPFS_BLOQUEADOS = {
    # "00000000000",
}