# Inspired by https://github.com/erykml/medium_articles/blob/master/Quantitative%20Finance/introduction_to_backtesting_eur_stocks.ipynb
import numpy as np
import pandas as pd
from yahoofinancials import YahooFinancials
import warnings
import pathlib
warnings.simplefilter(action='ignore', category=FutureWarning)

def download_csv_data(ticker, start_date, end_date, freq, path):
    
    yahoo_financials = YahooFinancials(ticker)

    df = yahoo_financials.get_historical_price_data(start_date, end_date, freq)
    df = pd.DataFrame(df[ticker]['prices']).drop(['date'], axis=1) \
            .rename(columns={'formatted_date':'date'}) \
            .loc[:, ['date','open','high','low','close','volume']] \
            .set_index('date')
    df.index = pd.to_datetime(df.index)
    df['dividend'] = 0
    df['split'] = 1

    # save data to csv for later ingestion
    df.to_csv(path, header=True, index=True)

    # plot the time series
    df.close.plot(title='{} prices --- {}:{}'.format(ticker, start_date, end_date))


folder_path = 'data/tsx/daily'
root_path = '/home/vscode/workspace/zipline-experiments'
data_path = f"{root_path}/{folder_path}"
pathlib.Path(data_path).mkdir(parents=True, exist_ok=True)
download_csv_data(ticker='NTAR.CN', 
                  start_date='2019-05-01', 
                  end_date='2020-12-10', 
                  freq='daily', 
                  path=f'{data_path}/ntar.csv')

download_csv_data(ticker='IDK.CN', 
                  start_date='2019-05-01', 
                  end_date='2020-12-10', 
                  freq='daily', 
                  path=f'{data_path}/idk.csv')

