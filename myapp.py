import ConfigParser

 configparser = ConfigParser.RawConfigParser()   
 configFilePath = r'config.txt'
 configparser.read(configFilePath)
 config()
 self.env= configparser.get('your-config','env')
 
