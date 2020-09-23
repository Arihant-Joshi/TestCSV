#!/usr/local/opt/python/libexec/bin/python
import sys

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

new_row = sys.argv[2:]

sheet = None
if(sys.argv[1] == "workspace"):
	sheet = client.open("test2").get_worksheet(0)
else:
	sheet = client.open("test2").get_worksheet(1)

sheet.append_row(new_row)