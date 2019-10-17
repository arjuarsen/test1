import configparser
configParser = configparser.RawConfigParser()   
configFilePath = r'config.txt'
configParser.read(configFilePath)
self.env= configParser.get('env')
