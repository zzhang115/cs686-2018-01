from logger import logger

class file_logger(logger):
    

    """
    Constructor
    """
    def __init__(self, log_level, file_name = 'file_log.txt'):
        self.__log_level__ = log_level
        self.__file__ = open(file_name, 'a+')

    """
    log
    Logs the message if log_level is less than or equal to
    the class' threshold. (In this case: does nothing.)
    """
    def log(self, log_level, message):
        if log_level <= self.__log_level__:
            self.__file__.write(str(log_level) + ':' + message + '\n')
        return

