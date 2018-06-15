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

# Step 5: Send Device MT-SMS Messages
send_sms = {
    "address": [
        DEVICE_IMSI
    ],
    "senderAddress": APP_NAME,
    "outboundSMSTextMessage": {
        "message": "AerFrame message hello"
    },
    "clientCorrelator": "1234",
    "senderName": "tester22"
}
send_sms_url = ("https://api.aerframe.aeris.com/smsmessaging/"
                "v2/{}/outbound/{}/requests?apiKey={}").format(ACCOUNT_ID, APP_NAME, APP_API_KEY)
req = requests.post(send_sms_url, json=send_sms)
print(req.text + '\n')
