import pandas as pd
from tqdm import tqdm
from src.config import *
from src.utils import normalizar_cpf
from src.cnab import detalhe

def executar_processamento():

    linhas = []

    codigo = CODIGO_INICIAL
    qtd_total = 0
    soma_total = 0

    # ===============================
    # CARREGAR RETRO PRIMEIRO
    # ===============================

    df_add = pd.read_excel(
        ARQUIVO_ADICOES,
        sheet_name="Retroativos_Outubro_2026"
    )

    df_add = df_add[df_add[COLUNA_CPF].notna()]
    df_add[COLUNA_CPF] = df_add[COLUNA_CPF].map(normalizar_cpf)

    # 🔥 REMOVE CPFs EXCLUÍDOS MANUALMENTE (IMPORTANTE)
    df_add = df_add[
        ~df_add[COLUNA_CPF].isin(CPFS_EXCLUIR)
    ]

    cpfs_retro = set(df_add[COLUNA_CPF])

    # ===============================
    # GERAR RETRO
    # ===============================

    parcelas_retro = [
        ("01", VALOR_2025),  # Jul/2025
        ("02", VALOR_2025),  # Ago/2025
        ("03", VALOR_2025),  # Set/2025
        ("04", VALOR_2025),  # Out/2025
        ("05", VALOR_2025),  # Nov/2025
        ("06", VALOR_2025),  # Dez/2025

        ("07", VALOR_2026),  # Jan/2026
        ("08", VALOR_2026),  # Fev/2026
        ("09", VALOR_2026),  # Mar/2026
        ("10", VALOR_2026),  # Abr/2026
        ("11", VALOR_2026),  # Mai/2026
        ("12", VALOR_2026),  # Jun/2026
        ("13", VALOR_2026),  # Jul/2026
        ("14", VALOR_2026),  # Ago/2026
        ("15", VALOR_2026),  # Set/2026
        ("16", VALOR_2026),  # Out/2026
    ]

    for cpf in tqdm(df_add[COLUNA_CPF], desc="Retroativo"):

        for parcela, valor in parcelas_retro:
            linhas.append(detalhe(cpf, codigo, parcela, valor))
            codigo += 1
            qtd_total += 1
            soma_total += valor

    # ===============================
    # LISTA PRINCIPAL (Outubrobro/2026)
    # ===============================

    df_principal = pd.read_excel(ARQUIVO_PRINCIPAL)

    df_principal = df_principal[df_principal[COLUNA_CPF].notna()]
    df_principal[COLUNA_CPF] = df_principal[COLUNA_CPF].map(normalizar_cpf)

    # 🔥 REMOVE CPFs EXCLUÍDOS MANUALMENTE
    df_principal = df_principal[
        ~df_principal[COLUNA_CPF].isin(CPFS_EXCLUIR)
    ]

    # 🔥 REMOVE QUEM JÁ ESTÁ NO RETRO (ANTI-DUPLICIDADE)
    df_principal = df_principal[
        ~df_principal[COLUNA_CPF].isin(cpfs_retro)
    ]

    for cpf in tqdm(df_principal[COLUNA_CPF], desc="Outubro"):

        linhas.append(detalhe(cpf, codigo, "16", VALOR_2026))
        codigo += 1
        qtd_total += 1
        soma_total += VALOR_2026

    return linhas, qtd_total, soma_total, codigo, len(df_add), len(df_principal)