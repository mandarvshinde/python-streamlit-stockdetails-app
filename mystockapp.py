import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime

def get_stock_name(symbol):
    # Retrieve the full name of the stock based on its symbol
    try:
        stock_info = yf.Ticker(symbol).info
        return stock_info['longName']
    except Exception as e:
        return None

def main():
    st.title("View Current Stock Price and Historical Data")

    # Input for user to enter stock symbol
    stock_symbol = st.text_input("**Enter Stock Symbol** (e.g., AAPL for Apple, etc. See [**NYSE Stock Symbols**](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt))")

    if stock_symbol:
        stock_name = get_stock_name(stock_symbol)
        if stock_name:
            try:
                # Retrieve live stock data
                stock_data = yf.Ticker(stock_symbol)
                current_price = stock_data.history(period='1d')['Close'][0]
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                st.success(f"**Current Price** for **{stock_name}** **({stock_symbol})** at {current_time}: **${current_price:.2f}**")

            except Exception as e:
                st.error(f"Error: {e}")
                return
        else:
            st.error("Invalid stock symbol. Please enter a valid symbol.")

    # Date range slider
    start_date = st.date_input("Start Date", pd.to_datetime("2010-01-01"))
    end_date = st.date_input("End Date", pd.to_datetime("today"))

    # Button to retrieve historical stock data
    if st.button("Get Historical Data"):
        if stock_symbol:
            try:
                # Get historical prices for this ticker
                ticker_data = yf.download(stock_symbol, start=start_date, end=end_date)
                
                # Drop the 'Adj Close' column
                ticker_data.drop(columns=['Adj Close'], inplace=True)
                
                # Display historical data
                st.subheader("Historical Prices Table")
                st.write(ticker_data, width=1000)

                # Plot closing price
                st.subheader("Historical Closing Price")
                st.line_chart(ticker_data['Close'])

                # Plot volume
                st.subheader("Historical Volume")
                st.line_chart(ticker_data['Volume'])

            except Exception as e:
                st.error(f"Error: {e}")
                return
        else:
            st.warning("Please enter a stock symbol.")

if __name__ == "__main__":
    main()
