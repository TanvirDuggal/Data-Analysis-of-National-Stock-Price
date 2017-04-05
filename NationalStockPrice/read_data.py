# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 13:38:58 2017

@author: Duggal
"""

import pandas as pd
import numpy as np
import quandl
import pickle
import os
import sys

class Read:
    __API_key = 'wyswgogmghRjLJtC-Ax8'
    __Qcode = ''
    __df = ''
    
    def __init__(self, Qcode):
        self.__Qcode = Qcode
        self.GetDataQuandl()
    
    def Get_API(self):
        return self.__API_key
    
    def Set_Qcode(self, Qcode):
        self.__Qcode = Qcode
    def Get_Qcode(self):
        return self.__Qcode
    
    def Set_df(self, df):
        self.__df = df
    def Get_df(self):
        return self.__df
    
    def GetDataQuandl(self):
        try:
            dirname = self.Get_Qcode()
            fname   =  dirname.replace('/', '_')
            fname   = fname + '.pickle'
            if os.path.exists(fname):
                print("Modfying Existing file : " + fname)
                df = quandl.get(self.Get_Qcode(), authtoken = self.Get_API())
                df['Date'] = df.index 
                with open(fname, 'wb') as pickle_out:
                    pickle.dump(df, pickle_out)
                df.to_csv("123.csv")
            else:
                print("Creating Directory " + fname)
                df = quandl.get(self.Get_Qcode(), authtoken = self.Get_API())
                df['Date'] = df.index
                with open(fname, 'wb') as pickle_out:
                    pickle.dump(df, pickle_out)
                df.to_csv("123.csv")
        except Exception as e:
            print("EXCEPTION : " + str(e))
            sys.exit("Error Occured !!! while reading pickle from quandl")
