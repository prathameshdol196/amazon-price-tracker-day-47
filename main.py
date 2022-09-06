
import requests
from bs4 import BeautifulSoup
import smtplib

product_link = "Amazon Product Link"  # amazon  product link

sender_email = "SenderEmailAddress"
password = "SenderEmailAddressPassword"

reciever_email = "ReceiverEmailAddress"

HEADERS = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}  # important headers to be included in the link

response = requests.get(product_link, headers=HEADERS)  # getting the scraped data and storing it in response variable
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")  # created a soup
price = soup.find(class_="a-price-whole")
actual_price = price.getText()

name_of_product = soup.find(id="productTitle", class_="a-size-large product-title-word-break").getText()

if float(actual_price) < 400:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(from_addr=sender_email,
                            to_addrs=reciever_email,
                            msg=f"Subject:Amazon Price Alert! \n\n {name_of_product} is now at Rs.{actual_price} \n\n {product_link}")
        print("msg has been sent")

