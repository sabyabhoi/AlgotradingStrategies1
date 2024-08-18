from backtesting import Strategy 

class BuyAndHold(Strategy):
    def init(self):
        self.buy()

    def next(self):
        pass


class OpeningRangeBreakout(Strategy):
    def init(self):
        pass

    def next(self):
        curr_time = self.data.index[-1].strftime('%H:%M')
        if curr_time == '09:05':
            val = (self.data.Close[-1] - self.data.Open[-1]) / self.data.Open[-1] * 100
            if abs(val) >= 0.01:
                if val > 0: self.buy(sl=self.data.Low[-1])
                elif val < 0: self.sell(sl=self.data.High[-1])
        elif curr_time == '03:10':
            self.close()
