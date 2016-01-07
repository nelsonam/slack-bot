import time
from threading import Thread


def initialize(irc, config):
    for channel, jobs in config.items():
        if not jobs:
            continue

        for (delay, enabled, callback) in jobs:
            if not enabled:
                continue

            CronJob(irc, channel, delay, callback).start()


class CronJob(Thread):

    def __init__(self, irc, channel, delay, callback):
        Thread.__init__(self)
        self.daemon = True
        self.delay = delay
        self.callback = callback
        self.irc = irc
        self.channel = channel

    def run(self):
        while True:
            time.sleep(self.delay)
            self.irc.send_message(self.channel, self.callback(self.channel))
