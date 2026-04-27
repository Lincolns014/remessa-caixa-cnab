def normalizar_cpf(cpf):
    cpf = str(cpf).replace(".", "").replace("-", "").strip()
    cpf = ''.join(filter(str.isdigit, cpf))
    return cpf.zfill(11)