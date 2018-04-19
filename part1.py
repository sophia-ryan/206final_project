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
            # print(phone)
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

    # NEED TO FIX THE FACT THAT NOT CATCHING THE SAME EPISODES
    for restaurant in restaurant_list:
        # name = restaurant[4]
        # q = cur.execute("SELECT COUNT(*) FROM Episode WHERE EpisodeName LIKE '%{}' ".format(name)
        result = cur.fetchone()
        if result is None:
            pass
        else:
            statement = 'INSERT INTO Episode Values (?,?,?)'
            insert = (None,restaurant[4] ,restaurant[3])
            cur.execute(statement, insert)

        conn.commit()
    conn.close()

def match_data():
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()

    q = cur.execute("SELECT * FROM Episode").fetchall()

    episode_map = {}

    for ep in cur:
        # it's coming in here but not setting
        episode_map[ep[1]] = ep[0]

    return episode_map

def insert_restaurants(restaurant_list):
    episode_map = match_data()
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()
    for restaurant in restaurant_list:
        statement = 'INSERT INTO Restaurants Values (?,?,?,?,?)'
        # insert = (None, restaurant[0], restaurant[1], episode_map[restaurant[3]], restaurant[2])
        insert = (None, restaurant[0], restaurant[1], "0", restaurant[2])
        cur.execute(statement, insert)

        conn.commit()
    conn.close()

# NEVER DO FOR DATA THATS ALREADY WORKED!! It duplicates the restaurants in db
state_list = get_ddd_for_state('mexico')
# init_db()
insert_episode(state_list)
match_data()
insert_restaurants(state_list)

# states that didn't work - it's occuring in the same place

# uk
# bc
# mexico
# west virginia
# utah
# tennessee
# south carolina
# rhode island
# oklahoma
# north carolina
# new york
# new mexico
# new jersey
# new hampshire
# nevada
# missouri
# Mississipi
# minnesota
# massachusetts
# maryland
# california
# connecticut
# dc
# hawaii
# illinois
# indiana
# kansas
# maine
