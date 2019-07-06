import requests
from bs4 import BeautifulSoup
import re
import smtplib
import time

def checkprice():
    url='https://www.amazon.in/Adidas-Mens-Running-Shoes/dp/B07F34WSKX?pf_rd_p=b06366d8-4e26-4388-a90b-937ef9a48564&pd_rd_wg=r2krw&pf_rd_r=SEGZ91V6E6FEJQ4NGHWS&ref_=pd_gw_unk&pd_rd_w=2h8Zy&pd_rd_r=41c3a983-9595-48bf-96b8-ce9495834ffd&th=1&psc=1'
    headers={"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
    page=requests.get(url,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    price=soup.find(id="priceblock_ourprice").get_text()
    np=price.strip()
    result = re.sub(r'\D+', '', np)
    result=result[:-2]
    print(result)
    if (float(result)>1500):
        sendmail()
    
def sendmail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('vidyun.as@gmail.com','fbpalqiemaofsidf')
    subject='price is low now'
    body="check the link https://www.amazon.in/Adidas-Mens-Running-Shoes/dp/B07F34WSKX?pf_rd_p=b06366d8-4e26-4388-a90b-937ef9a48564&pd_rd_wg=r2krw&pf_rd_r=SEGZ91V6E6FEJQ4NGHWS&ref_=pd_gw_unk&pd_rd_w=2h8Zy&pd_rd_r=41c3a983-9595-48bf-96b8-ce9495834ffd&th=1&psc=1"
    msg=f"subject:{subject}\n\n{body}"
    server.sendmail('vidyun.as@gmail.com','vidyun.as@gmail.com',msg)
    print("email send")
    server.quit()

while(1):
    checkprice()
    time.sleep(60*60)
    