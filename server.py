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
                print(dateParam)
                searchDatetime = datetime.fromisoformat(dateParam)
                searchDay = searchDatetime.weekday()
                print(searchDay)
                results = restaurants.open_at(searchDay, searchDatetime.time())
                print(results)
                self.send_response(200)
                print("1")
                self.send_header("Content-Type", "application/json")
                print("2")
                self.end_headers()
                print("3", results)
                self.wfile.write(json.dumps(results).encode("utf-8"))
                print("4")
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