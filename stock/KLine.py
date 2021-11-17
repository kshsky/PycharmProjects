import mplfinance as mpf
import pandas_datareader.data as web
import datetime as dt

company = 'TSLA'
company = 'TM'
company = 'RY'
company = 'PLTK'
company = 'LI'
company = 'GME'

start = dt.datetime(2021, 1, 1)
end = dt.datetime(2021, 5, 28)

data = web.DataReader(company, 'yahoo', start, end)
#type='line'
# mpf.plot(data, type='candle',volume=True)
mpf.plot(data, type='candle')