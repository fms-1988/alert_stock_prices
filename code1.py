import yfinance as yf
import os

def get_last_price(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    todays_data = stock.history(period="1d")
    return todays_data['Close'].iloc[0]

tickers = ["AAPL", "MSFT"]
target_prices = [2000, 2000]  # Example target prices for AAPL and MSFT

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
        for data in stock_data:
            file.write(f"<tr><td>{data[0]}</td><td>${data[1]:.2f}</td></tr>")
        
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
import smtplib
user = srt(user_)
pw   = srt(pw_)
host = 'email-smtp.us-east-2.amazonaws.com'
port = 465
me   = u'alert@carbonprice.top '
you  = ('fms.morelli@gmail.com',)
body = 'Test'
msg  = ("From: %s\r\nTo: %s\r\n\r\n"
       % (me, ", ".join(you)))

msg = msg + body

s = smtplib.SMTP_SSL(host, port, 'yourdomain')
s.set_debuglevel(1)
s.login(user, pw)
s.sendmail(me, you, msg)
'''
