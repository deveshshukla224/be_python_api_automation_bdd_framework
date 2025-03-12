from configparser import ConfigParser

def readfromglobalconf(section, key):
    config = ConfigParser()
    config.read('/home/devslane-75/Devesh/be_python_api_automation_bdd_framework/configurations/global_properties.ini')
    return config.get(section, key)


