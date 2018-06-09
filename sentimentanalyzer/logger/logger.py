import os

import inspect
import datetime
import coloredlogs
import logging


# TODO: Comments here
class Logger:
    def __init__(self, name: str, mode='DEBUG', out=None):
        self.__logger = None
        self.__name = name
        self.__mode = mode
        self.__out = out
        self.__create_directory()
        self.setup_logger()

    def __create_directory(self):
        try:
            if not os.path.exists("logs"):
                os.makedirs("logs")
        except Exception as e:
            print("Problem creating log directory. Error Message: " + str(e))
            exit(103)

    def setup_logger(self):
        self.__logger = logging.getLogger(self.__name)
        coloredlogs.install(level='DEBUG', logger=self.__logger)

        # If output file path is set add handler
        if self.__out:
            fh = logging.FileHandler("logs/" + self.__out)
            fh.setLevel(self.__mode)
            self.__logger.addHandler(fh)

    def log(self, message, mtype="DEBUG"):

        func = inspect.currentframe().f_back.f_code
        log_message = "Date: {}, Message: '{}', File: '{}', line {}, in method {}".format(
            str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            message, func.co_filename,
            func.co_firstlineno,
            func.co_name)

        if mtype == "INFO":
            self.__logger.info(log_message)
        elif mtype == "WARN":
            self.__logger.warn(log_message)
        elif mtype == "EROOR":
            self.__logger.error(log_message)
        elif mtype == "CRITICAL":
            self.__logger.critical(log_message)
        else:
            self.__logger.debug(log_message)
