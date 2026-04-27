

# 💰 Sistema de Geração de Remessa CNAB – CAIXA

Este projeto automatiza a geração de arquivos de remessa no padrão CNAB para envio à CAIXA Econômica Federal, incluindo processamento de parcelas mensais e retroativos com regras de negócio específicas.

---

## 🎯 Objetivo

Automatizar o processo de pagamento em lote de beneficiários, garantindo:

* Geração correta de arquivos CNAB (Header, Detalhe e Trailer)
* Pagamento de parcelas mensais (ex: Maio/2026)
* Cálculo e geração de retroativos (desde Julho/2025)
* Prevenção de pagamentos duplicados
* Validação e padronização de CPFs

---

## ⚙️ Funcionalidades

* 📌 Leitura de planilhas Excel com beneficiários
* 🔄 Processamento separado de:
* Lista principal (parcela atual)
* Lista de retroativos (FalaBR)
* 🚫 Remoção automática de duplicidade entre listas
* 🧠 Aplicação de regras de negócio por ano:
* 2025 → R$ 2.277,00
* 2026 → R$ 2.431,50
* 📄 Geração de arquivo CNAB estruturado (300 posições)
* 📊 Relatório final com:
* Quantidade de registros
* Valor total
* Código inicial e final de pagamento

---

## 🏗️ Estrutura do Projeto

<pre class="overflow-visible! px-0!" data-start="1773" data-end="2236"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>remessa_caixa/</span><br/><span>│</span><br/><span>├── data/</span><br/><span>│   └── entrada/          </span><span class="ͼl"># Arquivos Excel de entrada</span><br/><span>│</span><br/><span>├── outputs/              </span><span class="ͼl"># Arquivos CNAB gerados</span><br/><span>│</span><br/><span>├── src/</span><br/><span>│   ├── config.py         </span><span class="ͼl"># Configurações do sistema</span><br/><span>│   ├── utils.py          </span><span class="ͼl"># Funções auxiliares (ex: CPF)</span><br/><span>│   ├── cnab.py           </span><span class="ͼl"># Geração CNAB (Header, Detalhe, Trailer)</span><br/><span>│   ├── processador.py    </span><span class="ͼl"># Regras de negócio</span><br/><span>│</span><br/><span>├── main.py               </span><span class="ͼl"># Execução principal</span><br/><span>├── requirements.txt</span><br/><span>└── README.md</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

## 🚀 Como Executar

### 1. Instalar dependências

<pre class="overflow-visible! px-0!" data-start="2294" data-end="2338"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>pip install pandas openpyxl tqdm</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

### 2. Organizar arquivos

Coloque os arquivos de entrada em:

<pre class="overflow-visible! px-0!" data-start="2408" data-end="2429"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>data/entrada/</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

Exemplo:

<pre class="overflow-visible! px-0!" data-start="2441" data-end="2517"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>data/entrada/Maio_2026.xlsx</span><br/><span>data/entrada/Retroativos_julho_2025.xlsx</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

### 3. Executar o sistema

<pre class="overflow-visible! px-0!" data-start="2551" data-end="2577"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>python main.py</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

### 4. Resultado

O arquivo será gerado em:

<pre class="overflow-visible! px-0!" data-start="2629" data-end="2666"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>outputs/remessa_maio_2026.txt</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

## 🧠 Regras de Negócio

### ✔ Lista Principal

* Paga apenas a parcela do mês atual (ex: Maio/2026)

---

### ✔ Retroativos

Pagamentos retroativos desde:

* Julho/2025 até Maio/2026

Valores aplicados:

| Ano  | Valor       |
| ---- | ----------- |
| 2025 | R$ 2.277,00 |
| 2026 | R$ 2.431,50 |

---

### 🚫 Prevenção de Duplicidade

* CPFs presentes na lista de retroativos são removidos da lista principal
* Evita pagamento duplicado

---

