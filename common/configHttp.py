import requests
import urllib3
import logging.config
import readConfig as readConfig
import common.log

localReadConfig = readConfig.ReadConfig()
logging.config.dictConfig(common.log.LOGGING_DIC)
logger = logging.getLogger(__name__)


class ConfigHttp:
    def __init__(self):
        global host, port, timeout
        host = localReadConfig.get_censign("host")
        port = localReadConfig.get_censign("port")
        timeout = localReadConfig.get_censign("timeout")
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}

    def set_url(self, url):
        self.url = host + ":" + port + url

    def set_header(self, header):
        self.headers = header

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data

    def set_files(self, file):
        self.files = file

    # defined http get method
    def get(self):
        try:
            urllib3.disable_warnings()
            response = requests.get(self.url, params=self.params, headers=self.headers, timeout=float(timeout),
                                    verify=False)
            return response
        except TimeoutError:
            logger.error("Time Out!")
            return None


if __name__ == '__main__':
    c = ConfigHttp()
