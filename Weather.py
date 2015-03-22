#Import all the libraries we need
import unirest
import json
import os
#Assign X to 1 for our loop (We can use a While True Loop too)
x = 1
#Prints Welcome Screen
os.system('cls')
print('================================')
print('Welcome to the Weather App!')
print('Press Enter to Continue!')
print('================================')
raw_input('')
#While Loops begins, You can use While True loop too
while x == 1:
	#UserValue equals What the user inputs, the city or state
	UserValue = raw_input('Please enter a City or State: ')
	#Replace Space with a plus sign(So we can pass it onto the url)
	UserValue = UserValue.replace(' ','+' )
	#Make web request to the url(with url value attached) with the Mashape KEY and the content type
	response = unirest.get("https://george-vustrey-weather.p.mashape.com/api.php?location=" + UserValue,
  	headers={
  	  "X-Mashape-Key": "",
   	 "Accept": "application/json"
  	}
		)
	#Assigned the JSON Data we recieved with the varible data
	data = json.loads(response.raw_body)
	#Try to extract data and apply to varibles  
	try:
		DOW1 = data[0]["day_of_week"]
		DOW2 = data[1]["day_of_week"]
		DOW3 = data[2]["day_of_week"]
		DOW4 = data[3]["day_of_week"]
		DOW5 = data[4]["day_of_week"]
		DOW6 = data[5]["day_of_week"]
		DOW7 = data[6]["day_of_week"]

		H1 = data[0]["high"]
		H2 = data[1]["high"]
		H3 = data[2]["high"]
		H4 = data[3]["high"]
		H5 = data[4]["high"]
		H6 = data[5]["high"]
		H7 = data[6]["high"]

		L1 = data[0]["low"]
		L2 = data[1]["low"]
		L3 = data[2]["low"]
		L4 = data[3]["low"]
		L5 = data[4]["low"]
		L6 = data[5]["low"]
		L7 = data[6]["low"]

		C1 = data[0]["condition"]
		C2 = data[1]["condition"]
		C3 = data[2]["condition"]
		C4 = data[3]["condition"]
		C5 = data[4]["condition"]
		C6 = data[5]["condition"]
		C7 = data[6]["condition"]
		print('\n')
		print('================================')
		print(DOW1)
		print('Condition: ' + C1)
		print('High: ' + H1)
		print('Low: ' + L1)
		print('================================')
		print('\n')
		print('================================')
		print(DOW2)
		print('Condition: ' + C2)
		print('High: ' + H2)
		print('Low: ' + L2)
		print('================================')
		print('\n')
		print('================================')
		print(DOW3)
		print('Condition: ' + C3)
		print('High: ' + H3)
		print('Low: ' + L3)
		print('================================')
		print('\n')
		print('================================')
		print(DOW4)
		print('Condition: ' + C4)
		print('High: ' + H4)
		print('Low: ' + L4)
		print('================================')
		print('\n')
		print('================================')
		print(DOW5)
		print('Condition: ' + C5)
		print('High: ' + H5)
		print('Low: ' + L5)
		print('================================')
		print('\n')
		print('================================')
		print(DOW6)
		print('Condition: ' + C6)
		print('High: ' + H6)
		print('Low: ' + L6)
		print('================================')
		print('\n')
		print('================================')
		print(DOW7)
		print('Condition: ' + C7)
		print('High: ' + H7)
		print('Low: ' + L7)
		print('================================')
		print('\n')
		raw_input('')

		pass
	#If the data does not exist, it may be due to the user inputting something thats not a city or state
	except KeyError, e:
		#Clear Screen and show error message we get from API
		os.system('cls')
		print('Error ' + str(data[0]['code']) + ':' + ' ' + data[0]['message'])
		raw_input('')

		
	#Clear Screen and ask user if they want to quit or perform a search again
	os.system('cls')
	print('Would you like to search again? or Quit?')
	print('1: Search again')
	print('2: Quit')
	ans = input('')
	#If the quit, then x = 2 which breaks out of the loop, if Search again then do nothing and the Loop will restart
	if ans == 2:
		x = 2
