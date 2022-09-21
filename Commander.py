from distutils.command.config import config
import json
import os
import pathlib

path = str(pathlib.Path(__file__).parent.resolve())
configjson = {}
currentproject = ''

def compilebydir(dir):
    print(dir)

def getConfig():
    configfilepath = str(path)+'/config/config.json'
    if not os.path.exists(configfilepath):
        print('the config file does not exits...')
        print('please create one at '+configfilepath+'.')
        exit()
    try:
        configjson = json.load(open(configfilepath, 'r'))
    except json.decoder.JSONDecodeError:
        print('json syntax invalvid...')
        print('please fix the config.')
        exit()
    print(configfilepath)
    
def main():
    getConfig()
    for (root, dirs, file) in os.walk(path+'/projects'):
        if(root==str(path)+'/projects'):
            for dir in dirs:
                compilebydir(dir)

if __name__=='__main__':
    main()