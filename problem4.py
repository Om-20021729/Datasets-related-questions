import requests
import pandas as pd 
from io import StringIO
url = " https://api.kite.trade/instruments"

response = requests.get(url)

if response.status_code == 200:
     data = pd.read_csv(StringIO(response.text))

     filtered_data = data[(data["name"] == "FINNIFTY") & (data["expiry"] == "27-03-2024") ]

     if not filtered_data.empty:
        average_strike = filtered_data["strike"].mean()
        print(f"Average Strike Price: {average_strike}")

     else:
        print("No data found for FINNIFTY with expiry 27-03-2024")

else:
    print(f"Failed to fetch data. Status code:{response.status_code}")