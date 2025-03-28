import yfinance as yf
import os

def get_last_price(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    todays_data = stock.history(period="1d")
    return todays_data['Close'].iloc[0]

tickers = ["CSMG3.SA","CMIG3.SA", "CMIG4.SA", "PETR3.SA", "USIM5.SA","IBM","THETA-USD", "AMT"]
target_prices = [15, 13,10, 25, 7, 130, 1, 100]


# Store prices and check if any are below target
prices_below_target = False
stock_data = []
for ticker, target in zip(tickers, target_prices):
    last_price = get_last_price(ticker)
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
