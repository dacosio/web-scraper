from requests_html import HTMLSession
import json
import csv

canadian_cities = [
    "Edmonton",
    "Calgary",
    "Red-Deer",
    "Lethbridge",
    "Medicine-Hat",
    "St-Albert",
    "Wood-Buffalo",
    "Grande-Prairie",
    "Vancouver",
    "Surrey",
    "Burnaby",
    "Richmond",
    "Kelowna",
    "Kamloops",
    "Victoria",
    "Nanaimo",
    "Prince-George",
    "Winnipeg",
    "Brandon",
    "Steinbach",
    "Thompson",
    "Portage-la-Prairie",
    "Fredericton",
    "Saint-John",
    "Moncton",
    "St-Johns",
    "Mount-Pearl",
    "Corner-Brook",
    "Yellowknife",
    "Halifax",
    "Iqaluit",
    "Toronto",
    "Ottawa",
    "Mississauga",
    "Brampton",
    "Hamilton",
    "London",
    "Markham",
    "Vaughan",
    "Windsor",
    "Kitchener",
    "Kingston",
    "Charlottetown",
    "Summerside",
    "Montreal",
    "Laval",
    "Gatineau",
    "Longueuil",
    "Saskatoon",
    "Regina",
    "Prince-Albert",
    "Moose-Jaw",
    "Whitehorse"
]

for city in canadian_cities:
    city = city.lower()
    precipitation_url = f'https://www.timeanddate.com/weather/canada/{city}/climate'

    s = HTMLSession()
    r = s.get(precipitation_url)
    r.html.render(sleep=1)
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    data_list = []
    temp_high = r.html.xpath('//*[@class="climategraph__high-label"]')
    temp_low = r.html.xpath('//*[@class="climategraph__low-label"]')
    for month, low, high in zip(months,temp_low, temp_high):
        # temp is in Celsius
        ht = high.text
        lt = low.text
        mean = (int(ht)+int(lt))/2
        data ={
                "month":month,
                "high_temp" : ht,
                "low_temp":lt,
                "mean": mean,
                "city": city
            }
        data_list.append(data)


    to_csv = data_list
    keys = to_csv[0].keys()

    with open(f'temperature_csv/temp_{city}.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(to_csv)