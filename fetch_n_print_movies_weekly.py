"""python assignment for weekly movie info"""
import json
import os
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # This is to load your API keys from .env

TMDB_TRENDING_PATH = 'trending/movie/week'
TMDB_SEARCH_API_REQUEST = f'https://api.themoviedb.org/3/{TMDB_TRENDING_PATH}?'

#def get_top_10_weekly_trending_movies():
response = requests.get(
    TMDB_SEARCH_API_REQUEST,
    params={
        'api_key': os.getenv('TMDB_API_KEY')
    }
)
# Encodes response into a python json dictionary.
json_data = response.json()

# Convert json_data to a formatted pretty
# json string that is easy for humans to read.
# Mouse over function to get definition of indent and sort_keys
pretty_json_data = json.dumps(json_data, indent=4, sort_keys=True)
#print(pretty_json_data)
weekly_trending_movie_object = json_data
# Add Parsing Code Here
# build a 2d array, load it, sort alphabetically and print
results_length = len(weekly_trending_movie_object['results'])
rows, cols = (results_length, 3)
wtmo = [[0]*cols]*rows
for k in range(results_length):
    wtmo[k] = [weekly_trending_movie_object['results'][k]['title'], \
               weekly_trending_movie_object['results'][k]['popularity'], \
               weekly_trending_movie_object['results'][k]['vote_count']]
#sorts by alphabetical names
sorted_wtmo = sorted(wtmo)
print("\n{:<50} {:<15} {:<15} \n".format('Movie Title', 'Popularity', 'Vote Count'))
for j in range(results_length):
    print("{:<50} {:<15} {:<15} ".format(sorted_wtmo[j][0], sorted_wtmo[j][1], sorted_wtmo[j][2]))
# reload the 2d array, sort again for vote average, print again
for k in range(results_length):
    wtmo[k] = [weekly_trending_movie_object['results'][k]['vote_average'], \
               weekly_trending_movie_object['results'][k]['title'], \
               weekly_trending_movie_object['results'][k]['vote_count']]
sorted_wtmo = sorted(wtmo)
print("\n\n{:<15} {:<45} \n".format('Vote Average', 'Movie Title'))
for j in range(results_length):
    print("{:<15} {:<45} ".format(sorted_wtmo[j][0], sorted_wtmo[j][1]))
print("\n")
