#!/usr/bin/env python3

import sys
import requests
import json

'''
This script downloads itunes libraries for an artist that the user inputs at the command line, 
using the itunes API (Application Programming Interface)

'''

# Enter the https address below into your browser to download and view the JSON file from itunes
# The first line uses the requests method to fetch the JSON file and asign it to the response variable
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=4&term=ninasimone")

# uncomment this line to see the JSON file indented 2-columns, in a more readable format
# print(json.dumps(response.json() ,indent=2))

# This section prints out track names for the artist hard-coded in the https address above using a for loop
# you can changne the artist name and song track limit, or remove the limit to print out all of the tracks ("limit=4&")
# The "results" and "trackName" keys are taken directly from the downloaded itunes file
# object = response.json()
# for result in object["results"]: #key of object returned in JSON
#    print(result["trackName"]) # returned in JASON object too


# This section takes in a band name from the command linne and prints out a list of songs they have released, as we did in class
band_name = sys.argv[1]

# This is the same as the code above but the bannd name variable used is provided at the command line by the used
# the song limit has also beenn removed
response = requests.get("https://itunes.apple.com/search?term=" + band_name+ "&entity=song") # removed limit - use sys.argv

# uncomment this to see the raw JSON-formatted download
#print(response.json())

# First, we put the response variable downloaded from the itunes site into a variable
# We then use a for loop to loop through the results,
# The "results" and "trackName" keys are taken directly from the downloaded itunes file
object = response.json()
for result in object["results"]: #key of object returned in JSON
    print(result["trackName"]) # returned in JASON object too



