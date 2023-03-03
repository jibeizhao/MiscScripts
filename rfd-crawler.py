import requests
from bs4 import BeautifulSoup

# connect to mysql database
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
)
mycursor = mydb.cursor()

# create a table if not exists
mycursor.execute("CREATE TABLE IF NOT EXISTS hot_deals (topictitle_retailer VARCHAR(255), title VARCHAR(255), post_voting VARCHAR(255))")

# get the web page content
url = "https://forums.redflagdeals.com/hot-deals-f9/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# find all the div elements with class "thread_info_title"
divs = soup.find_all("div", class_="thread_info_title")

# loop through each div element and extract the relevant information
for div in divs:
  # get the topic title retailer
  topictitle_retailer = div.find("span", class_="topictitle_retailer").text.strip()

  # get the title and the link
  a = div.find("a", class_="topic_title_link")
  title = a.text.strip()

  # get the post voting score
  post_voting = div.find_next_sibling("div", class_="post_voting").text.strip()

  # create an object with the extracted information
  obj = {
    "topictitle_retailer": topictitle_retailer,
    "title": title,
    "post_voting": post_voting,
  }

  # insert the object into the mysql database table
  sql = "INSERT INTO hot_deals (topictitle_retailer, title, post_voting) VALUES (%s, %s, %s)"
  val = (obj["topictitle_retailer"], obj["title"], obj["post_voting"])
  mycursor.execute(sql, val)

# commit the changes to the database
mydb.commit()
