### Teste se o main.py está sendo executando no terminal

'''
def main():
    print("✅ O main.py está sendo executado!")

main()

'''
from email_reader import buscar_emails_com_fatura
from pdf_processor import extrair_dados_fatura
from sap_api import criar_po_sap
from utils import setup_logger

logger = setup_logger()

def main():
    logger.info("Iniciando automação de criação de PO no SAP.")

    # Simulação da leitura de e-mails
    anexos_pdf = buscar_emails_com_fatura()

    for pdf_path in anexos_pdf:
        try:
            dados_fatura = extrair_dados_fatura(pdf_path)
            response = criar_po_sap(dados_fatura)
            logger.info(f"PO criada com sucesso: {response}")
        except Exception as e:
            logger.error(f"Erro ao processar {pdf_path}: {str(e)}")

if __name__ == "__main__":
    main()

