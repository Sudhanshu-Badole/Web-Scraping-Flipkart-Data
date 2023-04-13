# Web-Scraping-Flipkart-Data
Readme file for Flipkart Mobiles Scrapper
This Python code is a web scraper that extracts data from Flipkart's search results for mobile phones that cost less than 5000.

Dependencies
This code requires the following Python libraries to run:

requests
pandas
BeautifulSoup
Usage
The product_name, price, and Description lists are initialized to hold the extracted data, which is appended from multiple pages of Flipkart's search results. The range in the for loop iterates through each page of results.

Then, the script makes a request to the search results page using the requests module, and passes the HTML content to BeautifulSoup for parsing. The box variable uses BeautifulSoup's find method to locate the main container div for the search results.

The script then finds all of the product names, prices, and descriptions on the page using BeautifulSoup's find_all method, and appends them to their respective lists.

Finally, the data is saved in a Pandas DataFrame with the columns "Product Name", "Price", and "Description". The DataFrame is then saved as a CSV file named "flipkart_mobiles_under_50000.csv" using Pandas' to_csv method.

To use this code, simply run the script in your Python environment or IDE. You can adjust the search criteria by modifying the URL in the url variable.

Disclaimer
This script is intended for educational purposes only. Scraping websites may be against their terms of service or even illegal in some cases. Use this code at your own risk.
