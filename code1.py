import yfinance as yf
import os
import time
'''
def get_last_price(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    todays_data = stock.history(period="1d")
    return todays_data['Close'].iloc[0]
'''
def get_last_price(ticker_symbol, retries=3, delay=30):
    for attempt in range(retries):
        try:
            stock = yf.Ticker(ticker_symbol)
            todays_data = stock.history(period="1d")
            return todays_data['Close'].iloc[0]
        except yf.exceptions.YFRateLimitError as e:
            print(f"Rate limit hit. Retry {attempt + 1}/{retries}")
            time.sleep(delay)
        except Exception as e:
            print(f"Other error: {e}")
            break
    return None
    
tickers = ["ALOS3F.SA","ORVR3.SA","CMIG3.SA",  "USIM5.SA","IBM","THETA-USD", "AMT"]
target_prices = [20,40,13, 7, 130, 1, 100]


# Store prices and check if any are below target
prices_below_target = False
stock_data = []
for ticker, target in zip(tickers, target_prices):
    last_price = get_last_price(ticker)
    time.sleep(20)  # wait 20 seconds between requests
    stock_data.append((ticker, last_price))
    if last_price < target:
        prices_below_target = True


# Save the stock data to alert.html if any price is below target
if prices_below_target:
    file_path = os.path.abspath("data/")
    alert_file = os.path.join(file_path, "alert.html")
    
    with open(alert_file, 'w') as file:
        # Write beginning of HTML content and table headers
        file.write("<html><head><style>table, th, td {border: 1px solid black; border-collapse: collapse;} th, td {padding: 10px;}</style></head><body>")
        file.write("<table>")
        file.write("<tr><th>Ticker</th><th>Last Price</th></tr>")
        
        # Write stock data
        for ticker, last_price in stock_data:
            # Get the target price for the current ticker
            target = target_prices[tickers.index(ticker)]

            # Skip if last_price is None or target is None
            if last_price is None or target is None:
                continue
    
            # Check if the last price is less than the target price, if true set the background color to green
            bgcolor = "background-color: lightgreen;" if last_price < target else ""
            file.write(f"<tr><td>{ticker}</td><td style='{bgcolor}'>${last_price:.2f}</td></tr>")
        
        # End table and HTML content
        file.write("</table></body></html>")


'''
# Save the stock data to alert.md if any price is below target
if prices_below_target:
    file_path = os.path.abspath("data/")
    alert_file = os.path.join(file_path, "alert.md")
    
    with open(alert_file, 'w') as file:
        # Write table headers
        file.write("| Ticker | Last Price |\n")
        file.write("|--------|------------|\n")
        
        # Write stock data
        for data in stock_data:
            file.write(f"| {data[0]} | ${data[1]:.2f} |\n")
'''

'''
#send email using AWS SES SMTP (this code works well)
#use boto3. understand using chatgpt
'''
