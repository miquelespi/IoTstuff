#!/usr/bin/python

import sys
import time
import datetime

import Adafruit_DHT
import gspread

DHT_TYPE = Adafruit_DHT.AM2302
DHT_PIN  = 22
GDOCS_SPREADSHEET_NAME = 'sensinghome'
GDOCS_JSON_FILE        = '/home/pi/src/IoTstuff/raspi_temperature_humidity/longnapiotfun-ef06d99c0061.json'


def login_open_sheet(json_file, spreadsheet):
    """Connect to Google Docs spreadsheet and return the first worksheet."""
    import json
    from oauth2client.client import SignedJwtAssertionCredentials

    try:
        json_key = json.load(open(json_file))
        scope = ['https://spreadsheets.google.com/feeds']

        credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
        gc = gspread.authorize(credentials)
        
        worksheet = gc.open(spreadsheet).sheet1
        return worksheet
    except:
        print 'Unable to login and get spreadsheet.'
        sys.exit(1)

worksheet = login_open_sheet(GDOCS_JSON_FILE, GDOCS_SPREADSHEET_NAME)

humidity, temp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)

if humidity is None or temp is None:
    donothing = 1
else:
    try:
        worksheet.append_row((datetime.datetime.now(), temp, humidity))
    except:
        donothing = 1
