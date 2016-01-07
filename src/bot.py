"""
basic slack-bot created by Shane Engelman <me@5h4n3.com>
"""

import lib.irc as irc_
import sys
import datetime
import traceback
import time
import os
import src.config.config as config
from threading import Thread
from lib.functions_general import *
import src.lib.incoming_data as incoming_data
import src.lib.cron as cron
import requests
import sys
reload(sys)
sys.setdefaultencoding("utf8")


class Roboraj(object):

    def __init__(self, config):
        self.config = config  # use config.py as this instance's config
        self.irc = irc_.irc(config)  # use irc.py for socket connections
        incoming_data.initialize(self.irc, self.config.get('channels', {}))

    def run(self):
        while True:  # main event loop
            pass
