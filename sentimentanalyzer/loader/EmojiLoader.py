import os

from numpy import mean, round
from pandas import read_csv
from nltk.tokenize import word_tokenize

from logger.logger import Logger


class EmojiLoader:
    """
    load (error handling), DataFrame, extract list of emojis, implement emoji tracer
    """
    __FILE_PATH = "../../data/Emoji_Dataset.csv"

    def __init__(self):
        """
        """
        self.__logger = Logger(name='emoji_logger')
        self.__df = self.__load()
        self.__emoji_table = self.__build_collection()

    def __load(self):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, self.__FILE_PATH)
        return read_csv(filename, index_col=None)

    def __build_collection(self):
        return {row.Char: row.Sentiment for index, row in self.__df.iterrows()}

    def __emoji_sentiment_score(self, emoji):
        return self.__emoji_table.get(emoji)

    def __extract_emoticons(self, sentence):
        """

        :param sentence:
        :return: Filtered sentence, list with emojis and scores
        """
        print("Initial sentence: {}".format(sentence))
        words = word_tokenize(sentence)
        elements = list()

        for index, word in enumerate(words):
            if word in self.__emoji_table:
                elements.append(words.pop(index))

        print("Detokenized Sentence: {}".format(self.__detokenize_sentence(words)))
        print("Elements found: {}".format(elements))
        return self.__detokenize_sentence(words), elements

    def __detokenize_sentence(self, words):
        """
        Unfortunately the folks over at NLTK, were using until recently MoseTokenizer that was licensed
        under LGPL license. Since they realised their mistake they remove the detokenizer from their
        source code and an alternative has not yet implemented. So, we have to use a custom way.
        :param words:
        :return:
        """
        return "".join([" " + w for w in words]).strip()

    def __sentiment_score(self, emojis):
        return [[e, self.__emoji_sentiment_score(e)] for e in emojis]

    def __calculate_average(self, emojis):
        scores = [s[1] for s in emojis]
        return round(mean(scores), 4)

    def __validate_sentence(self, sentence):
        if sentence is None or len(sentence) == 0:
            print("Invalid sentence")
            return False
        return True

    def sentiment_analyze_detailed(self, sentence):
        if self.__validate_sentence(sentence):
            filtered_sentence, emojis = self.__extract_emoticons(sentence)
            if not emojis:
                print("Sentence does not contain any emojis.")
                return 0
            else:
                emoji_table = self.__sentiment_score(emojis)
                average = self.__calculate_average(emoji_table)
                return emoji_table, average

    def sentiment_analyze(self, sentence):
        if self.__validate_sentence(sentence):
            filtered_sentence, emojis = self.__extract_emoticons(sentence)
            if not emojis:
                print("Sentence does not contain any emojis.")
                return 0
            else:
                return self.__calculate_average(self.__sentiment_score(emojis))
