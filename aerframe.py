#!/usr/bin/env python
import requests

ACCOUNT_ID = "11111"
ACCOUNT_API_KEY = "11111111-1111-1111-1111-111111111111"
APP_NAME = "pitest"
DEVICE_IMSI = "310170202463586"

# Step 1: Create an Application
create_app = {
    "applicationName": "pitest-pi001atbk",
    "applicationShortName": APP_NAME,
    "applicationTag": "aerframe",
    "description": "using AerFrame on Pi"
}
create_app_url = ("https://api.aerframe.aeris.com/registration/"
                  "v2/{}/applications?apiKey={}").format(ACCOUNT_ID, ACCOUNT_API_KEY)

req = requests.post(create_app_url, data=create_app)
APP_API_KEY = req.json()["apiKey"]

# Step 2: Create a Notification Channel
create_channel = {
    "applicationTag": "aerframe",
    "channelData": {
        "maxNotifications": "15",
        "type": "nc:LongPollingData"
    },
    "channelType": "LongPolling"
}
create_channel_url = ("https://api.aerframe.aeris.com/notificationchannel/"
                      "v2/{}/channels?apiKey={}").format(ACCOUNT_ID, ACCOUNT_API_KEY)
req = requests.post(create_channel_url, data=create_channel)

# Step 3: Create a Subscription for MT Delivery Notifications
notify_url = ("https://api.aerframe.aeris.com/notificationchannel/"
              "v2/{}/channels/{}/callback").format(ACCOUNT_ID, APP_API_KEY)
create_sub = {
    "callbackReference": {
        "callbackData": "mt-delivery-callback1",
        "notifyURL": notify_url
    },
    "filterCriteria": "SP:GPROD01"
}
create_sub_url = ("https://api.aerframe.aeris.com/smsmessaging/"
                  "v2/{}/inbound/subscriptions?apiKey={}").format(ACCOUNT_ID, APP_API_KEY)
req = requests.post(create_sub_url, data=create_sub)

# Step 4: Send Device MT-SMS Messages
send_sms = {
    "address": [DEVICE_IMSI],
    "senderAddress": APP_NAME,
    "outboundSMSTextMessage": {
        "message": "I am AerFrame 2.1"
    },
    "clientCorrelator": "123456",
    "senderName": "My Company"
}
send_sms_url = ("https://api.aerframe.aeris.com/smsmessaging/"
                "v2/{}/outbound/{}/requests?apiKey={}").format(ACCOUNT_ID, APP_NAME, ACCOUNT_API_KEY)
req = requests.post(send_sms_url, data=send_sms)