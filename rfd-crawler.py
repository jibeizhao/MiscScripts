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

  # check if the object exists in the database table
  sql = "SELECT * FROM hot_deals WHERE topictitle_retailer=%s AND title=%s"
  val = (obj["topictitle_retailer"], obj["title"])
  mycursor.execute(sql, val)

  # if it exists, update the post voting value and send an email if needed
  if mycursor.fetchone():
    sql = "UPDATE hot_deals SET post_voting=%s WHERE topictitle_retailer=%s AND title=%s"
    val = (obj["post_voting"], obj["topictitle_retailer"], obj["title"])
    mycursor.execute(sql, val)

    # check if the old value is less than 10 and the new value is larger than 10
    old_value = int(mycursor.fetchone()[2])
    new_value = int(obj["post_voting"])

    # if yes, send an email to foo@bar.com with the title
    if old_value <10 and new_value >10:
      import smtplib

      # create a SMTP object for gmail server
      server=smtplib.SMTP('smtp.gmail.com',587)

      # start TLS for security
      server.starttls()

      # login with your gmail account credentials
      server.login('yourgmailaccount','yourgmailpassword')

      # compose a message to be sent
      message='Subject: {}\n\n{}'.format(obj['title'], 'This deal has more than ten votes now!')

      # send an email to foo@bar.com with the message
      server.sendmail('yourgmailaccount','foo@bar.com',message)

      # close the connection
      server.quit()
