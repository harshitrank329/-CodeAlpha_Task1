def stock_portfolio_tracker():

    stock_prices = {"AAPL": 180, "TSLA": 250, "GOOG": 2800, "AMZN": 3500, "MSFT": 300}
    portfolio = {}
    total_investment = 0

    print("Welcome to Stock Portfolio Tracker!")
    print("Available stocks and their prices:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")

    while True:
        stock_name = input("Enter stock name (or type 'done' to finish): ").upper()
        if stock_name == "DONE":
            break

        if stock_name not in stock_prices:
            print("Invalid stock name. Please choose from the available stocks.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock_name}: "))
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue

        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
        total_investment += stock_prices[stock_name] * quantity

    print("\nYour Portfolio:")
    for stock, quantity in portfolio.items():
        print(f"{stock}: {quantity} shares")

    print(f"Total Investment Value: ${total_investment}")

    save_option = input("Do you want to save the result to a file? (yes/no): ").lower()
    if save_option == "yes":
        with open("portfolio.txt", "w") as file:
            file.write("Your Portfolio:\n")
            for stock, quantity in portfolio.items():
                file.write(f"{stock}: {quantity} shares\n")
            file.write(f"Total Investment Value: ${total_investment}\n")
        print("Portfolio saved to portfolio.txt")

if __name__ == "__main__":
    stock_portfolio_tracker()