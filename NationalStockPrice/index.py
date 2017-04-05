# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:54:33 2017

@author: Duggal
"""
import importdata
import read_data
import os
import sys

def Main():
    Qcode = input("Enter QCode from Quandl : ")
    fname = Qcode.replace('/', '_')
    fname = fname + ".pickle"
    if os.path.exists(fname):
        print("----------File already exist----------")
        print("Do you wish to plot existing graph or get a fresh version")
        res = input("1. Plot Graph " + "\n" + "2. Modify Graph" + "\n")
        print("--------------------------------------------------------")
        if res == '1':
            print("Please wait while your graph is been set up")
            dataold = importdata.getData(Qcode)
        elif res == '2':
            print("Please wait while the fresh copy of graph is been downloaded")
            datamody = read_data.Read(Qcode)
            print("Graph data updated, setting up graph")
            dataold = importdata.getData(Qcode)
        else:
            print("---------------Invalid Entry--------------")
    else:
        print("------------FILE Does not EXIST-----------")
        print("Permission to download the data")
        yn = input("1. YES" + '\n' + "2. NO" + '\n')
        if yn == '1':
            datanew = read_data.Read(Qcode)
            print("Graph data downloaded, setting up graph")
            dataold = importdata.getData(Qcode)
        elif yn == '2':
            print("Thank you for using our service")
        else:
            print("---------------Invalid Entry--------------")
Main()