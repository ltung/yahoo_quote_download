# -*- coding: utf-8 -*-
"""
Created on Sat May 20 18:58:59 2017

@author: c0redumb
"""

from yahoo_quote_download import yqd


def load_quote(ticker):
    print('===', ticker, '===')
    print(yqd.load_yahoo_quote(ticker, '20150102', '20160104'))


def read():
    # Download quote for stocks
    # TODO: Read symbol from a text file, download data as csv
    load_quote('AAPL')


if __name__ == '__main__':
    read()
