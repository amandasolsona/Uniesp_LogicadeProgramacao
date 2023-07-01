#Terminal -> pip install loguru
#file - settings - nome da pasta - project interpreter

from loguru import logger

# logger.info('Info')
# logger.warning('Warning')
# logger.error('Error')
# logger.debug('Debug')
# logger.add('Add')

from datetime import datetime
print(f'{datetime.now()} - Adicionou o usuário ! ')