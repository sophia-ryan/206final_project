from bs4 import BeautifulSoup
import sqlite3
import csv
import json
import requests

url = 'http://www.dinersdriveinsdiveslocations.com/'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

# a program that allows users to select a state and see all the different
# diners, drive - ins and dives in that state
# info is displayed as HTML on Flask

class Restaurant:
    def __init__(self, name, address, city, state, phone, price, reserve_url=None):
        self.name = rest_name
        self.address = rest_address
        self.city = rest_city
        self.state = rest_city
        self.phone = rest_phone
        self.price = rest_price
        self.reserve_url = reserve_url

    def __str__(self): # need to add extra params
        pass

## CACHING FOR GET_DDD_FOR_STATE

# on startup, try to load the cache from file
# just want to cache the html
CACHE_FNAME = 'cache.json'

try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()

# if there was no file, no worries. There will be soon!
except:
    CACHE_DICTION = {}

# The main cache function: it will always return the result for this
# url+params combo. However, it will first look to see if we have already
# cached the result and, if so, return the result from cache.
# If we haven't cached the result, it will get a new one (and cache it)

def make_request_using_cache(url):
    base_url = 'http://www.dinersdriveinsdiveslocations.com/'
    unique_ident = url

    ## first, look in the cache to see if we already have this data
    if unique_ident in CACHE_DICTION:
        print("Getting cached data...")
        print()
        return CACHE_DICTION[unique_ident]

    ## if not, fetch the data afresh, add it to the cache,
    ## then write the cache to file
    else:
        print("Making a request for new data...")
        print()
        # Make the request and cache the new data
        resp = requests.get(url).text
        CACHE_DICTION[unique_ident] = resp

        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME,"w")
        fw.write(dumped_json_cache)
        fw.close() # Close the open file
        return CACHE_DICTION[unique_ident]


## END: CACHING FOR GET_DDD_FOR_STATE!
restaurant_list = []

def get_ddd_for_state(state_name):
    url = 'http://www.dinersdriveinsdiveslocations.com/'
    state_list = soup.find_all('a')
    state_url_list = []
    state_name_url = 'http://www.dinersdriveinsdiveslocations.com/{}-locations.html'.format(state_name.lower())

    for state_lisk in state_list:
        if 'http://www.dinersdriveinsdiveslocations.com/' in state_lisk['href'] and 'road-trip' not in state_lisk['href']:
            state_url_list.append(state_lisk['href'])

    for x in state_url_list:
        if x == state_name_url:
            make_request_using_cache(x)

    res = requests.get(state_name_url)
    # turn back into soup
    state_soup = BeautifulSoup(res.text, 'html.parser')
    name_list = state_soup.find_all("table", align = "center", cellpadding= "3", width = "90%")

    for table in name_list:

        for data in table.find_all('td'):
            # data from first, overall state page
            phone = data.i.text.strip()
            name = data.a.text.strip()
            full_string = data.text.replace('\n', '').strip()
            address = full_string[len(name): full_string.index(phone)].strip()
            phone = phone[7:]

            # data from specific pages
            spec_url = data.a['href']
            restaurant_specifics = requests.get("http://www.dinersdriveinsdiveslocations.com/" + spec_url)
            spec_soup = BeautifulSoup(restaurant_specifics.text, 'html.parser')
            episode = spec_soup.find('strong').text
            first_header = spec_soup.find('h1', class_= 'dinerIntro')
            season = first_header.find_next('font').text[-1]

            restaurant_list.append((name, address, phone, season, episode))

    return(restaurant_list)

# now we have a list of list of tuples so we have everything for one state and then
# the restaurants are going to be in there

# Read data from CSV & JSON into Database

DBNAME = 'restaurant.db'

def init_db():
    try:
        conn = sqlite3.connect(DBNAME)
        cur = conn.cursor()
    except Error as e:
        print(e)

    statement = '''
                DROP TABLE IF EXISTS 'Restaurants'
                '''

    cur.execute(statement)

    statement = '''
                DROP TABLE IF EXISTS 'Episode'
                '''

    cur.execute(statement)

    statement = '''
                CREATE TABLE `Restaurants` (
            	`Id`	INTEGER PRIMARY KEY AUTOINCREMENT,
            	`Name`	TEXT,
            	`Address`	TEXT,
            	`EpisodeId`	INTEGER,
            	`PhoneNumber`	INTEGER
            );
                '''

    cur.execute(statement)
    conn.commit()

    statement = '''
                CREATE TABLE `Episode` (
            	`Id`	INTEGER PRIMARY KEY AUTOINCREMENT,
            	`EpisodeName`	TEXT,
                `SeasonNumber`  INTEGER
            );
                '''

    cur.execute(statement)
    conn.commit()
    conn.close()

def insert_episode(restaurant_list):
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()

    for restaurant in restaurant_list:
        statement = 'INSERT INTO Episode Values (?,?,?)'
        insert = (None, restaurant[3], restaurant[4])
        cur.execute(statement, insert)

        conn.commit()
    conn.close()

def match_data(restaurant_list):
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()

    q = cur.execute("SELECT * FROM Episode").fetchall()

    global episode_id

    for restaurant in restaurant_list:
        for iterate in q:
            if restaurant[3] in iterate:
                episode_id = iterate[0]
        conn.commit()
    conn.close()

def insert_restaurants(restaurant_list):
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()
    for restaurant in restaurant_list:
        statement = 'INSERT INTO Restaurants Values (?,?,?,?,?)'
        insert = (None, restaurant[0], restaurant[1], episode_id, restaurant[2])
        cur.execute(statement, insert)

        conn.commit()
    conn.close()

alabama_list = get_ddd_for_state('alabama')
init_db()
insert_episode(alabama_list)
match_data(alabama_list)
insert_restaurants(alabama_list)
