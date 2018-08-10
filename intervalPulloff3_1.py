import os, time, bs4, requests # We will use the 'os' module to clear screen later
from notify_run import Notify

# Here we're declaring a variable for notification function
notify = Notify()


def getTime(url):

    timeRes = requests.get(url)
    timeRes.raise_for_status()
    timeSoup = bs4.BeautifulSoup(timeRes.text, 'html.parser')
    timeElems = timeSoup.select('#ct')
    return(timeElems[0].text)
    
def getTheValue(url):

    ethRes = requests.get(url)

    ethRes.raise_for_status()

    ethSoup = bs4.BeautifulSoup(ethRes.text, 'html.parser')

    ethElems = ethSoup.select('html body div.container.main-section div.row div.col-lg-10.padding-top-1x div.details-panel.flex-container.bottom-margin-2x div.details-panel-item--header.flex-container div.details-panel-item--price.bottom-margin-1x span#quote_price span.h2.text-semi-bold.details-panel-item--price__value')

    
    return(ethElems[0].text)




seconds = int(0) 
minutes = int(0)
hours = int(0)



# Start of the program This is a first request before the timer
print('ETH ' + getTheValue('https://coinmarketcap.com/currencies/ethereum/#markets'), getTime('https://www.timeanddate.com/worldclock/usa/new-york'))



# Here we set the lowest rate treshold and highest rate treashold
print('Please enter a bottom threshold: ')
bottom = input()

print('Please enter a top threshold: ')
top = input()

print('Please enter a step value in percent: ')
step = input()


# ! Set a checkpoint here. if stepValue > top - bottom then error. And bottom has be < then top.


bottomValue = float(bottom) / 100
topValue = float(top) / 100

# This is average step value
stepValue = float(step) * ((bottomValue + topValue) / 2)
print('stepValue is: ' + str(stepValue))
#print('DEBUG' + str(type(top)) + str(type(stepValue)))
while 1 == 1:
    if seconds > 59:
        seconds = 0
        minutes += 1
            
    if minutes > 59:
        minutes = 0
        hours += 1

    #os.system('cls') # This line line will clear the command prompt
    if seconds == 15 or seconds == 30 or seconds == 45 or seconds == 60:
        v = getTheValue('https://coinmarketcap.com/currencies/ethereum/#markets')
        t = getTime('https://www.timeanddate.com/worldclock/usa/new-york')
        print('ETH ' + v, t)
        if float(v) > float(top):
            #print('met top treshold')
            notify.send('ETH ' + v)
            top = float(top) + stepValue
            bottom = float(bottom) + stepValue
            print('New top treshold has set to ' + str(top) + ' and bottom has set to ' + str(bottom))
        if float(v) < float(bottom):
            #print('met bottom treshold')
            notify.send('ETH ' + v)
            bottom = float(bottom) - stepValue
            top = float(top) - stepValue
            print('New bottom treshold has set to ' + str(bottom) + ' and top has set to ' + str(top))
    seconds =(seconds + 1)


        
    # This line sends a notification when rate meet conditions

    #if float(getTheValue('https://coinmarketcap.com/currencies/ethereum/#markets')) < 340.00 or float(getTheValue('https://coinmarketcap.com/currencies/ethereum/#markets')) > 380:
     #   notify.send('ETH ' + getTheValue('https://coinmarketcap.com/currencies/ethereum/#markets'))
                    
    
     
    
    
    
    time.sleep(1)

