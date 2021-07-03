# import data on Star Wars movies from swapi database api
# return a list of Start Wars movies ordered by the length of their opening crawls

import requests                   # opens the requests module to import data through api

resp = requests.get('https://swapi.dev/api/films/') #gets the data from the api provided

import json                       # opens json module to parse the data received from the api

films = resp.json()               # parses the info in resp and stores in films

# films is a dict with the following keys- count, next, previous, results.
# Value of 'results' is a list with values as dict of each movie with the following keys- title, episode_id, opening_crawl, director, producer, release_date, characters etc. 

episodes = films['results']       # creates a list from dict films with only the values stored in key 'results'

crawl_length = [] # creates an empty list to append tuples later

for i in episodes:
    crawl_length.append((i['title'],len(i['opening_crawl'])))   # from the list episodes, a tuple with the title and length of opening crawl is appended for each index (index = dict of each movie)

def sort_tuple(tup):        #define a function to sort tuples by the second element
    tup.sort(key = lambda x : x[1])
    return tup

ordered_crawl_list = sort_tuple(crawl_length)

print(ordered_crawl_list)

