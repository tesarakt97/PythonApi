import logging

logger = logging.getLogger("qa_logger")
logger.setLevel(logging.DEBUG)

# Вывод в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)
