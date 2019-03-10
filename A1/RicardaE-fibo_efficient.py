#!/usr/bin/env python3

from argparse import ArgumentParser

parser=ArgumentParser()
parser.add_argument("-n", help="Enter the number of the Fibonacci-number you want to calculate.", type=int)
parser.add_argument("--all", help="Specify if you want to print all Fibonacci-numers leading up to the one you entered.", action="store_true")
args=parser.parse_args()


def fibo_efficient(m):
    f=[0,1]
    for number in (range(m-1)):
        k=f[number+1]+f[number]
        f.insert(number+2,k)
    return f[m]

if args.all:
    F = list()
    for number in range(args.n):
        F.insert(number, fibo_efficient(number))
    print(*F, sep=", ")
else:
    F=fibo_efficient(args.n)
    print(F)
