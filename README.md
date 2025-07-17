# 💼 Desafio Técnico – Automação para Criação de PO no SAP

## 📌 Objetivo

Automatizar o processo de leitura de faturas de energia elétrica recebidas por e-mail e criação de Ordens de Compra (PO) no SAP S/4HANA, simulando a integração via API.

---

## ⚙️ Como executar o projeto

Clone ou extraia o projeto:

Coloque os arquivos em uma pasta local, por exemplo:


Desafio_Automacao_DouglasMendes/
Crie e ative um ambiente virtual (opcional, mas recomendado):

bash

python -m venv venv
venv\Scripts\activate  # Windows
Instale as dependências:

bash

pip install -r requirements.txt
Configure as variáveis de ambiente:

Crie um arquivo .env na raiz do projeto com os dados:

ini

EMAIL_USER=seu_email@gmail.com
EMAIL_PASS=sua_senha_de_app
EMAIL_SERVER=imap.gmail.com
⚠️ Use uma senha de app do Gmail com autenticação em 2 etapas ativada.

Rode o script principal:

bash

python main.py
Saída esperada:

O script irá:

Acessar sua caixa de entrada

Buscar e-mails não lidos com anexos PDF

Salvar os PDFs na pasta /anexos

Simular a extração de dados das faturas

Simular o envio da PO para a API SAP

Registrar tudo em logs (app.log e terminal)


### Teste realizado com sucesso com o meu gmail

2025-07-08 11:55:20,746 - INFO - Iniciando automação de criação de PO no SAP.
🔐 Conectando ao e-mail douglasms118@gmail.com via imap.gmail.com...
📥 Buscando e-mails não lidos com anexos...
📧 E-mail encontrado: ENC: Teste de fatura
📎 Anexo encontrado: fatura_teste.pdf
✅ PDF salvo: anexos/fatura_teste.pdf
📧 E-mail encontrado: “Analista de automação”: Netvagas - Analista de automacao e inovacao ia vaga afirmativa para mulheres pretas pardas e indigenas
📎 Anexo encontrado: 
📎 Anexo encontrado: 
📧 E-mail encontrado: “técnico mecatronica”: Netvagas - Tecnico em mecatronica equipamento medico hospitalar
📎 Anexo encontrado: 
📎 Anexo encontrado: 
📧 E-mail encontrado: 🔥 Ofertas imperdíveis que você não vai querer perder!
📧 E-mail encontrado: A Seleção de Moda Masculina chegou!
📧 E-mail encontrado: 12 vagas novas para “powershell automation“
📎 Anexo encontrado:
📎 Anexo encontrado:
📧 E-mail encontrado: Uma pessoa no cargo de Recruiter viu
📎 Anexo encontrado:
📎 Anexo encontrado:
📧 E-mail encontrado: Novas vagas semelhantes à de Analista de automação na Orizon
📎 Anexo encontrado:
📎 Anexo encontrado:
📧 E-mail encontrado: Liquida de Férias 7.7！
📧 E-mail encontrado: “técnico mecatronica”: Moderna Emprego - Técnico em mecatrônica - SP e mais
📎 Anexo encontrado:
📎 Anexo encontrado:
📊 Total de PDFs encontrados: 1
Simulando envio da PO com dados: {'cnpj': '12.345.678/0001-90', 'contrato': '12345678', 'valor': 450.75, 'vencimento': '15/07/2025'}
2025-07-08 11:55:29,286 - INFO - PO criada com sucesso: {'status': 200, 'message': 'PO criada (simulada)'}


```bash
cd Desafio_Automacao_DouglasMendes

### Arquitetura de software de automação 

Desafio_Automacao_DouglasMendes/
├── main.py                  ✅ Arquivo principal que executa a automação
├── email_reader.py          ✅ Faz a leitura de e-mails via IMAP
├── pdf_processor.py         ✅ Extrai os dados dos PDFs
├── sap_api.py               ✅ Faz a simulação do envio para o SAP
├── utils.py                 ✅ Logger e utilitários
├── requirements.txt         ✅ Lista das bibliotecas usadas no projeto
├── README.md                ✅ Explicação do projeto e instruções
├── .env                     ✅ Suas credenciais de e-mail (Arquivo não enviado - será necessário criar para rodar o main.py)
├── anexos/                  ✅ Pasta onde os PDFs serão salvos
│   └── (vazia ou com PDFs)  ✅ Pode começar vazia


### procedimento para usar o IMAP com python 

✅ Etapa 1: Acessar a conta Google
Acesse: 👉 https://myaccount.google.com/security

Faça login com seu Gmail (ex: Seu_e-mail@gmail.com) se ainda não estiver logado.

✅ Etapa 2: Ativar a Verificação em Duas Etapas (2FA)
Na tela de segurança:

Role até a seção "Como fazer login no Google".

Clique em "Verificação em duas etapas".

Clique em "Começar".

Faça login novamente, se solicitado.

✅ Etapa 3: Configurar a segunda etapa de verificação
Você pode escolher um método de autenticação secundário, como:

Telefone (SMS ou notificação no celular) — mais fácil.

Chave de segurança física (opcional).

📱 A mais comum é SMS ou notificação no celular Android.

Siga os passos:
Escolha o número de telefone.

Receba o código por SMS ou notificação.

Digite o código para confirmar.

✅ Etapa 4: Concluir ativação
Depois de confirmar, clique em "Ativar".

Agora, sua conta já tem 2FA ativado ✅

✅ Etapa 5: Gerar Senha de App
Acesse: 👉 https://myaccount.google.com/apppasswords

Faça login novamente.

Em "Selecionar aplicativo", escolha: "Outro (nome personalizado)".

Digite um nome como: automacao-python e clique em "Gerar".

O Google vai te mostrar uma senha assim:

Senha: abcd efgh ijkl mnop

### Informações pasta anexos/ 

Na pasta anexo deixei o arquivo que foi usado para o teste em .PDF

