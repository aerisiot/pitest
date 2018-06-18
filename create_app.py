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

# Step 1: Create an Application
create_app = {
    "applicationName": APP_NAME + "-pi001atbk",
    "applicationShortName": APP_NAME,
    "applicationTag": "aerframe",
    "description": "using AerFrame on Pi"
}
create_app_url = ("https://api.aerframe.aeris.com/registration/"
                  "v2/{}/applications?apiKey={}").format(ACCOUNT_ID, ACCOUNT_API_KEY)
req = requests.post(create_app_url, json=create_app)
print(req.text + '\n')
APP_API_KEY = req.json()["apiKey"]
config.set("aerframe", "app_api_key", APP_API_KEY)
with open('config.ini', 'w') as configfile:
    config.write(configfile)

# Step 2: Create a Notification Channel
create_channel = {
    "applicationTag": "aerframe",
    "channelData": {
        "maxNotifications": "1",
        "type": "nc:LongPollingData"
    },
    "channelLifetime": "7200",
    "channelType": "LongPolling",
    "clientCorrelator": "1234"
}
create_channel_url = ("https://api.aerframe.aeris.com/notificationchannel/"
                      "v2/{}/channels?apiKey={}").format(ACCOUNT_ID, APP_API_KEY)
req = requests.post(create_channel_url, json=create_channel)
print(req.text + '\n')
CALLBACK_URL = req.json()["callbackURL"]

# Step 3: Create Inbound SMS Subscription
inbound_sub = {
    "callbackReference": {
        "callbackData": "pitest-mosub1",
        "notifyURL": CALLBACK_URL
    },
    "criteria": "SP:*",
    "destinationAddress": [
        APP_NAME
    ]
}
inbound_sub_url = ("https://api.aerframe.aeris.com/smsmessaging/"
                   "v2/{}/inbound/subscriptions?apiKey={}").format(ACCOUNT_ID, APP_API_KEY)
req = requests.post(inbound_sub_url, json=inbound_sub)
print(req.text + '\n')

# Step 4: Create Outbound SMS Subscription
outbound_sub = {
    "callbackReference": {
        "callbackData": "pitest-mtsub1",
        "notifyURL": CALLBACK_URL
    },
    "filterCriteria": "SP:*"
}
outbound_sub_url = ("https://api.aerframe.aeris.com/smsmessaging/"
                    "v2/{}/outbound/{}/subscriptions?apiKey={}").format(ACCOUNT_ID, APP_NAME, APP_API_KEY)
req = requests.post(outbound_sub_url, json=outbound_sub)
print(req.text + '\n')
