import configparser

config=configparser.RawConfigParser()
config.read("C:\\Users\\Admin\\Desktop\\nopcommerce_project\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('commoninfo','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('commoninfo', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('commoninfo', 'password')
        return password