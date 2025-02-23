import coloredlogs
import logging
import time
from logging.handlers import RotatingFileHandler

# Define new logging levels
SUCCESS_LEVEL_NUM = 35  # Between WARNING (30) and ERROR (40)
FAILED_LEVEL_NUM = 36
logging.addLevelName(SUCCESS_LEVEL_NUM, "SUCCESS")
logging.addLevelName(FAILED_LEVEL_NUM, "FAILED")

# Add custom logging methods for SUCCESS and FAILED levels
def success(self, message, *args, **kws):
    if self.isEnabledFor(SUCCESS_LEVEL_NUM):
        self._log(SUCCESS_LEVEL_NUM, message, args, **kws)
logging.Logger.success = success

def failed(self, message, *args, **kws):
    if self.isEnabledFor(FAILED_LEVEL_NUM):
        self._log(FAILED_LEVEL_NUM, message, args, **kws)
logging.Logger.failed = failed

# Function to create and configure a logger
def get_logger(name: str, level: int = logging.DEBUG):
    # Create and configure the logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Configure field styles for coloredlogs
    field_styles = coloredlogs.DEFAULT_FIELD_STYLES
    field_styles['levelname'] = {'color': 11}  # Set the color for the level name

    # Configure level styles for coloredlogs
    level_styles = coloredlogs.DEFAULT_LEVEL_STYLES
    level_styles['debug'] = {'color': 'yellow', 'bold': True}       # DEBUG: yellow + bold
    level_styles['info'] = {'color': 'cyan'}                     # INFO: cyan
    level_styles['warning'] = {'color': 'yellow', 'bold': True}  # WARNING: yellow + bold
    level_styles['error'] = {'color': 'red', 'bold': True}       # ERROR: red + bold
    level_styles['critical'] = {'color': 'magenta', 'bold': True} # CRITICAL: magenta + bold
    level_styles['success'] = {'color': 'green', 'bold': True}   # SUCCESS: green + bold
    level_styles['failed'] = {'color': 'red', 'bold': True}      # FAILED: red + bold

    

    # Install coloredlogs for terminal output
    coloredlogs.install(
        fmt='%(asctime)s %(message)s',  # Log format: timestamp + message
        datefmt='%Y-%m-%d %H:%M:%S',    # Date format for timestamp
        level=level,                    # Set the logging level
        logger=logger,                  # Apply to this logger
        field_styles=field_styles,      # Apply field styles
        level_styles=level_styles       # Apply level styles
    )

    return logger

# Timer class to measure execution time of code blocks
class Timer:
    def __init__(self, description):
        self.description = description
        self.logger = get_logger('Timer')
    
    def __enter__(self):
        self.start = time.time()
        print('')  # Print a blank line for better readability
        self.logger.info('=' * 15 + f"{self.description} starts." + '=' * 15)
        return self
    
    def __exit__(self, type, value, traceback):
        self.end = time.time()
        self.logger.info('=' * 10 + f"{self.description} ends. Cost {self.end - self.start} seconds" + '=' * 10)
        print('')  # Print a blank line for better readability

# Main program
if __name__ == '__main__':
    with Timer('logger'):
        logger = get_logger('logger_test')
        logger.debug('This is a debug message')  # DEBUG level
        logger.info('This is an info message')   # INFO level
        logger.warning('This is a warning message')  # WARNING level
        logger.error('This is an error message')     # ERROR level
        logger.critical('This is a critical message')  # CRITICAL level
        logger.success('This is a success message')  # Custom SUCCESS level
        logger.failed('This is a failed message')    # Custom FAILED level