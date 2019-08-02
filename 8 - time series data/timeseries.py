import pandas as pd
from matplotlib import pyplot as plt

#importing date and time
from datetime import datetime, timedelta

#to customize the format of the dates
from matplotlib import dates as mpl_dates 

#loading data
dates = [
    datetime(2019, 5, 24),
    datetime(2019, 5, 25),
    datetime(2019, 5, 26),
    datetime(2019, 5, 27),
    datetime(2019, 5, 28),
    datetime(2019, 5, 29),
    datetime(2019, 5, 30)
]

y = [0, 1, 3, 4, 6, 5, 7]

#use plot_date to plot the time series graph
plt.plot_date(dates, y, linestyle = 'solid')

#to make the customization
#gcf is use to get current figure
#autofmt_xdates give format to the dates
plt.gcf().autofmt_xdate()

#changing the format
date_format = mpl_dates.DateFormatter('%b, %d %Y')

#setting the format to the axis
#gca gets current axis
plt.gca().xaxis.set_major_formatter(date_format)

plt.tight_layout()
plt.savefig('time_series.png')

plt.show()