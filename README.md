# Open Restaurants API #

A simple restaurant API that uses weekday time ranges to return a list of open restaurants for a specific date and time

## Running ##
Placeholder -- for now it's just `python restaurants.py`
TODO: Add Docker instructions

## Usage ##
The service runs on port 8000, so visit hostname:8000/. The service accepts GET requsts and accepts one parameter: `date` which is an ISO-8601 formatted date representing when you would like to check for open restaurants

The service simply returns a list of restaurant names in a JSON array.

TODO: Add swagger file
