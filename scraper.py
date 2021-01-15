from selenium import webdriver
import json

# For testing
m_id = 10426269
f_driver = webdriver.Firefox()

def get_players(container):
	return [e.get_attribute("innerHTML") for e in container.find_elements_by_css_selector("a.tableMatch__playerLink")]

def get_score(table):
	return int(table.find_element_by_css_selector("span.TableMatchTeamScore").get_attribute("innerHTML"))

def get_attribute(element, selector, attr):
	return element.find_element_by_css_selector(selector).get_attribute(attr)

def get_innerHTML(element, selector):
	return get_attribute(element, selector, "innerHTML")

def get_innerText(element, selector):
	return get_attribute(element, selector, "innerText")

def extra_data(driver):
	data_cell = get_innerText(driver, "#match-info-lobby > div > div.stats.columns > div:nth-child(1) > div:nth-child(1)")
	hour = data_cell[-5:]
	date = data_cell[-16:-6]
	played_map = get_innerText(driver, "#match-info-lobby > div > div.stats.columns > div:nth-child(1) > div:nth-child(4)")[5:] # remove MAP\n

	return hour, date, played_map

def extract_data(driver, match_id):
	# First we have to select the correct table
	match_data = {
		"id": match_id
	}
	driver.get("https://gamersclub.com.br/lobby/partida/{}".format(match_id))
	tables = driver.find_elements_by_css_selector("div.tableMatch")
	players0 = get_players(tables[0])
	players1 = get_players(tables[1])

	if "cristobalszk" in players0:
		player_table, enemy_table = tables
		p_index = players0.index("cristobalszk")
	else:
		enemy_table, player_table = tables
		p_index = players1.index("cristobalszk")

	# Table selected. Extract relevant data

	# Match relevant data

	match_data["team_score"] = get_score(player_table)
	match_data["enemy_score"] = get_score(enemy_table)
	match_data["victory"] = True if match_data["team_score"] > match_data["enemy_score"] else False
	match_data["hour"], match_data["date"], match_data["map"] = extra_data(driver)
	
	# Player relevant data

	player_cell = player_table.find_elements_by_css_selector("tr.tableMatch__user")[p_index]
	player_data = player_cell.find_elements_by_css_selector("td")
	
	items = ["kills", "assists", "deaths", "adr", "kdr", "kast", "s", "t", "fa", "1vsX", "mk", "fk"]
	del player_data[0] # remove name cell
	del player_data[3] # remove diff cell
	del player_data[-1] # delete action cell
	match_data["points"] = int(player_data[-1].get_attribute("innerHTML").strip("\n")) # last cell will be points cell

	for i in range(0, len(items)):
		match_data[items[i]] = player_data[i].get_attribute("innerHTML")

	print(json.dumps(match_data, indent=4))

extract_data(f_driver, m_id)