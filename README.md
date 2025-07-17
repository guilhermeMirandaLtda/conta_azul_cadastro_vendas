# 🤖 ContaAzul Sales Bot

Automatize cadastros de vendas no sistema Conta Azul com facilidade e precisão usando Python + Playwright.

---

## 🚀 Visão Geral

Este projeto automatiza o processo de lançamento de vendas no Conta Azul, incluindo:

- Login automático
- Cadastro de cliente (ou seleção se já existir)
- Preenchimento dos itens da venda
- Escolha da forma de pagamento
- Escolha da conta bancária
- Seleção da parcela
- Preenchimento de detalhes adicionais
- Registro de tempo e logs por etapa

---

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- [Playwright](https://playwright.dev/python/)
- JSON para configurações
- Logs personalizados com `logger.py`

---

## 📦 Instalação

### 1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/conta_azul_cadastro_vendas.git
cd contaazul-sales-bot
```
### 2. Crie um ambiente virtual:

python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate.bat     # Windows

### 3. Instale as dependências:

pip install -r requirements.txt

### 4. Instale os navegadores do Playwright:

playwright install

## 🔐 Configuração
Edite o arquivo config.json com seu e-mail e senha do Conta Azul:

{
  "email": "seu_email@empresa.com",
  "senha": "sua_senha_segura"
}
⚠️ Nunca compartilhe este arquivo publicamente.

## ▶️ Como Usar
Execute o sistema com:

python main.py
Ele realizará o login e processará os dados da planilha para cadastrar a venda automaticamente.

## 📁 Estrutura do Projeto

📦 contaazul-sales-bot
├── bot/
│   ├── login.py
│   ├── cliente_section.py
│   ├── item_venda_section.py
│   ├── forma_pagamento_section.py
│   └── ...
├── utils/
│   └── logger.py
├── config.json
├── main.py
├── requirements.txt
└── README.md

## ✅ Checklist de Funcionalidades
 Login automatizado
 Cadastro e seleção de clientes
 Cadastro e seleção de itens de venda
 Seleção de forma de pagamento
 Seleção de conta de banco
 Escolha de parcelas
 Preenchimento de detalhes da venda
 Registro de logs e tempos

## 📌 Observações
A automação é sensível a mudanças no layout do Conta Azul.
Use com responsabilidade e apenas em contas autorizadas.
Este projeto é de uso pessoal/educacional.

📬 Contato
Desenvolvido por Guilherme Miranda
📧 guilherme.miranda.ltda@gmail.com
