import ConfigParser
configParser = ConfigParser.RawConfigParser()   
configFilePath = r'config.txt'
configParser.read(configFilePath)
config()
self.env= configParser.get('your-config','env')
 
