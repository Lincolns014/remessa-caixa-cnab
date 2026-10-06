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
         "00174152760",
         "01980303711",
         "03492002706",
         "07643027790",
         "08012014700",
         "08725670794",
         "13291477740",
         "14151837752",
         "18520667848",
         "41855043734",
         "47205130778",
         "48060852787",
         "52571173715",
         "57472963704",
         "63290219615",
         "65216563768",
         "67421547720",
         "69216223553",
         "72535903768",
         "78624576768",
         "80262902753",
         "82704600791",
         "89107373791",
         "97905763749",
         "97946087772",
 
}

# ===============================
# 🔒 (OPCIONAL) CPFs BLOQUEADOS
# ===============================
# 👉 Se quiser separar bloqueados de exclusão manual

CPFS_BLOQUEADOS = {
    # "00000000000",
}