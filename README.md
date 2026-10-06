
# 💰 Sistema de Geração de Remessa CNAB – CAIXA

Automação em Python para processamento de dados e geração de arquivos de remessa no padrão CNAB para a CAIXA Econômica Federal.

O projeto foi desenvolvido a partir de um cenário real de processamento de pagamentos em lote, envolvendo tratamento de dados, aplicação de regras de negócio, validações, prevenção de duplicidades e geração automatizada do arquivo de remessa.

---

## 🎯 Objetivo

Automatizar o processo de geração de remessas CNAB, reduzindo atividades manuais e aumentando a confiabilidade do processamento.

O sistema foi desenvolvido para:

- Gerar arquivos CNAB estruturados;
- Processar parcelas da competência atual;
- Processar pagamentos retroativos;
- Aplicar regras de negócio específicas;
- Evitar pagamentos duplicados;
- Validar e padronizar identificadores;
- Processar dados provenientes de planilhas Excel;
- Gerar um relatório resumido da execução.

---

## ⚙️ Funcionalidades

### 📥 Entrada de dados

- Leitura de planilhas Excel;
- Tratamento e organização dos dados;
- Validação das informações necessárias ao processamento;
- Normalização de identificadores.

### 🔄 Processamento

- Separação entre lista principal e registros retroativos;
- Aplicação de regras de negócio;
- Processamento de diferentes competências;
- Controle dos registros já considerados no processamento;
- Prevenção de duplicidades entre listas.

### 📄 Geração CNAB

- Geração de Header;
- Geração de registros de detalhe;
- Geração de Trailer;
- Controle sequencial dos registros;
- Geração do arquivo no padrão CNAB utilizado pelo processo.

### 📊 Relatório

Ao final do processamento, o sistema gera informações de acompanhamento da execução, incluindo:

- quantidade de registros processados;
- quantidade de registros por grupo de processamento;
- valor total processado;
- controle dos códigos utilizados;
- status da execução.

---

## 🧠 Regras de Negócio

O processamento é dividido em diferentes etapas para permitir maior controle sobre as regras utilizadas.

### ✔ Lista Principal

Processa os registros referentes à competência atual.

### ✔ Retroativos

Processa registros referentes a competências anteriores que precisam ser incluídos na remessa.

### 🚫 Prevenção de Duplicidade

Os registros presentes na lista de retroativos são considerados no controle da lista principal para evitar que o mesmo beneficiário seja processado de forma duplicada.

### 🔒 Tratamento dos Dados

O sistema realiza procedimentos como:

- normalização de CPF;
- padronização para 11 dígitos;
- tratamento de valores nulos;
- validação das informações utilizadas no processamento.

As regras financeiras e os dados utilizados no ambiente real não são disponibilizados neste repositório público.

---

## 🏗️ Estrutura do Projeto

```text
remessa-caixa-cnab/
│
├── data/
│   └── # Arquivos de entrada não versionados
│
├── outputs/
│   └── # Arquivos gerados não versionados
│
├── src/
│   ├── config.py
│   ├── utils.py
│   ├── cnab.py
│   └── processador.py
│
├── main.py
├── .gitignore
└── README.md
```

### Responsabilidade dos módulos

| Arquivo            | Responsabilidade                                             |
| ------------------ | ------------------------------------------------------------ |
| `main.py`        | Orquestração da execução do sistema                      |
| `processador.py` | Processamento dos dados e aplicação das regras de negócio |
| `cnab.py`        | Construção dos registros CNAB                              |
| `config.py`      | Configurações e parâmetros do sistema                     |
| `utils.py`       | Funções auxiliares e tratamento dos dados                  |

---

## 🔄 Fluxo do Processamento

```text
                 Arquivos Excel
                       │
                       ▼
                Leitura dos dados
                       │
                       ▼
             Tratamento e validação
                       │
                       ▼
              Aplicação das regras
                  de negócio
                       │
              ┌────────┴────────┐
              ▼                 ▼
        Lista Principal     Retroativos
              │                 │
              └────────┬────────┘
                       ▼
             Controle de duplicidade
                       │
                       ▼
              Geração dos registros
                    CNAB
                       │
             ┌─────────┼─────────┐
             ▼         ▼         ▼
           Header   Detalhes   Trailer
                       │
                       ▼
                Arquivo de Remessa
                       │
                       ▼
                  Relatório
```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**
- **Pandas**
- **OpenPyXL**
- **TQDM**
- **Git**
- **GitHub**
- **CNAB**

---

## 🚀 Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/Lincolns014/remessa-caixa-cnab.git
```

### 2. Acessar o projeto

```bash
cd remessa-caixa-cnab
```

### 3. Instalar as dependências

```bash
pip install pandas openpyxl tqdm
```

### 4. Organizar os arquivos de entrada

Os arquivos de entrada devem ser disponibilizados localmente na estrutura utilizada pelo projeto.

```text
data/
```

> Os arquivos utilizados no ambiente real não fazem parte deste repositório público.

### 5. Executar o sistema

```bash
python main.py
```

Após a execução, o sistema gera o arquivo de remessa e o relatório correspondente no ambiente local.

---

## 🔒 Tratamento de Dados

Este projeto foi desenvolvido em um cenário real de processamento de pagamentos e pode envolver informações pessoais e operacionais.

Por esse motivo, dados reais não são disponibilizados neste repositório público.

Não fazem parte do repositório:

- planilhas com dados reais;
- CPFs;
- arquivos CNAB reais;
- relatórios operacionais;
- informações financeiras;
- credenciais;
- configurações sensíveis.

O arquivo `.gitignore` é utilizado para impedir o versionamento desses arquivos.

---

## 💼 Aplicação Real

O projeto foi desenvolvido para automatizar uma rotina real de processamento de pagamentos em lote.

A solução combina:

- automação de processos;
- tratamento de dados;
- regras de negócio;
- geração de arquivos estruturados;
- validações;
- controle de duplicidade;
- geração de relatórios.

O objetivo é reduzir tarefas manuais, diminuir riscos de inconsistência e aumentar a confiabilidade do processo.

---

## 📊 Competências Demonstradas

Este projeto envolve conhecimentos relacionados a:

- 🐍 Python
- 📊 Pandas
- 🔄 ETL
- 🧹 Tratamento de dados
- 🧠 Regras de negócio
- 🔎 Validação de dados
- 🚫 Controle de duplicidade
- 📄 Processamento de arquivos
- 🏦 Padrão CNAB
- ⚙️ Automação de processos
- 📈 Geração de relatórios
- 🗂️ Organização de projetos Python
- 🔧 Git e GitHub

---

## 🔮 Próximos Passos

Possíveis evoluções do projeto:

- [ ] Testes automatizados;
- [ ] Logging estruturado;
- [ ] Validação mais abrangente dos arquivos de entrada;
- [ ] Configuração externa dos parâmetros;
- [ ] Geração de relatórios em Excel;
- [ ] Integração com arquivos de retorno CNAB;
- [ ] Persistência das informações em banco de dados;
- [ ] Monitoramento do processamento;
- [ ] Integração com ferramentas de orquestração.

---

## 👨‍💻 Autor

**Lincolns Rocha**

Python | Data Analysis | Automation | ETL | Data Engineering

🔗 [GitHub](https://github.com/Lincolns014)
