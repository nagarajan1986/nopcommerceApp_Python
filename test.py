import logging


logging.basicConfig(filename="D://Logs//automation.log",format='%(asctime)s: %(levelname)s: %(message)s')
logger=logging.getLogger()
logger.setLevel(logging.INFO)

logger.info("This is info message")
