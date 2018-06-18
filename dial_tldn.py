#!/usr/bin/env python
import configparser
import requests

config = configparser.ConfigParser()
config.read("config.ini")

DEVICE_IMSI = config["aerframe"]["device_imsi"]
ACCOUNT_ID = config["aerframe"]["account_id"]
ACCOUNT_API_KEY = config["aerframe"]["account_api_key"]
APP_API_KEY = config["aerframe"]["app_api_key"]
APP_NAME = config["aerframe"]["app_name"]

get_tldn_url = ("https://api.aerframe.aeris.com/networkservices/"
                "v2/{}/devices/imsi/{}/localDialableNumber?apiKey={}").format(ACCOUNT_ID, DEVICE_IMSI, APP_API_KEY)
req = requests.get(get_tldn_url)
print(req.url + "\n")
print(req.text + "\n")
