# Open Restaurants API #

A simple restaurant API that uses weekday time ranges to return a list of open restaurants for a specific date and time

## Testing ##
The only dependencies in this project are for testing coverage. I could not find a code coverage solution that was in the standard library. For this reason, pip install is only required when testing.
`pip install -r requirements.txt`

`python tests.py`

## Running ##

### Locally ###
`python restaurants.py`

### In Docker ###
TODO: Add Docker instructions

## Usage ##
The service runs on port 8000, so visit hostname:8000/. The service accepts GET requsts and accepts one parameter: `date` which is an ISO-8601 formatted date representing when you would like to check for open restaurants

The service simply returns a list of restaurant names in a JSON array.

TODO: Add swagger file
