# Zameen.com Scraper

A Python scraper that extracts real estate listings from [Zameen.com](https://www.zameen.com/) using **BeautifulSoup**.

The scraper generates a CSV file with the following columns:

| Column Name    | Description                   |
|----------------|-------------------------------|
| Type           | Type of property (e.g., House, Apartment) |
| City           | City of the property          |
| Address        | Full address                  |
| Area           | Size of property (sq ft / marla) |
| Price          | Listing price                 |
| Bathrooms      | Number of bathrooms           |
| Bedrooms       | Number of bedrooms            |
| Listing Time   | Time when the listing was posted |
| Link           | URL to the property listing   |

## Technologies Used

- Python 3.x  
- BeautifulSoup  
- Requests  
- Pandas  
