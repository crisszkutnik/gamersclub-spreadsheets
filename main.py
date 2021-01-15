from scraper import extract_data
from spreadsheets import update_table
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def main():
    options = Options()
    options.headless = True

    matches = [
        10426756,
        10425538
    ]
    f_driver = webdriver.Firefox(options=options)

    matches_data = [extract_data(f_driver, match_id) for match_id in matches]

    update_table(matches_data)

main()