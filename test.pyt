import requests

url = "https://www.costco.ca/AjaxOrderPromotionCmd"

querystring = {"checkoutPage":"review"}

payload = "authToken=159679707%25252CfVET829eO2ptNameuOjwVF6TfOU%25253D&promoCode=QYX9HK4&taskType=A"
headers = {
    "cookie": "ajs_anonymous_id=%2206bab408-a2d0-4565-a619-7fd3ef0b4023%22; s_ecid=MCMID%7C54768245675167095480618975676775244997; _cs_c=1; WRUID20200731=3337330150851493; sto__vuid=c5f6e483c727f57a442e92670a342826; spid=120E36EB-74D8-4829-B6D0-F74744CD2392; BVBRANDID=6b83e076-e471-4d7e-b4df-33fbf8b0ad47; sellpoints_abtesting={}; ajs_user_id=%22jibeizhao%40gmail.com%22; _cc=AUBbHjPZQjiwxbpn9o3mpTwA; CriteoSessionUserId=830981f5d8714376be5b63a149d8cda9; akaas_AS_CA=2147483647~rv=10~id=96e33f839efc7f6b1d5dff28adf2ada6; BVImplnative_review_form=20040_1_0; at_check=true; AMCVS_97B21CFE5329614E0A490D45%40AdobeOrg=1; s_cc=true; WC_SESSION_ESTABLISHED=true; WC_ACTIVEPOINTER=-24%2C10302; invCheckCity=Ottawa; selectedLanguage=-24; C_CLIENT_SESSION_ID=df9216ed-882c-4463-a5f1-ad48f29cbe69; WAREHOUSEDELIVERY_WHS=National%3D00894%2CRegional%3D802-bd; rememberedLogonId=%7B%22id%22%3A%22159679707%22%2C%22hash%22%3A%2296693db99e3271bf8a119782124b0959a54866374859e53e7dbacb12c71104ad531f4654fd588b8850ac9b88ebafb293e0a4f16a211489a0909b38f93d55cd25%22%7D; checkoutMemberTier=Z00020; C_2LOC=true; capp_json=%7B%22coBrandedCreditMax%22%3Afalse%2C%22displayErrorForRenew%22%3Afalse%2C%22displayErrorForCancel%22%3Afalse%2C%22displayErrorForRenewGSHousehold%22%3Afalse%7D; BVImplorder_history=20040_2_0; bvUserToken=5707e0e6921b8b52bf16ef3146ae77df646174653d323032312d31302d3132267573657269643d63303939376130662d343435642d343237342d383136652d37396263646263613335346426656d61696c616464726573733d6a696265697a68616f40676d61696c2e636f6d264d656d6265724e756d6265723d313131383338353337343237; rememberedShowMemberItem=1; AMCV_97B21CFE5329614E0A490D45%40AdobeOrg=-1124106680%7CMCMID%7C54768245675167095480618975676775244997%7CMCAAMLH-1634667248%7C7%7CMCAAMB-1634667248%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1634069648s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.2.0; AKA_A2=A; sp_ssid=1634068334797; JSESSIONID=0000rrkZMwuSbE3dZh9kJR_km2Q:175b16sa4; nonce=y45g4oLrwQIH9Efh; sto__session=1634068336330; rrDisabledPref=1; rrStoreFlag=1; hashedUserId=05531f7db84cff61adaf25b39210a2a2; memberPrimaryPostal=K2G%205Y2; memberPrimaryStateCode=ON; mSign=1; WC_PERSISTENT=DfjuwgMTYEjuEXtzvItHV%2B156WE%3D%0A%3B2021-10-12+12%3A52%3A21.855_1419990510815-845714_10302; WC_AUTHENTICATION_159679707=159679707%2CfVET829eO2ptNameuOjwVF6TfOU%3D; bm_sz=87FE0FD8621F02DECE59E6FE5503E840~YAAQPzorFym0Elh8AQAAmyQQdg3X6dssWIl9/ZZGcN9iNTR2v+I+ShlLRfoQvSje6IbZRCLQPDMp0VPvmP1UeqahbLRCUimdAZpdcy0In0GDNZptH97W0LFCmbmykLnA5dyAAs9c4WyxXtAbU3mUuxGs+KZcK2IFgB4I3So+B6TCE6SN8xAC3HR117sYLZi1eyThlsQsCC1cQRWQZ3tnNQcPpZqgq5XhehSIV2FXYsfwg3i0sKJuCUQ68nz6LYpuo6/kuHd+weJ2hJtnJQjOMzgvudCdoqEj1DiV8epWM7FQ2Q==~3359792~3490886; bm_mi=61096846AD2BC0604D89C6B39F98B984~FUGPHg5ZgqINdL7o5MDZ87swCQ20C3JeJJ9TV5us/Eqs7nYwEMj7r8B9wK4Fk028Twt6SFkWVvYFRe89UCsV74qYII0L3CwQ1tmr9cTdE+33p+E4uoehAr2/ICTBdHFBtO+Lhxn67jR+Ni+CUfRd2/bcN5mHtpioEupgtu/z/y6TkOMjLWh6CxrfIE+gK3pKHyileRaqDw0frRIlvmiJDKz8NzmDCe90ZntZapubm90FCnLTRNy5VejKkEHR6TCIo1faTuKa4dIcoFbf+7OxblzlDrFA/9/L6CHfSL+fC60=; C_LOC=CAON; invCheckPostalCode=K2G+5Y2; invCheckStateCode=ON; ak_bmsc=7CB0B00CFF3799E738B12F52383DCD20~000000000000000000000000000000~YAAQPzorF6u0Elh8AQAAajcQdg2uL51g3SML4nILw/16AaQciP5ke2lELyVjXtgC8BD0yFb45I7ceCwAlVDoDzFlZAwbNVPfL5mgePKU9V9Q6gKZHoc27cDveb5AMUSrjLkZATbIDlynalTHv7CkL1gUG08yQfDf/cNt4rWKxyccNOrBQ3WQt9omy7anggpe5cY+poJT9uxGw2V9XCXsTVfzRr+ngd/A41Q+rsKl/uIXzGrwCW/Eqf0GsYpYLJMOdLNjwg/Yyy8WtSUNcTvyohMjHhjSjS+WDaFiASFiGHN49d4AhF6kZkv2810kXlMg7UxmwBQ40acRVfMe+Lbf63RPeaDUQQFbMEqjpybdJj58yE0WgQWG1QXhM3FRc/mCv6EEWP2qD6Pim9lwidrL1MMi/VqG1UM9mMw4IYS2/OjkFIkf3OgPPQ==; BVBRANDSID=49aa10c6-d4a7-4d71-8bc0-9a67110cd5f5; wcMember=05531f7db84cff61adaf25b39210a2a2%2C1%2CZ00020%2CZ010%2C1%2C1%2CE0002%2CDEFAULT%2C111838537427; flixgvid=flixbe36d0ac000000.69777735; inpsession_4824_b5=A28C5400-A756-6086-EBF0-2FD987F6122E; inptime_4824_b5=0; cartCountCookie=1; lastAddedProductId=2483033; client-zip-short=K1A; cto_bundle=ibhJ6l9jbnRhVFhhYXVadmFGJTJCSFh6Mnc1MGhYSW1VNjNsem5DZldJMVlpU1JBWVpTb2xLQzBsSzg2U2VJOWdFRHhBWSUyQktRa1ZCamd1RzBWRFQyNVR3akxBbFpIaDBpbU45ZlV3UnYlMkJSejFYM0tjMVRTVDJDV0V1SldiTU5KeEtFclBteWFFeVhhNUI0aXZXR3QyN2txUlRmNkdjMXhPcnhpbGNvbWs4YXNTczAwZUprVnZyYWdnaFZORDh2Y29OJTJCaloybA; WC_USERACTIVITY_159679707=159679707%2C10302%2C0%2Cnull%2C1634068341856%2C1634073204476%2Cnull%2Cnull%2Cnull%2Cnull%2CDcbFPMK2TijmenkKls%2F2kkn74DSSuXYjpyo85%2F03TnJugVuqfhhJgWwqToxf6draiwnK9edtr%2FCb8q1sw8wRD4RXTwH%2BHnKVIRWrKNwWbOZCDGyK6xcLx4L%2BLJwRnQteC8fpYybOtkWf%2Fo1TaRfqGY%2BgfAhzhQpKYnrVIDR5jZZgHk6r1iK7ffYPPKxPVDAHuWxR7FapZGMZaj%2FtAANk1Lg%2BROs4QI1QVtDkLsktHPI%3D; sto__count=4; _cs_cvars=%7B%221%22%3A%5B%22Page%20type%22%2C%22Cart%22%5D%2C%222%22%3A%5B%22Category%20Name%22%2C%224K%20%26amp%3B%20OLED%20TVs%22%5D%2C%223%22%3A%5B%22Items%20Count%20In%20Cart%22%2C%221%22%5D%2C%227%22%3A%5B%22Search%20Results%20Count%22%2C%221%22%5D%7D; s_sq=%5B%5BB%5D%5D; costco_f_p_LOCATIONS=%7B%22contract%22%3A%7B%22id%22%3A%22%22%2C%22switch%22%3A%22true%22%7D%7D; _abck=1F59E150354AC7274FEB6E0EB7B325B9~0~YAAQPzorFwdGE1h8AQAAiH0jdgbDuFu1SVABNQ6TtnEL+JVgXr7N7rHUrQp07o9HQsmTRGFUNo8LKiTzNECt++lqVdMsyjo+/0ltyUnUSISQhFxAQTOGZ99y642LBXNg2G8HYqt7cJACPyZrzcStUFaz1rUO1gy02xzIPdeTIq4IXcqKgSiXnYrIxcgbZZfFjgVyNsrghT0xO1ToBuk5TzlG9bcETmF9I9LgFBPkBl24a6deDcjqx/WCVGrJt8RdwM50rR5qKtGQOwzAIem/0qqnQY47S9wGQEpK6QlpLN9icWGktEBihntbo+RBN09tc1DRXYgT5OxBD0OUQY934Jt/Rduu15vpgSlZLyMg+lGDnOF1i+qO8E2YVACOh1e69KvRb1+/E5KdrXMFVoFPINkvMez6TmE=~-1~-1~-1; mbox=PC#47a6acb2b53d4119a39a7e54923a88b6.34_0#1697314412|session#9fc8dbbbb4cd4a2ea900303cd98debd4#1634070194; _cs_id=117266c4-a8f7-a4bb-d6da-339511b4c2d1.1623764866.47.1634069611.1634068334.1586376816.1657928866810; _cs_s=15.1.0.1634071411604; __CT_Data=gpv=164&ckp=tld&dm=costco.ca&apv_81_www33=164&cpv_81_www33=164&rpv_81_www33=158; RT="z=1&dm=www.costco.ca&si=16f4b450-ace0-4fac-a1f6-95384b9d8067&ss=kuoi3elx&sl=d&tt=omn&bcn=%2F%2F173c5b0e.akstat.io%2F&ld=rfs6"; bm_sv=953513096731336333AB8486909C8328~OxeeMcMqVWGXi7MaD19BJYBt3ZffxjWNrBrkkaQnoOPI+umm2zbPrpMfBLMGTX/eEiwvHyEvIOQZ8PNBD7NhoueogKwtTR1bhdzGON/9662T+cHi+IyGTNZ/crd9QDEPfkUhX5AMNGDt6dqBYv277X97rLikk1E3SdzPlMdqdV8=",
    "authority": "www.costco.ca",
    "sec-ch-ua": ""Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "x-requested-with": "XMLHttpRequest",
    "sec-ch-ua-mobile": "?0",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
    "sec-ch-ua-platform": ""macOS"",
    "origin": "https://www.costco.ca",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.costco.ca/SinglePageCheckoutView?storeId=10302&catalogId=11201&langId=-24&krypto=QSJk%2F9ikuEKAlsStNzZ7nBeobR%2BdyYmeDiDWcNvh5pfRr4VcXKv9im1xG7oFc9NvvN%2FrhJQtlZ0gCNxH%2B5tctDFqmRlZbNf%2FnbRokUHUtY2aCF%2B21HRIb9cFm%2Fl0SYtmXgEr%2Bi4NTW77wnLs%2BImgL9w271TuN2AtHUXfQadBbuOEx3r4c55hwPe6H5bn6BVedujaSwMXmw2VALkyOvtUlwMdgosUsetXx9HTDgtsMQqPGGqN4W6cdK%2BByB2mYmV9UssIAvHXwq3mIVA0bOSn9vKIc%2FldaZX1HQZUBHcKGvk%3D&ddkey=http%3AManageShoppingCartCmd",
    "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"
}

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)