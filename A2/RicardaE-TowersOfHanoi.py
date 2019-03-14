#!/usr/bin/env python3

from argparse import ArgumentParser
from sys import stderr

parser = ArgumentParser()
parser.add_argument("-n", help="Enter the number disks you want to move from peg one to peg three. Then run the program and follow the instructions in the output. See stderr for the total amount of disk moves needed.", type=int)
args = parser.parse_args()


def HanoiTowers(n, frompeg, topeg):
    global count
    if n==1:
        print("move disk from "+str(frompeg)+" to "+str(topeg))
        count += 1
    elif n>1:
        unusedpeg=6-frompeg-topeg
        HanoiTowers(n-1, frompeg, unusedpeg)
        print("move disk from "+str(frompeg)+" to "+str(topeg))
        count += 1
        HanoiTowers(n-1, unusedpeg, topeg)


count = 0
HanoiTowers(args.n, 1, 3)
stderr.write(str(count)+"\n")
