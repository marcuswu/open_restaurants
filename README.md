# Open Restaurants API #

A simple restaurant API that uses weekday time ranges to return a list of open restaurants for a specific date and time

## Testing ##
The only dependencies in this project are for testing coverage. I could not find a code coverage solution that was in the standard library. For this reason, pip install is only required when running test coverage. Running tests by themselves does not require installing test coverage.

### Running tests ###
`python tests.py`

### Setup for test coverage ###
`pip install -r requirements.txt`

### Running test coverage ###
`coverage run tests.py`

### Printing coverage report ###
`coverage report`

## Running ##

### Locally ###
`python restaurants.py`

### In Docker ###

#### Build Docker Container ####
`docker build -t open_restaurants .`

#### Run Docker Container ####
To auto publish the exposed port:
`docker run -P open_restaurants`

Or to choose the host port:
`docker run -p localhost:8000:8000 open_restaurants`

## Usage ##
The service runs on port 8000, so visit hostname:8000/. If running under Docker, use the chosen publish port.

The service accepts GET requsts and accepts one parameter: `date` which is an ISO-8601 formatted date representing when you would like to check for open restaurants

The service simply returns a list of restaurant names in a JSON array.

See also: [swagger file ](docs/open_restaurants.yaml)
