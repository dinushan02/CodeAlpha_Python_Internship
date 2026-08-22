# CodeAlpha Stock Portfolio Tracker

## 📌 Project Overview

This project is a simple Stock Portfolio Tracker developed using Python as part of the CodeAlpha Python Programming Internship.

The program allows the user to enter stock symbols and quantities, calculates the investment value of each stock, tracks the total portfolio value, and saves the portfolio summary to a text file.

The project uses predefined sample stock prices instead of live stock market data.

## 🎯 Features

- Allows the user to enter stock symbols and quantities.
- Uses a predefined dictionary of stock prices.
- Validates stock symbols.
- Validates quantities to ensure they are greater than 0.
- Handles invalid numeric input using exception handling.
- Allows the user to add multiple stocks to the portfolio.
- Combines quantities when the same stock is entered more than once.
- Calculates the investment value for each stock.
- Calculates the total portfolio value.
- Displays a portfolio summary when the user enters `DONE`.
- Saves the portfolio summary to a `portfolio_summary.txt` file.

## 🛠️ Technologies Used

- Python

## 🧠 Python Concepts Used

- Dictionaries
- `while` loop
- `if-elif-else` statements
- `try-except` exception handling
- User input and output
- String methods
- Dictionary methods
- Arithmetic operations
- File handling
- `with open()` statement

## 📊 Available Stocks

The program uses the following predefined sample stock prices:

| Stock Symbol | Price per Share |
|--------------|-----------------|
| AAPL         | 180             |
| TSLA         | 250             |
| GOOGL        | 150             |
| MSFT         | 420             |
| AMZN         | 200             |

> These are sample prices used for this project and are not live stock market prices.

## 🔄 How the Program Works

1. The program displays the Stock Portfolio Tracker title.
2. The user enters a stock symbol.
3. The program checks whether the stock symbol is valid.
4. The user enters the quantity of shares.
5. The program validates the quantity.
6. The investment value is calculated using the stock price and quantity.
7. If the same stock is entered again, its quantity is added to the existing portfolio quantity.
8. The user can continue adding stocks.
9. When the user enters `DONE`, the program displays the portfolio summary.
10. The total portfolio value is displayed.
11. The portfolio summary is saved to `portfolio_summary.txt`.

## 📄 File Saving

When the user enters `DONE`, the program creates or updates:

```text
portfolio_summary.txt
```

The file contains:

- Stock symbol
- Quantity
- Price per share
- Investment value
- Total portfolio value

## ▶️ How to Run

Make sure Python is installed on your computer.

Run the following command:

```bash
python stock_portfolio.py
```

Example input:

```text
Enter a stock symbol: AAPL
Enter a quantity: 5

Enter a stock symbol: TSLA
Enter a quantity: 2

Enter a stock symbol: DONE
```

## 📁 Project Structure

```text
Stock-Portfolio-Tracker/
│
├── stock_portfolio.py
├── portfolio_summary.txt
└── README.md
```

## 👨‍💻 Author
M. Dinushan