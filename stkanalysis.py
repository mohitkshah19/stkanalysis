import streamlit as st
import yfinance as yf

# Function to fetch stock data
def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)
    return stock

# Function to calculate and display fundamental analysis metrics
def display_fundamentals(stock):
    info = stock.info
    st.write("**Company Name:**", info.get('longName', 'N/A'))
    st.write("**Market Capitalization:**", f"${info.get('marketCap', 'N/A'):,}")
    st.write("**P/E Ratio (TTM):**", info.get('forwardPE', 'N/A'))
    st.write("**Price-to-Book Ratio (P/B):**", info.get('priceToBook', 'N/A'))
    st.write("**Return on Equity (ROE):**", info.get('returnOnEquity', 'N/A'))
    st.write("**Return on Capital Employed (ROCE):**", info.get('returnOnAssets', 'N/A'))
    st.write("**EPS (TTM):**", info.get('trailingEps', 'N/A'))
    st.write("**Dividend Yield:**", info.get('dividendYield', 'N/A'))

# Streamlit app layout
st.title('Stock Price and Fundamental Analysis App')

# User input for stock ticker
ticker = st.text_input('Enter the stock ticker symbol (e.g., AAPL, MSFT)', value='AAPL')

# Fetch and display stock data
if ticker:
    stock = fetch_stock_data(ticker)

    st.subheader(f'Stock Data for {ticker}')
    
    # Display fundamental analysis metrics
    display_fundamentals(stock)

    # Display stock price
    st.subheader(f'Price Data for {ticker}')
    stock_data = stock.history(period='1d', interval='1m')
    st.line_chart(stock_data['Close'])
