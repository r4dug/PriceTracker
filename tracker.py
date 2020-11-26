import requests
from bs4 import BeautifulSoup
import smtplib
import time

#Product used for demo: The new Macbook with M1 chip sold at a local website
URL = 'https://www.pcgarage.ro/notebook-laptop/apple/133-macbook-air-13-with-retina-true-tone-apple-m1-chip-8-core-cpu-8gb-512gb-ssd-apple-m1-8-core-gpu-macos-big-sur-gold-int-keyboard-late-2020/'

#My user agent
headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}

#Function where the current price is verified
def check_price():
    page = requests.get(URL,headers=headers)


    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="product_name").get_text()
    price = soup.find('span', {'class':'price_num'}).get_text()
    converted_price = float(price[0:5])

    if (converted_price<6.000):
        send_mail()

    print(title)
    print(converted_price)

#Send mail function
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    #server.login('mail@gmail.com','lrspheniejptfcqr')
    server.login('mail@gmail.com','zaqmlp')
    
    subject = 'Price fell under 6000 lei !!!'
    body = 'Check the pcgarage link https://www.pcgarage.ro/notebook-laptop/apple/133-macbook-air-13-with-retina-true-tone-apple-m1-chip-8-core-cpu-8gb-256gb-ssd-apple-m1-7-core-gpu-macos-big-sur-gold-int-keyboard-late-2020/'
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'sendfrom@gmail.com',
        'sendto@gmail.com',
        msg
    )
    print('Email has been sent!')

    server.quit()

#Run once a day
while(True):
    check_price()
    time.sleep(43200)