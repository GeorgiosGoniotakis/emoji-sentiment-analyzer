# coding: utf-8
# !/usr/bin/env python

"""
This is the file containing the implementation of the ConfigLoader class.
"""

import configparser

from logger.logger import Logger


class ConfigLoader:
    """
    This class contains a simple constructor in order to keep track of the
    configurations across multiple instances which use them.
    """

    def __init__(self):
        """
        A simple constructor that keeps track of the configurations.
        """
        self.conf = None
        self.__logger = Logger(name='Config Loader')

    def get_configurations(self):
        """
        Retrieves the credentials from the config.ini file
        """

        # Retrieve configurations from config.ini file
        cfg = configparser.ConfigParser()
        cfg.read("../config.ini")

        # TODO: Load all different configs here
        if "logging" in cfg:
            self.conf = dict(cfg.items('logging'))
            self.__logger.log(message="Successfully loaded settings from config.ini", mtype="INFO")
        else:
            self.__logger.log(message="Wrong configurations in file: config.ini", mtype="CRITICAL")
            exit(100)

    def reset_config_file(self):
        try:
            with open("../config.ini", 'w') as file:
                file.write(";This file includes all the logging parameters of the project. \n;"
                           "Please modify as preferred.\n[logging]\nlogger=true\nlevel=DEBUG")
                print("Successfully reset config file.")
                file.close()
        except Exception as e:
            print("Problem resetting config file. Error Message: " + str(e))
            exit(104)
