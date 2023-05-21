# Build an application that extracts phone number, email and link from a website
import re
import requests
import csv


mytext = input("Which web page do you want to scrape? :")
# use requests module to access the site
response = requests.get(mytext)
#output it in the form of a text
my_text_url = response.text


To_scrape = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b|\b(?:https?://|www\.)\S+\b|\b(?:\+\d{1,3}\s)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"

matches = re.findall(To_scrape, my_text_url)

with open('matches.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Matches'])
    writer.writerows([[match] for match in matches])

print("Completed,your file can be found at'matches.csv'.")