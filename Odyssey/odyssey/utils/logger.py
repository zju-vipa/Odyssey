import coloredlogs, logging
import time
# Define a new logging level
SUCCESS_LEVEL_NUM = 35  # Between WARNING (30) and ERROR (40)
FAILED_LEVEL_NUM = 36
logging.addLevelName(SUCCESS_LEVEL_NUM, "SUCCESS")
logging.addLevelName(FAILED_LEVEL_NUM, "FAILED")

def success(self, message, *args, **kws):
    if self.isEnabledFor(SUCCESS_LEVEL_NUM):
        self._log(SUCCESS_LEVEL_NUM, message, args, **kws)
logging.Logger.success = success

def failed(self, message, *args, **kws):
    if self.isEnabledFor(FAILED_LEVEL_NUM):
        self._log(FAILED_LEVEL_NUM, message, args, **kws)
logging.Logger.failed = failed

def get_logger(name: str, level: int = logging.DEBUG):
    # Configure coloredlogs
    field_styles = coloredlogs.DEFAULT_FIELD_STYLES
    field_styles['levelname'] = {'color': 11}  # Set the color for the custom level

    level_styles = coloredlogs.DEFAULT_LEVEL_STYLES
    level_styles['success'] = {'color': 'green', 'bold': True}
    level_styles['failed'] = {'color': 'red', 'bold': True}

    logger = logging.getLogger(name)
    logger.setLevel(level)
    coloredlogs.install(
        fmt='%(asctime)s %(message)s',datefmt='%Y-%m-%d %H:%M:%S',
        level=level, logger=logger, field_styles=field_styles, level_styles=level_styles
    )
    return logger



class Timer:
    def __init__(self, description):
        self.description = description
        self.logger = get_logger('Timer')
    
    def __enter__(self):
        self.start = time.time()
        print('')
        self.logger.info('='*15+f"{self.description} starts."+'='*15)
        return self
    
    def __exit__(self, type, value, traceback):
        self.end = time.time()
        self.logger.info('='*10+f"{self.description} ends. Cost {self.end - self.start} seconds"+'='*10)
        print('')


if __name__ == '__main__':
    with Timer('logger'):
        logger = get_logger('logger_test')
        logger.success('success')
        logger.failed('failed')
        logger.critical('critical')
        logger.debug('debug'*20)