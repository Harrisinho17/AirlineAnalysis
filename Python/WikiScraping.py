from bs4 import BeautifulSoup
import requests
import pandas as pd
import os


url = "https://en.wikipedia.org/wiki/Largest_airlines_in_the_world"  


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}


response = requests.get(url, headers=headers)


if response.status_code == 200:
    
    soup = BeautifulSoup(response.text, "lxml")

    
    tables = soup.find_all("table", {"class": "wikitable"})

    
    output_dir = "/Users/aharris/Documents/GitHub/AirlineSentiment/Data"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    
    for idx, table in enumerate(tables):
        
        df = pd.read_html(str(table))[0]

        
        file_name = f"{output_dir}/table_{idx + 1}.csv"
        df.to_csv(file_name, index=False)
        print(f"Table {idx + 1} saved as {file_name}")

    print("All tables have been saved.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
