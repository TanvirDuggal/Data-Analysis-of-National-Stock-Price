# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 15:58:25 2017

@author: Duggal
"""
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.style as style
import numpy as np
import pickle
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
import pandas.tseries.converter as converter
import sys
style.use("fivethirtyeight")
c = converter.DatetimeConverter()
fig = plt.figure()

class getData:
    __Qcode = ''
    def __init__(self, Qcode):
        self.Set_Qcode(Qcode)
        self.GetPickleData()
    
    def Set_Qcode(self, Qcode):
        self.__Qcode = Qcode
    def Get_Qcode(self):
        return self.__Qcode
    
    def GetPickleData(self):
        fname = self.Get_Qcode()
        fname = fname.replace('/', '_')
        fname = fname + '.pickle'
        
        with open(fname, 'rb') as readPickle:
            df = pickle.load(readPickle)
    
        self.CreatingGrids(df)
        
    def CreatingGrids(self, df):
       try:
          MA1 = 10
          MA2 = 30
          ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan = 1, colspan = 1)
          plt.title("STOCK : " + self.Get_Qcode(), fontsize = 10)
          plt.ylabel("Open", fontsize = 13)
          ax2 = plt.subplot2grid((6, 1), (1, 0), rowspan = 4, colspan = 1, sharex = ax1)
          plt.ylabel("Price", fontsize = 13)
          ax3 = plt.subplot2grid((6, 1), (5, 0), rowspan = 1, colspan = 1, sharex = ax1)
          plt.ylabel("Close", fontsize = 13)
           
          start = len(df['Date'][MA2-1:])
          ax1.plot_date(df['Date'][-start:], df['Open'][-start:], '-', label = "Open Price", linewidth = 2)
          ax1.yaxis.set_major_locator(mticker.MaxNLocator(nbins = 4, prune = "lower"))
           
          ohlc = []
          x = 0
          y = len(df['Date'])
           
          while x<y:
              s = matplotlib.dates.date2num(df['Date'][x])
              append_me = s, df['Close'][x], df['High'][x], df['Low'][x], df['Open'][x], df['Total Trade Quantity'][x]
              ohlc.append(append_me)
              x += 1
          
          candlestick_ohlc(ax2, ohlc[-start:], width = 0.4, colorup = "g", colordown = "r")
            
          ma1 = self.Moving_Object(df['Close'], MA1)
          ma2 = self.Moving_Object(df['Close'], MA2)
           
          
          ax2.yaxis.set_major_locator(mticker.MaxNLocator(nbins = 6, prune = "lower"))
          ax2.grid(True)
           
          ax3.plot(df['Date'][-start:], ma1[-start:], linewidth = 1, color = 'g')
          ax3.plot(df['Date'][-start:], ma2[-start:], linewidth = 1, color = 'r')
          
          ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
          ax3.xaxis.set_major_locator(mticker.MaxNLocator(10))
          ax3.yaxis.set_major_locator(mticker.MaxNLocator(nbins = 3, prune = "upper")) 
           
          for label in ax3.xaxis.get_ticklabels():
            label.set_rotation(45)
            label.set_fontsize(10)
           
          plt.setp(ax1.get_xticklabels(), visible = False)
          plt.setp(ax2.get_xticklabels(), visible = False)
          plt.subplots_adjust(left = 0.09, right = 0.94, top = 0.90, bottom = 0.20, hspace = 0 )
            
          for tick in ax1.yaxis.get_ticklabels():
              tick.set_fontsize(10)
               
          for tick in ax2.yaxis.get_ticklabels():
              tick.set_fontsize(10)
               
          for tick in ax3.yaxis.get_ticklabels():
              tick.set_fontsize(10)
           
          plt.show()
       except Exception as e:
           print("EXCEPTION : " + str(e))
           sys.exit("ERROR OCCURED !! while import data from pickle")
       
        
    def PlotGraph(self, df): 
       av = df['Open'][0]
       plt.fill_between(df['Date'], df['Open'], av, where = (df['Open'] > av), facecolor = 'g', alpha = 0.8) 
       plt.fill_between(df['Date'], df['Open'], av, where = (df['Open'] < av), facecolor = 'r', alpha = 0.8)
       plt.show()
       
    def Moving_Object(self, values, window):
        weights = np.repeat(1.0, window)/window
        smas    = np.convolve(values, weights, "valid")
        return smas
    
