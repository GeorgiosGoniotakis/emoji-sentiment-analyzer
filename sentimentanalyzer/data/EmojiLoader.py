from logger.logger import Logger

import pandas as pd


class EmojiLoader:
    """

    """
    FILE_URL = "https://unicode.org/Public/emoji/11.0/emoji-test.txt"

    # TODO: Remove mode, make it local
    def __init__(self, mode):
        """

        :param mode: Either load from file or from web address
        """
        self.__logger = Logger(name='emoji_logger')
        self.data = self.load()

    def load(self):

        try:
            d = pd.read_csv(self.FILE_URL, sep=" ", header=None)

            if d.status != 200:
                self.__logger.log(message="Problem loading data using HTTP. Error code: " + d.status, mtype="CRITICAL")
                exit(102)
            self.__logger.log(message="Successfully loaded source dataset from URL", mtype="INFO")
            return d
        except Exception as e:
            self.__logger.log(message="Problem performing HTTP request. Error message: " + str(e), mtype="CRITICAL")
            exit(101)
