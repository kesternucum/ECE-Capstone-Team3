# Import Libraries
import json
import requests
import time

url_post = "https://localhost:7202/api/LiveFeed/{}/{}/{}"

# Ensure that sum has changed before writing to database
temp = 0

# Sum together values from different JSON files
while True:
	# Open JSON files and read data from it
	sjFile = open('static_data.json')
	static_data = json.load(sjFile)
	djFile = open('dynamic_data.json')
	dynamic_data = json.load(djFile)
	
	time.sleep(5)
	
	# Calculate sum and determine if there has been a change
	sum = static_data['car_count'] + dynamic_data['car_count'];
	if sum != temp:
		print(temp)
		print(sum)
		temp = sum
		post_response = requests.post(url_post.format("92opt", sum, False), verify=False)
		print(post_response)
	
	# Close file once work completed
	sjFile.close()
	djFile.close()
