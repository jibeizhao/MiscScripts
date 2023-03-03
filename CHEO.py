import requests
import random
import json
import smtplib



url = "https://mychart.kidshealthalliance.ca/mychart/OpenScheduling/OpenScheduling/GetScheduleDays?noCache=" + str(random.random())

payload = "view=grouped&specList=205&vtList=1172721&start=&filters=%7B%22Providers%22%3A%7B%7D%2C%22Departments%22%3A%7B%7D%2C%22DaysOfWeek%22%3A%7B%7D%2C%22TimesOfDay%22%3A%22both%22%7D"
headers = {
  'Accept': '*/*',
  'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
  'Connection': 'keep-alive',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'Cookie': 'MyChart_Session=o2yjsoc4jfoe2lavpkm5pcta; __RequestVerificationToken_L215Y2hhcnQ1=umlMEFBpouAfkhd5MS6vgPzAytShGJztTI8gmW0-BwqkyOsgV3F52Xdje7tsgXcEK11lEGzGkODqOkma-iPMHl4kpAY1; MyChartLocale=en-CA; MyChartAffinity=ffffffffaf1e3c0745525d5f4f58455e445a4a42378b; ASPSESSIONIDCGSCASRR=HJHIABGBOFHNCJHGAFGJEIND; .WPCOOKIE4mychart=4979E7A1D2ED94BEA31E30AD3ABBD6EFF239DB0C06629BFEEADDA077908EB422F75ECB1C6F867E67B5C0B4C90FFFE71B25F11574DDF3567DA857115F15CAA0D5F4B3B102CCC3AFBFD38F97E0F0881639FAFF3922AB4829DC2D13A864FD5D8ACA17E016FAF382B69C906B40F816C730951959ECAF06DC0BC099D0953D6B0B106B25726FCB5203FC0B4A645FE75573D2702F151615380677B269B1B12DAF4779AB63794A6D0AFF6FF8294F495A78C73059DA96A5629E85ABB90F57806AB4CD28D0FA795104AC36F375D1F6BCB8C4EEA8BDEED8752CA0E63B6FF39B0E30456EFBB75B377687215E8DD54F7BB42D5BDC03D3F311518C',
  'Origin': 'https://mychart.kidshealthalliance.ca',
  'Referer': 'https://mychart.kidshealthalliance.ca/mychart/openscheduling?lang=canadianenglish?utm_source=OPH&utm_medium=OPH_COVIDTesting_Page&utm_campaign=Coronavirus&utm_content=CHEO_Booking_Form',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest',
  '__RequestVerificationToken': 'JDSwXvT4tH9Xx90_0CCoz2beWeiPrua0wdfXuNj6GH7W85xX47ihAU5jZaokQOhF4FBlKvoyigmtLUfNgR2scTsW0-Y1',
  'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"'
}

response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)
res = json.loads(response.text)




if len(res['AllDays']) >0:

    TO = 'jibeizhao@gmail.com'
    SUBJECT = 'Cheo available!!! $'
    TEXT = 'https://mychart.kidshealthalliance.ca/mychart/openscheduling?lang=canadianenglish?utm_source=OPH&utm_medium=OPH_COVIDTesting_Page&utm_campaign=Coronavirus&utm_content=CHEO_Booking_Form'

    gmail_sender = 'jakediscountnotifier@gmail.com'
    gmail_passwd = 'appozmvvpahxmoku'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)
    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % gmail_sender,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])
    server.sendmail(gmail_sender, [TO], BODY)
    print("Available")
else:
    print("Not available")
