# StockTrader2.0
This code performs a backtest of a simple moving average crossover strategy using the backtrader library. Here's a summary of what the code does:

It imports necessary modules including backtrader, datetime, and yfinance.
The code creates an instance of Cerebro, which is the core of the backtrader system.
Historical stock price data for Apple (AAPL) is downloaded from Yahoo Finance using the yfinance library and stored in the df variable.
The code defines a custom strategy called SmaCross, which implements a simple moving average crossover technique.
A PandasData feed is created using the downloaded data and added to the Cerebro instance for the backtesting process.
The SmaCross strategy, AnnualReturn analyzer, and position sizer are added to the Cerebro instance.
The backtest is executed by running Cerebro, and the results are stored in the teststrat variable.
The code generates a bar plot of the backtest results and saves it as a file named 'backtest_plot.png'.
Finally, an interactive plot of the backtest results is displayed.
In summary, the code combines historical price data with a simple moving average crossover strategy to simulate and analyze the performance of the strategy on the given data.
