import logging
import logging.handlers

LOG_FILENAME = 'logging_sample/hoge.log'

logger = logging.getLogger('hogelog')
log_rotator = logging.handlers.TimedRotatingFileHandler(LOG_FILENAME, when='d')
logger.addHandler(log_rotator)
logger.handlers[0].doRollover()

for i in range(1000):
    logger.error("fugafuga")

