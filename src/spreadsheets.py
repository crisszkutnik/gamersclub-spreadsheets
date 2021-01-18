import os.path
import pickle
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

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

	for index in ["kdr", "adr"]:
		obj[index] = obj[index].replace(".", ",")
	# replace '.' with ',' because spreadsheets would not recognize numbers correctly otherwise

	ret = [obj[key] for key in order]

def login():
	SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

	# Code snippet extracted from Sheets docs

	creds = None

	if os.path.exists("../token.pickle"):
		with open("../token.pickle", "rb") as token:
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

	return build('sheets', 'v4', credentials=creds)


def update_table(objs, spreadsheet_id):
	service = login()

	body = {
		"range": "A2:Y2",
		"values": [sort_keys(obj) for obj in objs]
	}

	# Ignore error
	sheet = service.spreadsheets()
	result = sheet.values().append(
		spreadsheetId=spreadsheet_id,
		range="A2:Y2",
		body=body,
		valueInputOption="RAW"
	).execute()

	print("Spreadsheet updated")