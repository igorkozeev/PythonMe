import os, time, bs4, requests # We will use the 'os' module to clear screen later

def getTheValue(url):

    ethRes = requests.get(url)

    ethRes.raise_for_status()

    ethSoup = bs4.BeautifulSoup(ethRes.text, 'html.parser')

    ethElems = ethSoup.select('html body div.container.main-section div.row div.col-lg-10.padding-top-1x div.details-panel.flex-container.bottom-margin-2x div.details-panel-item--header.flex-container div.details-panel-item--price.bottom-margin-1x span#quote_price span.h2.text-semi-bold.details-panel-item--price__value')

    print(ethElems[0].text)




###########################################################

seconds = int(0) 
minutes = int(0)
hours = int(0)

 

while 1 == 1:
    if seconds > 59:    
        seconds = 0
        minutes += 1
    if seconds == 10:
        getTheValue('https://coinmarketcap.com/currencies/ethereum/#markets')
    if minutes > 59:
        minutes = 0
        hours += 1

    os.system('cls') # This line line will clear the command prompt
    seconds =(seconds + 1)
    print (hours,':',minutes,':',seconds)
    time.sleep(1)

