# Import the required libraries
import requests
from bs4 import BeautifulSoup

# Make a request to the page URL and get the HTML content
url = "https://forums.redflagdeals.com/hot-deals-f9/"
response = requests.get(url)
html = response.text

# Parse the HTML content using BeautifulSoup and find all the <li> tags with class "row topic"
soup = BeautifulSoup(html, "html.parser")
topics = soup.find_all("li", class_="row topic")

# Loop through each topic and extract the information you want
for topic in topics:
    # Get the value from the "topictitle_retailer" <a> tag
    topictitle_retailer = topic.find("a", class_="topictitle_retailer").text

    # Get the value from the <a> tag right after the above <a>
    title = topic.find("a", class_="topictitle_retailer").find_next_sibling("a").text

    # Get the value from the  "total_count total_count_selector" <dd> tag
    post_voting = topic.find("dd", class_="total_count total_count_selector").text

    # Create an object with these properties
    obj = {
        "topictitle_retailer": topictitle_retailer,
        "title": title,
        "post_voting": post_voting
    }

    # Do something with this object, such as print it or store it in a list or database
    print(obj)
