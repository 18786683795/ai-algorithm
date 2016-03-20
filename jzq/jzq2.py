#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random,sys,cPickle,time,math
from datetime import datetime
#from multiprocessing import Pool
random.seed(datetime.now())

def initweightlayer(n):
    weightlayer = []
    for i in xrange(n*9):
        weightlayer.append(random.random())
    return weightlayer


def runnetwork(i, w, n):
    for x in xrange(n-1):
        ws = x * 9
        print ('i[x]', i[x])
        i.(reduce(lambda x,y:x+y, map(lambda x,y:x*y, i[x], w[ws:ws+9])))

def printBoard(board):
    def R(o):
        return repr(o).replace('2', 'X').replace('1', 'O').replace('0', '_').replace(',', ' ').replace('(', '|').replace(')', '|')
    print(R((board[0], board[1], board[2])) + ' 0 1 2')
    print(R((board[3], board[4], board[5])) + ' 3 4 5')
    print(R((board[6], board[7], board[8])) + ' 6 7 8')
    print('-'*19)

if __name__ == '__main__':

    layernum = 3
    weight = initweightlayer(layernum)

    inputlayer = [[0,0,0,0,0,0,0,0,0,], ]
    while True:
        runnetwork(inputlayer, weight, layernum)
        output = inputlayer[layernum - 1]
        output.sort(reserve = True)
        inputlayer = inputlayer[0:1]
        for idx, v in enumerate(output):
            if inputlayer[0][idx] == 0:
                inputlayer[0][idx] = v
                break
        else:
            break
        printBoard(inputlayer[0])
