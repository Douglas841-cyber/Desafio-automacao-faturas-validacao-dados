import logging

def setup_logger():
    logger = logging.getLogger("automacao")
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Evita múltiplos handlers duplicados
    if not logger.handlers:

        # Handler para exibir logs no terminal
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # Handler para salvar logs no arquivo app.log
        file_handler = logging.FileHandler("app.log")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger