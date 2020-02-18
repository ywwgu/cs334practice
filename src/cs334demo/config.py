
import os
from configparser import ConfigParser
from dotenv import load_dotenv
from os import getenv

class Config:

    def get_delay(self):
        return 100

    def get_secret(self):
        return 42
