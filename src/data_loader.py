import pandas as ps 
import yfinance as yf 
from statsmodels.datasets import get_rdataset

def load_air_passengers():
    """
    Load built-in Air Passengers dataset
    
    """
    data = get_rdataset("AirPassengers")
    df = data.data
    df.index = pd.range(start='1949-01-01', periods=len(df), freq='MS')
    return df 


def load_stock_data(symbol='AAPL', period='5y'):
    """
    Load stock data from Yahoo Finance
    
    """
    data = yf.Ticker(symbol)
    df = stock.history(period=period)
    return df['close']


def load_sample_data():
    """
    Load sample temperature data
    
    """
    data = ger_rdataset('nhtemp')
    df = data.data
    df.index = pd.range(start='1912-01-01', periods=len(df), freq='YS')
    return df

