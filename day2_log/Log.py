import os
import logging
from datetime import datetime
import threading

proDir = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))

class Log:
    def __init__(self):
        global logPath, resultPath, proDir
        resultPath = os.path.join(proDir, "output")
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        # defined config
        logging.basicConfig(format='%(asctime)s-%(pathname)s[line:%(lineno)d]-%(levelname)s: %(message)s', level=logging.DEBUG)
        self.logger = logging.getLogger()
        # defined handler
        handler = logging.FileHandler(os.path.join(logPath, "output.log"))
        # defined formatter
        formatter = logging.Formatter('%(asctime)s-%(pathname)s[line:%(lineno)d]-%(levelname)s: %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def get_logger(self):
        """
        get logger
        :return:
        """
        return self.logger


    def get_report_path(self):
        """
        get report file path
        :return:
        """
        report_path = os.path.join(logPath, "report.html")
        return report_path

    def get_result_path(self):
        """
        get test result path
        :return:
        """
        return logPath

    def write_result(self, result):
        """

        :param result:
        :return:
        """
        result_path = os.path.join(logPath, "report.txt")
        fb = open(result_path, "wb")
        try:
            fb.write(result)
        except FileNotFoundError as ex:
            logger.error(str(ex))


class ZLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():
        if ZLog.log is None:
            ZLog.mutex.acquire()
            ZLog.log = Log()
            ZLog.mutex.release()

        return ZLog.log


if __name__ == "__main__":
    log = ZLog.get_log()
    logger = log.get_logger()
    logger.debug("test debug")
    logger.info("test info")
