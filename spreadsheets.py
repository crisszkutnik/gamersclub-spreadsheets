from scraper import extract_data
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os.path
import pickle
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# For testing
options = Options()
options.headless = True

m_id = 10446808 
f_driver = webdriver.Firefox(options=options)

def sort_keys(obj):
	order = [
		"id",
		"date",
		"hour",
		"map",
		"team_score",
		"enemy_score",
		"victory",
		"player_level",
		"team_level",
		"enemy_level",
		"kills",
		"assists",
		"deaths",
		"diff",
		"adr",
		"kdr",
		"kast",
		"s",
		"t",
		"fa",
		"1vsX",
		"mk",
		"fk",
		"points",
		"rating"
	]

	return [obj[key] for key in order]

def update_table(obj):

	SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

	# Code snippet extracted from Sheets docs

	creds = None

	if os.path.exists("token.pickle"):
		with open("token.pickle", "rb") as token:
			creds = pickle.load(token)

	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file(
				"credentials.json", SCOPES)
			creds = flow.run_local_server(port=0)

			with open("token.pickle", "wb") as token:
				pickle.dump(creds, token)

	service = build('sheets', 'v4', credentials=creds)

	# End code snippet

	body = {
		"range": "A2:Y2",
		"values": [sort_keys(obj)]
	}

	with open("data.json", "r") as f:
		json_file = json.load(f)
		spreadsheetId=json_file["spreadsheet_id"]

	# Ignore error
	sheet = service.spreadsheets()
	result = sheet.values().append(
		spreadsheetId=spreadsheetId,
		range="A2:Y2",
		body=body,
		valueInputOption="RAW"
	).execute()

	print("{} cells appended".format(result))

data = extract_data(f_driver, m_id)
update_table(data)