# GamersClub scraper to spreadsheets

This utility is designed to scrape data from the GamersClub webpage and save it on a Google Drive spreadsheet. It collects the following data: match id, date, hour, 
map, score, player level, lobby level, kills, assists, deaths, K/D, ADR, KDR, KAST, survived rounds, traded rounds, flash assists, 1vsX, multi kills, first kills, 
points awarded/taken and rating 2.0
 
 
Rating 2.0 is calculated based on [flashed.gg reverse engineering Rating 2.0](https://flashed.gg/posts/reverse-engineering-hltv-rating/)

# Set up

### 1. First, clone this repo

`git clone https://github.com/crisszkutnik/gamersclub-spreadsheets.git`

### 2. Install dependencies
`
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib selenium
`

You also have to install the correct driver for the browser that you are going to use 
 
If you use Ubuntu, geckodriver for Firefox can be installed with the following command:
`sudo apt install firefox-geckodriver`

Otherwise, visit the (Selenium webpage)[https://selenium-python.readthedocs.io/installation.html#drivers] for instructions.

### 3. Set up spreadsheet API

Access to Google spreadsheet API webpage [here](https://developers.google.com/sheets/api/quickstart/python). Go to Step 1 and click **Enable the Google Sheets API**.
Follow the set up steps and then download the file with your credentials. Name it **credentials.json** and paste this file on the cloned folder.

### 4. Create your **config.json** 

This file must be located on the root folder and must contain: spreadsheet_id, player_name and matches array

A guide to finding the spreadsheet ID can be found [here](https://developers.google.com/sheets/api/guides/concepts#spreadsheet_id)

An example can be:

```JSON
{
    "spreadsheet_id": "Your spreadsheet id here",
    "player_name": "cristobalszk",
    "matches": [
        10426756,
        10425538
    ]
}
```

### 5. Run the script
