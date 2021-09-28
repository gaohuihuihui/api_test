import logging
import os
import time

basic_path=os.path.dirname(os.path.dirname(__file__))

log_path=os.path.join(basic_path,"log")
if not os.path.exists(log_path):
    os.mkdir(log_path)


class Logger():

    def __init__(self):
        self.logname = os.path.join(log_path, "{}.log".format(time.strftime("%Y%m%d")))
        self.logger = logging.getLogger("log")
        self.logger.setLevel(logging.DEBUG)

        self.formater = logging.Formatter(
            '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')

        self.filelogger = logging.FileHandler(self.logname, mode='a', encoding="UTF-8")
        self.console = logging.StreamHandler()
        # self.console.setLevel(logging.DEBUG)
        # self.filelogger.setLevel(logging.DEBUG)
        self.filelogger.setFormatter(self.formater)
        self.console.setFormatter(self.formater)

        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)


Logger = Logger().logger


if __name__=="__main__":
    Logger.info("testlog")
