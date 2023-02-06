from configparser import ConfigParser

config = ConfigParser()

config.read('config.ini')

api_id = config.get('pyrogram', 'api_id')
api_number = config.get('pyrogram', 'api_number')
api_hash = config.get('pyrogram', 'api_hash')

token = config.get('aiogram','token')