from scraper import extract_data
from spreadsheets import update_table
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

def main():
    options = Options()
    options.headless = True

    with open("config.json", "r") as f:
        json_data = json.load(f)

    matches = json_data["matches"]
    f_driver = webdriver.Firefox(options=options)

    matches_data = [extract_data(f_driver, match_id, json_data["player_name"]) for match_id in matches]

    update_table(matches_data, json_data["spreadsheet_id"])

main()