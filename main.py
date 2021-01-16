from scraper import extract_data
from spreadsheets import update_table
from driver import start_driver
import json

def main():
    with open("config.json", "r") as f:
        json_data = json.load(f)

    if len(json_data["matches"]) == 0: # There is no match to scrape
        print("No matches to scrape")
        return
    
    matches = json_data["matches"]

    browser_driver = start_driver()   

    matches_data = [extract_data(browser_driver, match_id, json_data["player_name"]) for match_id in matches]

    update_table(matches_data, json_data["spreadsheet_id"])

main()