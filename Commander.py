from distutils.command.config import config
import json
import os
import pathlib

path = str(pathlib.Path(__file__).parent.resolve())
configjson = {}
currentproject = ''
proname = ''

def compilebydir(prodir):
    os.system(f'rm -rf {prodir}/tmp/')
    os.system(f'cp -r {prodir}/src/ {prodir}/tmp/ -f')

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
    
def main():
    os.system(f'cd {path}')
    getConfig()
    for (root, dirs, file) in os.walk(path+'/projects'):
        if(root==str(path)+'/projects'):
            for dir in dirs:
                proname = dir
                compilebydir(path+'/projects/'+dir)

if __name__=='__main__':
    main()