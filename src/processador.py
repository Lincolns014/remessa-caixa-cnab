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
        sheet_name="Adições Fala.BR Maio 2026"
    )

    df_add = df_add[df_add[COLUNA_CPF].notna()]
    df_add[COLUNA_CPF] = df_add[COLUNA_CPF].map(normalizar_cpf)

    cpfs_retro = set(df_add[COLUNA_CPF])

    # ===============================
    # GERAR RETRO
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
        ("11", VALOR_2026),
    ]

    for cpf in tqdm(df_add[COLUNA_CPF], desc="Retroativo"):

        for parcela, valor in parcelas_retro:
            linhas.append(detalhe(cpf, codigo, parcela, valor))
            codigo += 1
            qtd_total += 1
            soma_total += valor

    # ===============================
    # LISTA PRINCIPAL (MAIO)
    # ===============================

    df_principal = pd.read_excel(ARQUIVO_PRINCIPAL)

    df_principal = df_principal[df_principal[COLUNA_CPF].notna()]
    df_principal[COLUNA_CPF] = df_principal[COLUNA_CPF].map(normalizar_cpf)

    # 🔥 REMOVE QUEM JÁ ESTÁ NO RETRO
    df_principal = df_principal[
        ~df_principal[COLUNA_CPF].isin(cpfs_retro)
    ]

    for cpf in tqdm(df_principal[COLUNA_CPF], desc="Maio"):

        linhas.append(detalhe(cpf, codigo, "11", VALOR_2026))
        codigo += 1
        qtd_total += 1
        soma_total += VALOR_2026

    return linhas, qtd_total, soma_total, codigo