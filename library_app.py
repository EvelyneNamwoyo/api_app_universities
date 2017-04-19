import requests
import json
# import urllib3
def getuniversity(country):
	url = 'http://universities.hipolabs.com/search?country=' + country

	r = requests.get(url)
	country_info = r.json()
while True:
	select_country = str(input('Please enter a country name to obtain university iformation.\nPress enter without any text to exit: ').lower())
	if select_country == '':
		break
	else:
		country_data = getuniversity(select_country)
		# Print the status code of the response.
		#print(response.status_code)

	if country_data[0]['country'].lower() == select_country.lower():
		print ('\nThe country name is ' + country_data[0]['name'] )
		print ('University: ' + str(country_data[0]['name']))
		print ('Domain: ' + str(country_data[0]['domain']))
		print ('Web page: ' + str(country_data[0]['web_page']))
		print ('The Alpha Code is: ' + str(country_data[0]['alpha2Code']))
	else:
		print("whoops no information for that country.")
