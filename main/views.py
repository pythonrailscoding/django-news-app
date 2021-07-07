from django.shortcuts import render
import urllib.request
import json
from datetime import date, datetime
from django.http import JsonResponse

api_key = ""
weather_api = ""

def index(request):
	# Get ip address of the user
	ip = urllib.request.urlopen("https://api.ipify.org?format=json").read()
	json_res = json.loads(ip)
	ip_address = json_res["ip"]

	# Get country code of the current user
	country_ip = urllib.request.urlopen("http://ip-api.com/json/"+ip_address).read()
	country_json = json.loads(country_ip)
	country_code = country_json["countryCode"]
	country = country_json["country"]

	# Get Weather Details of the user's region
	user_region = country_json["city"]
	weather_json = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q="+user_region+"&appid="+weather_api).read()
	weather_list = json.loads(weather_json)
	weather_list = {
		"temp": format(weather_list['main']['temp'] - 273, ".2f"),
		"description": str(weather_list["weather"][0]["description"]).capitalize()
	}

	# Get current Year
	current_date = date.today()
	current_year = current_date.year

	# Get news for a country code
	res = urllib.request.urlopen("https://newsapi.org/v2/top-headlines?country="+country_code+"&apiKey="+api_key).read()
	json_data = json.loads(res)
	t_length = len(json_data["articles"])

	# Create some python lists
	author = []
	title = []
	description = []
	url = []
	image = []


	for i in range(t_length):
		author.append(json_data["articles"][i]["author"])
		title.append(json_data["articles"][i]["title"])
		description.append(json_data["articles"][i]["description"])
		url.append(json_data["articles"][i]["url"])
		image.append(json_data["articles"][i]["urlToImage"])
	zipped_data = zip(author, title, description, url, image)

	return render(request, "index.html", {"zipped": zipped_data, "country": country, "year": current_year, "region": user_region, "weather_list": weather_list})

def getDate(request):
	current_time = datetime.now()

	# Get Current Time Credentials
	current_hour = current_time.hour
	current_minute = current_time.minute
	current_second = current_time.second

	# Convert current hour and minute to list
	current_time_data = [
		current_hour, current_minute, current_second
	]

	return JsonResponse({"time": list(current_time_data)})
