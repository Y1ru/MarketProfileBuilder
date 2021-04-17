from market_profile import MarketProfile
import yfinance
from TwitterPost import TwitterPost
import pandas as pd
from datetime import date
from datetime import timedelta

today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

ticker = yfinance.Ticker("ES=F")
#df = ticker.history(start="2021-03-01", end="2021-03-02", interval="1m", actions=False)
df = ticker.history(start= today, end= tomorrow, interval="1m", actions=False)
print(df)

# You can change the mode to volume by replacing mode='tpo' with 'vol'
mp = MarketProfile(df, tick_size=0.5, mode='tpo')

mp_slice = mp[df.index.min() + pd.Timedelta(9.5, 'h'):df.index.min() + pd.Timedelta(16, 'h')]

today = date.today()

a = str("The market profile for ") + \
    str(today) + \
    str(" Initial balance: %.2f, %.2f" % mp_slice.initial_balance()) + \
    str("\nOpening range: %.2f, %.2f" % mp_slice.open_range()) + \
    str("\nPOC: %.2f" % mp_slice.poc_price) + \
    str("\nProfile range: %.2f, %.2f" % mp_slice.profile_range) + \
    str("\nValue area: %.2f, %.2f" % mp_slice.value_area) + \
    str("\nBalanced Target: %.2f" % mp_slice.balanced_target)

print(a)
## TwitterPost(a)

