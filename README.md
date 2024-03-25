# Stock Price Viewer

This application allows users to view the current stock price and historical data for a given stock symbol. It is built using Streamlit and utilizes the Yahoo Finance API to retrieve stock data.

## Features

- **Current Stock Price**: Users can enter a stock symbol and view the current price of the stock along with its full name.
- **Historical Data**: Users can specify a date range and retrieve historical stock prices for the selected stock symbol.
- **Interactive Visualization**: The application provides interactive line charts to visualize historical closing prices and volume.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/username/repo.git
    cd repo
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

4. Enter a stock symbol in the text input field and click on the "Get Historical Data" button to retrieve historical data.

## Input

- **Enter Stock Symbol**: Users can input the stock symbol (e.g., AAPL for Apple) to view its current price and historical data. A list of available stock symbols can be found [here](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt).

## Dependencies

- Streamlit
- yfinance
- pandas

## Note

- In case of an invalid stock symbol, an error message will be displayed prompting the user to enter a valid symbol.
- The application may experience delays in retrieving data depending on network conditions and the performance of the Yahoo Finance API.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/) - For creating interactive web apps with Python.
- [Yahoo Finance](https://finance.yahoo.com/) - For providing financial data through their API.

## Contributors

- [Mandar Shinde](https://github.com/mandarvshinde)
