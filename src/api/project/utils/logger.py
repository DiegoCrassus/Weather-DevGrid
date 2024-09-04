from loguru import logger


class ControllLog:
    def __init__(self):
        print("ControllLog class for log controll")

    @staticmethod
    def debug(messages):
        """
        Informações interessantes para desenvolvedores, ao tentar depurar um problema.
        """
        logger.debug("[+] - {}".format(messages))

    @staticmethod
    def info(messages):
        """
        Informações interessantes para a equipe de suporte que tenta
        descobrir o contexto de um determinado erro.
        """
        logger.info("[+] - {}".format(messages))

    @staticmethod
    def success(messages):
        logger.success("[-] - {}".format(messages))

    @staticmethod
    def warning(messages):
        """
        declarações que descrevem eventos ou estados potencialmente prejudiciais no programa.
        """
        logger.warning("[-] - {}".format(messages))

    @staticmethod
    def error(messages):
        """
        declarações que descrevem erros não fatais no aplicativo; esse nível é
        usado com bastante frequência para registrar exceções tratadas.
        """
        logger.error("[-] - {}".format(messages))

    @staticmethod
    def critical(messages):
        """
        declarações que representam as condições de erro mais graves,
        supostamente resultando no encerramento do programa.
        """
        logger.critical("[-] - {}".format(messages))
