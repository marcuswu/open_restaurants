import json
import csv
from datetime import datetime
from urllib.parse import urlparse, parse_qs
from http.server import SimpleHTTPRequestHandler, HTTPServer
from restaurants import Restaurants

def restaurant_handler(restaurants):
    class RestaurantRequestHandler(SimpleHTTPRequestHandler):
        def do_GET(self):
            # try:
                params = parse_qs(urlparse(self.path).query)
                dateParam = params.get('date')[0]
                print("Received request for date ", dateParam)
                searchDatetime = datetime.fromisoformat(dateParam)
                searchDay = searchDatetime.weekday()
                print("Looking up day of week ", searchDay)
                results = restaurants.open_at(searchDay, searchDatetime.time())
                print("Restaurants open for date ", dateParam, ": ", results)
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(results).encode("utf-8"))
            # except ValueError as e:
            #     # bad request -- invalid date
            #     print("Invalid date", e)
            #     self.send_response(400, "Invalid 'date' parameter. The 'date' field must be a valid ISO-8601 datetime value")
            # except Exception as e:
            #     # return bad request
            #     print("Unknown exception", e)
            #     self.send_response(400, e)
    return RestaurantRequestHandler
        

csv_file = open('restaurants.csv')
csv_reader = csv.reader(csv_file)
restaurants = Restaurants(csv_reader)
server = HTTPServer(('localhost', 8000), restaurant_handler(restaurants=restaurants))
server.serve_forever()