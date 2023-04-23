import requests

currencies = {
    'USD' : 1,
    'GBP' : 2,
    'EUR' : 3,
    'CHF' : 4,
    'RUB' : 5,
    'KRW' : 16,
    'CAD' : 20,
}

appid = '730'
country = 'SE'
currency = 3
steamLoginSecure = ''

url = 'http://steamcommunity.com/market/pricehistory'

"""

Navaja, Talon, Ursus, Stiletto

"""

assets = [
    'Prisma Case', 'Prisma 2 Case', 'Horizon Case', 'Clutch Case',
    'Danger Zone Case',
]
data = {}

for asset in assets:
    url = 'http://steamcommunity.com/market/pricehistory'
    history = requests.get(
        url, 
        params={
        'appid': appid,
        'market_hash_name': asset,
        'country': country,
        'currency': currency,
      },
        cookies={
            'steamLoginSecure': steamLoginSecure,
        }
    )
    data[asset] = history.json()['prices']

import numpy as np
dataset = {}
for asset in assets:
    dataset[asset] = {}
    dataset[asset]['price'] = np.array([p[1] for p in data[asset]])
    dataset[asset]['time'] = np.array([p[0].split(':')[0] for p in data[asset]])

from datetime import datetime
import matplotlib.dates
import calendar
import matplotlib.pyplot as plt

m2n = {m: i for i, m in enumerate(calendar.month_abbr)}
del[m2n['']]

for asset in assets:
    dates = []
    for t in dataset[asset]['time']:
        month, day, year, time = t.split(' ')
        dtime = datetime(int(year), m2n[month], int(day), int(time))
        dates.append(dtime)
    plt.plot(matplotlib.dates.date2num(dates), dataset[asset]['price'], label=asset)

plt.title('Assets price over time')
plt.ylabel('Price [€]')
plt.xlabel('Time')
plt.legend(loc='best')
plt.show()


quantity = {}
quantity['Clutch Case'] = 119437
quantity['Danger Zone Case'] = 183661
quantity['Prisma 2 Case'] = 108733
quantity['Prisma Case'] = 101701
quantity['Horizon Case'] = 58031


qp = []
for asset in assets:
    q = quantity[asset]
    p = dataset[asset]['price'][-1]
    print(f'{asset}: {p/q}')
    qp.append(p/q)
    
plt.bar(assets, qp)
plt.show()


p = np.linspace(0.03, 100, num=300)
q = np.linspace(1, 100, num=300)
x, y = np.meshgrid(p, q)

z = x / y

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z, cmap='viridis', rstride=1, cstride=1)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

