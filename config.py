import os, json

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    with open('firebase_config.json', 'r') as f, open('dialogflow_config.json', 'r') as f2:
        FIREBASE_CONFIG_JSON = json.loads("".join(f.readlines()))
        DIALOGFLOW_CONFIG_JSON = json.loads("".join(f2.readlines()))