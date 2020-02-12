
import os
from configparser import ConfigParser
from dotenv import load_dotenv
from os import getenv

class Config:

    def __init__(self):
        # determine where this file is located
        file_dir = os.path.dirname(__file__)
        filename = file_dir + '/config.cfg'

        # Load the config from "this" directory
        # This will work regardless of python's working directory
        self.config = ConfigParser()
        self.config.read(filename)

        load_dotenv()
        self.secret = int(getenv('secret'))

    def get_delay(self):
        return int(self.config['DEFAULT']['delay'])

    def get_secret(self):
        return self.secret
