from source.logger.logger import Logger

import urllib3


class EmojiLoader:

    FILE_URL = "http://unicode.org/Public/emoji/11.0/"

    # TODO: Implement mode
    def __init__(self, mode):
        """

        :param mode: Either load from file or from web address
        """
        self.__logger = Logger(name='emoji_logger')
        self.data = self.load()

    def load(self):

        try:
            http = urllib3.PoolManager()
            r = http.request('GET', self.FILE_URL)

            if r.status != 200:
                self.__logger.log(message="Problem loading data using HTTP. Error code: " + r.status, mtype="CRITICAL")
                exit(102)
            self.__logger.log(message="Successfully loaded source dataset from URL", mtype="INFO")
            return r.data
        except Exception as e:
            self.__logger.log(message="Problem performing HTTP request. Error message: " + str(e), mtype="CRITICAL")
            exit(101)
