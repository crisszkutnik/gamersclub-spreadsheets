from scraper import extract_data
from spreadsheets import update_table
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

def main():
    with open("config.json", "r") as f:
        json_data = json.load(f)

    

    options = Options()
    options.headless = True

    browser = json_data["browser"].lower()

    matches = json_data["matches"]
    #f_driver = webdriver.Firefox(options=options)

    if browser == "firefox":
        browser_driver = webdriver.Firefox(options=options)
    elif browser == "chrome":
        browser_driver = webdriver.Chrome(options=options)
    elif browser == "opera":
        browser_driver = webdriver.Opera(options=options)
    elif browser == "ie": # Most likely will not work but idk
        browser_driver = webdriver.Ie(options=options)
    else:
        raise Exception("'browser' property in config.json has to be Firefox, Chrome, Opera or IE")

    if len(json_data["matches"]) == 0: # There is no match to scrape
            print("No matches to scrape")
            return

    matches_data = [extract_data(browser_driver, match_id, json_data["player_name"]) for match_id in matches]

    update_table(matches_data, json_data["spreadsheet_id"])

main()