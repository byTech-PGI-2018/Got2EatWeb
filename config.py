import os, json

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    with open('firebase_config.json', 'r') as f:
        FIREBASE_CONFIG_JSON = json.loads("".join(f.readlines()))