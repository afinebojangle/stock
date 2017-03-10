from yahoo_finance import Share

import pandas as pd

def make_capm_data_frame(ticker, index, start_date, end_date):
    
    ticker = Share(ticker)
    
    if index == 'SP500':
        index = Share('^GSPC')
        
    ticker_results = ticker.get_historical(start_date, end_date)
    
    index_results = index.get_historical(start_date, end_date)
    
    date_vector = []
    ticker_vector = []
    
    for item in ticker_results:
        date_vector.append(item.pop('Date'))
        ticker_vector.append(float(item.pop('Adj_Close')))
        
    index_vector = []
    
    for item in index_results:
        if item.pop('Date') in date_vector:
            index_vector.append(float(item.pop('Adj_Close')))
            
    
    capm_data = pd.DataFrame({'date': date_vector, 'ticker': ticker_vector, 'index': index_vector})
    
    return capm_data