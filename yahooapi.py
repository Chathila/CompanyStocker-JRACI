import numpy as np
import pandas as pd
import matplotlib as plt
import yfinance as yf
import seaborn as sns

import plotly.express as px
import datapane as dp

def grapher(name):
    tick = yf.download(name, period='MAX', Interval='1d')
    tick_chart = px.line(tick['Close'], 
                           title='{0} Daily Close Price'.format(name), 
                           color_discrete_map={'Close':'green'}, 
                           width=800, height=800)
    tick_chart.show()

#print(grapher("AAPL"))
