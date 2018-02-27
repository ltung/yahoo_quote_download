# -*- coding: utf-8 -*-
import csv
from yahoo_quote_download import yqd


def write_csv(ticker):
    f = open('./data/'+ticker+'.csv', 'w+')
    print(yqd.load_yahoo_quote(ticker, '20150102', '20160104'), file=f)
    f.close()


def read():
    # Download quote for stocks
    file = open('list.txt', 'r')
    symbols = []
    for line in file:
        symbols.append(line[:-1])
    for symbol in symbols:
        print(symbol)
        write_csv(symbol)


if __name__ == '__main__':
    read()
