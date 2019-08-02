import pandas as pd
#importing date and time
from datetime import datetime, timedelta

from matplotlib import pyplot as plt

#to customize the format of the dates
from matplotlib import dates as mpl_dates 

#loading data
data = pd.read_csv('data.csv')

#converting the date string value to date format
data['Date'] = pd.to_datetime(data['Date'])

#sorting the dates
data.sort_values('Date', inplace = True)

price_date = data['Date']
price_close = data['Close']

#use plot_date to plot the time series graph
plt.plot_date(price_date, price_close, linestyle = 'solid')

#to make the customization
#gcf is use to get current figure
#autofmt_xdates give format to the dates
plt.gcf().autofmt_xdate()

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

#plt.tight_layout()
plt.savefig('time_series1.png')

plt.show()