from bs4 import BeautifulSoup
import requests 
import pandas as pd
import time
import random

def safe_extract(tag,attribute):
    try:
        element = new_source_code.find(tag,attrs=attribute).text
        return element
    except Exception as e:
        return "N/A"
    
cities_dict ={
    "Lahore": "-1-",
    "Karachi": "-2-",
    "Islamabad": "-3-"
}

property_types_dict={
    "House": "Houses_Property/",
    "Flats": "Flats_Apartments/",
    "Rooms": "Rooms/"
}

purpose_dict={
    "Buy": "",
    "Rent": "Rentals_",
}
city = input("Enter city: Karachi/Lahore/Islamabad\t")
purpose = input("Enter purpose: Buy/Rent\t")
property_type = input("Enter property type: House/Flats/Rooms\t")

## scrapping 
details= []

for x in range(1,5):
    url = "https://www.zameen.com/"+ purpose_dict[purpose] + property_types_dict[property_type] + city + cities_dict[city] + str(x) +".html"
    print(url)

    Headers = ({"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.70 Safari/537.36","Accept-Language":"en-US,en;q=0.9"})
    response = requests.get(url,headers=Headers)

    source_code = BeautifulSoup(response.content,"lxml")


    for property in source_code.find_all("a",attrs={"class":"d870ae17"}):
        extract_link = property.get("href")
        base_url = "https://www.zameen.com/"
        property_url = base_url + extract_link
        # print(property_url)
        response = requests.get(property_url,headers=Headers)
        # print(response.status_code)


        new_source_code = BeautifulSoup(response.content,"lxml")

        address = new_source_code.find("div",attrs={"class":"cd230541"}).text
        type = safe_extract("span",{"aria-label":"Type"})
        price = safe_extract("span",{"aria-label":"Price"})
        baths = safe_extract("span",{"aria-label":"Baths"})
        beds = safe_extract("span",{"aria-label":"Beds"})
        area = safe_extract("span",{"aria-label":"Area"})
        listed_time = safe_extract("span",{"aria-label":"Creation date"})

        property_info ={
            "Type": type,
            "City": city,
            "Address": address,
            "Area": area,
            "Price": price,
            "Bathrooms": baths,
            "Bedrooms": beds,
            "Listig Time": listed_time,
            "link":property_url
        }

        details.append(property_info)   
           
    print(len(details))
    time.sleep(random.uniform(2, 4))


df = pd.DataFrame(details)
print(df.head())
df.to_csv("PropertyData.csv",index=True)




