import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".//Logs//automation.log",format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
