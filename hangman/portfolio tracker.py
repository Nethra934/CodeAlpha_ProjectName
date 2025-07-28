stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "AMZN": 3300,
    "MSFT": 300
}
portfolio = {}
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found in the price list. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        if quantity < 0:
            raise ValueError
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Invalid quantity. Please enter a positive integer.")


total_investment = 0
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_investment += investment
    print(f"{stock}: {qty} shares × ${price} = ${investment}")

print(f"\nTotal Investment: ${total_investment}")


save = input("Do you want to save the result to a file? (yes/no): ").lower()
if save == 'yes':
    file_format = input("Enter file format (txt/csv): ").lower()
    filename = f"portfolio.{file_format}"
    try:
        with open(filename, 'w') as f:
            if file_format == 'txt':
                for stock, qty in portfolio.items():
                    price = stock_prices[stock]
                    investment = price * qty
                    f.write(f"{stock}: {qty} shares × ${price} = ${investment}\n")
                f.write(f"\nTotal Investment: ${total_investment}\n")
            elif file_format == 'csv':
                f.write("Stock,Quantity,Price,Investment\n")
                for stock, qty in portfolio.items():
                    price = stock_prices[stock]
                    investment = price * qty
                    f.write(f"{stock},{qty},{price},{investment}\n")
                f.write(f",,,{total_investment}\n")
            print(f"Portfolio saved to {filename}")
    except Exception as e:
        print("Error saving file:", e)
