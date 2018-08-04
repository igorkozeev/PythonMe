import bs4, requests

# This will handle the actual downloading
res = requests.get('https://coinmarketcap.com/currencies/ethereum/#markets')

# We call 'raise_for_status' method just to make sure that everything works.
# And were no problems with downloading that site.
res.raise_for_status() 

# We pass here the html text we've downloaded,
# and this will return a "beautifulsoup" object.
soup = bs4.BeautifulSoup(res.text, 'html.parser') 

# So this 'soup' object that we have is ready to find html elements
# in the web-page we've downloaded. So we pass the string of the
# CSS selector in 'select()' method.
elems = soup.select('html body div.container.main-section div.row div.col-lg-10.padding-top-1x div.details-panel.flex-container.bottom-margin-2x div.details-panel-item--header.flex-container div.details-panel-item--price.bottom-margin-1x span#quote_price span.h2.text-semi-bold.details-panel-item--price__value')

# Sometimes it might be handy to write it like elems[0].text.strip()
# in order to get rid of white spaces and other garbage.
print('Eth: ' + elems[0].text)