### 🔒 Tratamento de Dados

* Normalização de CPF
* Remoção de valores nulos
* Padronização para 11 dígitos

---

## 📊 Exemplo de Saída

<pre class="overflow-visible! px-0!" data-start="3266" data-end="3398"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>✅ REMESSA GERADA COM SUCESSO</span><br/><br/><span>Registros: </span><span class="ͼq">21500</span><br/><span>Valor total: R</span><span class="ͼt">$ 52</span><span>.000.000,00</span><br/><span>Código inicial: </span><span class="ͼq">197894</span><br/><span>Código final: </span><span class="ͼq">220394</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

## 🛠️ Tecnologias Utilizadas

* Python 3.12
* Pandas
* OpenPyXL
* TQDM

---

## 💼 Aplicação Real

Este projeto foi desenvolvido para um cenário real de processamento de pagamentos em lote, com regras específicas de negócio e integração com padrão bancário CNAB da CAIXA.

---

## 📌 Próximas Melhorias

* Validação automática de arquivos Excel
* Relatório detalhado em Excel
* Integração com retorno CNAB
* Interface via linha de comando (CLI)

---

## 👨‍💻 Autor

**Lincoln Rocha**

---

## 🚀 Como Executar

### 1. Instalar dependências

<pre class="overflow-visible! px-0!" data-start="1870" data-end="1914"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>pip install pandas openpyxl tqdm</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

### 2. Organizar arquivos

Coloque os arquivos de entrada em:

<pre class="overflow-visible! px-0!" data-start="1984" data-end="2005"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>data/entrada/</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

Exemplo:

<pre class="overflow-visible! px-0!" data-start="2017" data-end="2093"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>data/entrada/Maio_2026.xlsx</span><br/><span>data/entrada/Retroativos_julho_2025.xlsx</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

### 3. Executar o sistema

<pre class="overflow-visible! px-0!" data-start="2127" data-end="2153"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>python main.py</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

### 4. Resultado

O arquivo será gerado em:

<pre class="overflow-visible! px-0!" data-start="2205" data-end="2242"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>outputs/remessa_maio_2026.txt</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

## 🧠 Regras de Negócio

### ✔ Lista Principal

* Paga apenas a parcela do mês atual (ex: Maio/2026)

---

### ✔ Retroativos

Pagamentos retroativos desde:

* Julho/2025 até Maio/2026

Valores aplicados:

| Ano  | Valor       |
| ---- | ----------- |
| 2025 | R$ 2.277,00 |
| 2026 | R$ 2.431,50 |

---

### 🚫 Prevenção de Duplicidade

* CPFs presentes na lista de retroativos são removidos da lista principal
* Evita pagamento duplicado

---

### 🔒 Tratamento de Dados

* Normalização de CPF
* Remoção de valores nulos
* Padronização para 11 dígitos

---

## 📊 Exemplo de Saída

<pre class="overflow-visible! px-0!" data-start="2842" data-end="2974"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>✅ REMESSA GERADA COM SUCESSO</span><br/><br/><span>Registros: </span><span class="ͼq">21500</span><br/><span>Valor total: R</span><span class="ͼt">$ 52</span><span>.000.000,00</span><br/><span>Código inicial: </span><span class="ͼq">197894</span><br/><span>Código final: </span><span class="ͼq">220394</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

## 🛠️ Tecnologias Utilizadas

* Python 3.12
* Pandas
* OpenPyXL
* TQDM

---

## 💼 Aplicação Real

Este projeto foi desenvolvido para um cenário real de processamento de pagamentos em lote, com regras específicas de negócio e integração com padrão bancário CNAB da CAIXA.

---

## 📌 Próximas Melhorias

* Validação automática de arquivos Excel
* Relatório detalhado em Excel
* Integração com retorno CNAB
* Interface via linha de comando (CLI)

---

## 👨‍💻 Autor

**Lincoln Rocha**
