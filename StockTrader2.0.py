import backtrader as bt
from datetime import date
import yfinance as yf

cerebro = bt.Cerebro()

df = yf.download('AAPL', start='2010-01-01')

print(df)

class SmaCross(bt.Strategy):
    def __init__(self):
        sma1 = bt.ind.SMA(period=50)  # fast moving average
        sma2 = bt.ind.SMA(period=200)  # slow moving average
        self.crossover = bt.ind.CrossOver(sma1, sma2)  # crossover signal

    def next(self):
        if not self.position:  # not in the market
            if self.crossover > 0:  # if fast crosses slow to the upside
                self.buy()  # enter long
        elif self.crossover < 0:  # in the market & cross to the downside
            self.close()  # close long position

feed = bt.feeds.PandasData(dataname=df)
cerebro.addstrategy(SmaCross)
cerebro.adddata(feed)
cerebro.addanalyzer(bt.analyzers.AnnualReturn)
cerebro.addsizer(bt.sizers.PercentSizer, percents=10)  # Percent of capital being invested each trade

teststrat = cerebro.run()
cerebro.plot(style='bar', filename='backtest_plot.png')
cerebro.plot()
