import os
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")


class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath, encoding='utf-8')

    def get_censign(self, name):
        value = self.cf.get("CENSIGN", name)
        return value

    def get_netsign(self, name):
        value = self.cf.get("NETSIGN", name)
        return value


if __name__ == "__main__":
    aa = ReadConfig()
    value = aa.get_censign('port')
    print(value)
