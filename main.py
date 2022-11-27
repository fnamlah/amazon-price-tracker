from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
url = "https://www.amazon.com/GoPro-HERO7-Silver-Commerce-Stabilization/dp/B083C5Q8VJ/ref=sr_1_1_sspa?qid=1669587555&s=electronics&sr=1-1-spons&smid=ANIVUW1SREVVT&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExVVgwTFVJQUFGOVhYJmVuY3J5cHRlZElkPUEwOTM3NzkzR0FVSjVYUUgxSzgxJmVuY3J5cHRlZEFkSWQ9QTA3NTI4MTAxREdFTEVCNEREQ0hRJndpZGdldE5hbWU9c3BfYXRmX2Jyb3dzZSZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get(url=url, headers=header)
website_txt = response.text
# print(website_txt)
soup = BeautifulSoup(website_txt, "lxml")

title = soup.find(name="span", attrs={"id": 'mbc-price-1'})
title_value = title.string
title_strip = title_value.strip()
price = float(title_strip[1:])

target_price = 100.99

if price <= target_price:
    pass
