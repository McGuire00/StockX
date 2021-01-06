import requests
from datetime import datetime


def clock():
    current = datetime.now()
    clock_format = current.strftime('%Y/%m/%d %I:%M:%S:%f')
    return(str(clock_format) + " CST")

print(clock())
print()

print('To only show shoes with lower asks higher than: Ex $300 ')
price = input('Enter an amount. If you wish to see all results enter "0"... ')
print()


s = requests.session()

url = 'https://stockx.com/api/browse?productCategory=sneakers&sort=release_date&order=ASC&releaseTime=gte-1609912800'

headers = {
'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
}

page = s.get(url, headers=headers)

data = page.json()

for chart in data['Products']:
    names = chart['title']
    release_date = chart['traits'][-1]['value']

    lowest_ask = chart['market']['lowestAsk']
    ask_num = chart['market']['numberOfAsks']

    highest_bid = chart['market']['highestBid']
    bid_num = chart['market']['numberOfBids']

    last_sale = chart['market']['lastSale']

    if lowest_ask >= int(price):
        print(names + ' ::: ' + '$'+str(lowest_ask))
        print('Release: ', release_date)
        print('Total asks ::: ', ask_num)
        print('Total bids ::: ', bid_num, 'Highest bid ::: ' + '$' + str(highest_bid))
        print()
