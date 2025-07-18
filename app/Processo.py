### Teste se o main.py está sendo executando no terminal

'''
def main():
    print("✅ O main.py está sendo executado!")

main()

'''
from app.email_reader import buscar_emails_com_fatura
from app.pdf_processor import extrair_dados_fatura
from app.sap_api import criar_po_sap
from app.logger_config import setup_logger

logger = setup_logger()

def executar_processo():
    # Simulação da leitura de e-mails
    anexos_pdf = buscar_emails_com_fatura()

    for pdf_path in anexos_pdf:
        try:
            dados_fatura = extrair_dados_fatura(pdf_path)
            response = criar_po_sap(dados_fatura)
            logger.info(f"PO criada com sucesso: {response}")
        except Exception as e:
            logger.error(f"Erro ao processar {pdf_path}: {str(e)}")