"""

"""

from logger.logger import Logger
from data.EmojiLoader import EmojiLoader
from config.config import ConfigLoader

__author__ = "Georgios Goniotakis"
__email__ = "georgios.goniotakis@outlook.com"
__version__ = "1.0"
__status__ = "Development"  # TODO: Connect this to config file


def main():
    logger = Logger(name='emoji_logger', mode='DEBUG', out='hey.log')
    emoji_loader = EmojiLoader("some")
    config_loader = ConfigLoader()
    conf = config_loader.conf


if __name__ == '__main__':
    main()
