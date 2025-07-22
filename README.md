rest-api-python-demo 

This demo shows how to call the New York Times API using the 
python requests library and parse its JSON data.

It also shows how you can store and hide your API keys with 
a .env file and .gitignore file, respectively.

Part 1 — Get article headlines for topic 
Check out NYT API 
Create app using NYT Dev console: https://developer.nytimes.com/my-apps 
Get API key for sending requests pip install requests 
Write initial article search request code 
Read JSON from response 
Print JSON into a nicer format 
Get article headlines from JSON 
Part 2 — Hide API Key 
import os 
pip install python-dotenv 
Create .env file and add key to NYT_KEY variable 
Get NYT_KEY from environment variable using dotenv 
Create .gitignore and add .env to it


had to do

create a venv
  ctrl+shift+p
  search for Python: Create Environment

./.venv/bin/activate (seems to happen automatically in vscode now?)

pip3 install requests
pip3 install load-dotenv
pip3 install python-dotenv

python3 ./fetch_n_print_movies_weekly.py