from app.logger_config import setup_logger
from app.Processo import executar_processo

logger = setup_logger()


if __name__ == "__main__":
    logger.info("Iniciando automação de criação de PO no SAP.")
    executar_processo()
    logger.info("✅ Processamento finalizado")
