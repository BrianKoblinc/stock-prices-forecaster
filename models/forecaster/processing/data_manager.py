import os
from typing import Optional
from datetime import datetime, timedelta
import pandas as pd
import yfinance as yf
from forecaster.config.core import DATASET_DIR

class Extract():
    def __init__(self, ticker_list, years_bf: Optional[int] = 0, months_bf: Optional[int] = 0, days_bf: Optional[int] = 0):
        self.ticker_list = ticker_list
        self.end = datetime.now()
        self.start = datetime(self.end.year - years_bf, self.end.month - months_bf, self.end.day - days_bf)
        self.load_path = f"{DATASET_DIR}/"

    def _read(self):
        self.data = {}
        files = os.listdir(self.load_path)
        self.stocks_data = [i[:-26] for i in files]

        for i in list(set(self.stocks_data) & set(self.ticker_list)):
            date1 = files[self.stocks_data.index(i)][-14:-4]
            start_date_file = datetime(int(date1[:4]), int(date1[5:7]), int(date1[8:10]))
            date2 = files[self.stocks_data.index(i)][-25:-15]
            end_date_file = datetime(int(date2[:4]), int(date2[5:7]), int(date2[8:10]))

            start_date_inter = max(start_date_file, self.start)
            end_date_inter = min(end_date_file, self.end)

            if start_date_inter <= end_date_inter:
                if self.start > start_date_file and self.end > end_date_inter:
                    serie = pd.concat([pd.read_csv(os.path.join(self.load_path, files[self.stocks_data.index(i)])).set_index('Date')['Adj Close'],
                                       yf.download(i, end_date_inter + timedelta(days=1), self.end)['Adj Close']])
                    serie.index = pd.to_datetime(serie.index)
                    self.data[i] = serie.loc[self.start:self.end]
                    self.ticker_list.remove(i)

        for file in [i for i in files if '.ipynb_checkpoints' not in i]:
            os.remove(os.path.join(self.load_path, file))

    def _load(self):
        for stock in self.data.keys():
            self.data[stock].to_csv(os.path.join(self.load_path, f"{stock}_{self.data[stock].index.max().date()}_{self.data[stock].index.min().date()}.csv"))

    def run(self):
        self._read()
        for stock in self.ticker_list:
            self.data[stock] = yf.download(stock, self.start, self.end)['Adj Close']
        self._load()
        return self.data
