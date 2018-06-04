from source.logger.logger import Logger
from source.codes.general import error_codes as c

import urllib3


class EmojiLoader:
    FILE_URL = "http://unicode.org/Public/emoji/11.0/"

    def __init__(self, mode):
        self.__logger = Logger(name='emoji_logger')
        self.data = self.load()


    def load(self):

        try:
            http = urllib3.PoolManager()
            r = http.request('GET', self.FILE_URL)

            if r.status != 200:
                self.__logger.log(message="Problem loading data using HTTP. Error code: " + r.status, mtype="CRITICAL")
                exit(c()[100])
            self.__logger.log(message="Successfully loaded source dataset from URL", mtype="INFO")
            return r.data
        except Exception as e:
            self.__logger.log(message="Problem performing HTTP request. Error message: " + str(e), mtype="CRITICAL")
            exit(c()[101])

