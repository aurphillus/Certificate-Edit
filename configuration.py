import configparser
import os

def create_config():
    default_path = os.getcwd()
    config = configparser.ConfigParser()
    config['PATH'] = {
        "parentdirectory": default_path,
    }
    config ['EXTENSIONS'] = {
        "acceptedextensions": 'jpeg,png,jpg'
    }
    config['DIRECTORY'] = {
        "input": "injest",
        "output": "output",
        "log": "logs",
        "default": "default",
        "temporary": "temporary",
    }
    config['IMAGE'] = {
        'basewidth': 1276,
        'defaultbackground': 'transparent.png',
        'defaultbackgroundlink':'https://pasteboard.co/JiXOlCH.png'
    }
    with open("config.ini","w") as configfile:
        config.write(configfile)

def load_config():
    if os.path.exists("config.ini"):
        config = configparser.ConfigParser()
        config.read("config.ini")
        # Checking config     
        try: 
            if config['PATH']['parentdirectory'] and config['EXTENSIONS']['acceptedextensions'] and config['DIRECTORY']['input'] and config['DIRECTORY']['output'] and config['DIRECTORY']['log'] and config['IMAGE']['basewidth'] and config['IMAGE']['defaultbackground'] and config['DIRECTORY']['DEFAULT'] and config['IMAGE']['defaultbackgroundlink']:
                config={
                    'parentdirectory': config['PATH']['parentdirectory'],
                    'extensions': config['EXTENSIONS']['acceptedextensions'].split(','),
                    'input_directory': config['DIRECTORY']['input'],
                    'output_directory': config['DIRECTORY']['output'],
                    'logs_directory': config['DIRECTORY']['log'],
                    'basewidth': config['IMAGE']['basewidth'],
                    'transparentbackground': config['IMAGE']['defaultbackground'],
                    'default_directory': config['DIRECTORY']['default'],
                    'defaultbackgroundlink': config['IMAGE']['defaultbackgroundlink'],
                }
                return config
            else:
                print(f"#. Problem with config file.")
                print(f"#. Resetting config file.")
                
                if os.path.exists("config.ini"):
                    os.remove("config.ini")
                
                print(f"#. Generating new default config file")
                create_config()
                load_config()
        except Exception as e:
            
            print(f"#. Problem with config file.")
            print(f"#. Resetting config file.")
            if os.path.exists("config.ini"):
                os.remove("config.ini")
                print(f"#. Generating new default config file")
                create_config()
                load_config()
    else:
        print(f"#. Creating new config file.")
        print(f"#. Generating new default config file")
        create_config()
        load_config()
