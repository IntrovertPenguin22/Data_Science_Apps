import yfinance as yf
import streamlit as st

st.write("""
### Hi! I'm ADII. It's a normal web app showing opening and closing price of $TSLA stock and Volume throughtout the year 2020 using yfinance!
# Simple Stock Price App

# Shown are the stock **closing price** and **volume** of beloved Tesla!
""")

tickerSymbol = 'TSLA'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1y', start='2020-1-1', end='2020-12-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.write("""
## This chart showing opening and closing price of $TSLA stock.
""")
st.line_chart(tickerDf.Close)
st.write("""
## This chart showing opening and closing volume of $TSLA stock.
""")
st.line_chart(tickerDf.Volume)

st.write("""
## Follow me on 
[Github](https://github.com/IntrovertPenguin22)
[Kaggle](https://www.kaggle.com/penguin22)
[Twitter](https://www.twitter.com/Penguin02919956)
## Contact me by _Email_
introvert.penguin@protonmail.com
""")