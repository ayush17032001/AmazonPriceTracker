from pickle import TRUE
import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/gp/product/1784161926/ref=ox_sc_saved_image_7?smid=AT95IG9ONZD7S&psc=1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36'}

def get_price():
    page= requests.get(URL, headers=headers)

    soup= BeautifulSoup(page.content, 'html.parser')

    title= soup.find(id="productTitle").get_text()
    price=soup.find(id="price").get_text()
    converted_price=float(price[1:-1])

    if(converted_price<400):
        send_mail()

    print(title)
    print(converted_price)
    

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('ayushdixit1703.manitbhopal@gmail.com', 'dibmvrttcadrukld')
    
    subject='Price fell down!'
    body='Check the amazon link https://www.amazon.in/gp/product/1784161926/ref=ox_sc_saved_image_7?smid=AT95IG9ONZD7S&psc=1'
    
    msg=f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'ayushdixit1703.manitbhopal@gmail.com', 'ahdt1703@gmail.com', msg
    )
    
    print("Email has been sent")
    
    server.quit()

while(TRUE):
    get_price()
    time.sleep(60*60*24*7)
