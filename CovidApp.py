import tkinter as tk
import requests
import json

HEIGHT = 500
WIDTH = 600

def test_function(entry):
	print("This is the entry:", entry)



def format_response(users):
	try:

		for user in users:


			confirmed = user['provinces'][0]['confirmed']
			recovered =  user['provinces'][0]['recovered']
			deaths = user['provinces'][0]['deaths']
			active = user['provinces'][0]['active']
		#print('Confirmed cases:', confirmed)
		#print('Recovered:', recovered)
		#print('Deaths:', deaths)
		#print('Active:', active)
			final_str = 'Confirmed: %s \nRecovered: %s \nDeaths: %s \nActive: %s' %(confirmed, recovered, deaths, active)

	except:
		final_str = 'There was a problem retrieving that information'

	return final_str


def get_report(city):
	url = "https://covid-19-data.p.rapidapi.com/report/country/name"

	querystring = {"date-format":"YYYY-MM-DD","date":"2020-06-01","name":city}

	headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "bb658d2dbcmsh8559bdc1d32e1e8p121224jsndc79c0a35b41"
    }


	response = requests.get(url, headers=headers, params=querystring)
	
	users = json.loads(response.text)

	label['text'] = format_response(users)









root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image=tk.PhotoImage(file='cov.png')
background_label=tk.Label(root,image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#1979a9', bd=5)
frame.place(relx=0.5, rely=0.1,relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Report", font=30, command=lambda: get_report(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#1979a9', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 10))
label.place(relwidth=1, relheight=1)



root.mainloop()