#!/usr/bin/env python3

from argparse import ArgumentParser

parser=ArgumentParser()
parser.add_argument("-n", help="Enter the number of the Fibonacci-number you want to calculate.", type=int)
parser.add_argument("--all", help="Specify if you want to print all Fibonacci-numers leading up to the one you entered.", action="store_true")
args=parser.parse_args()


def fibo_inefficient(n):
    if n==0:
        f=0
    elif n==1:
        f=1
    else:
        a=fibo_inefficient(n-1)
        b=fibo_inefficient(n-2)
        f=a+b
    return f

if args.all:
    F = list()
    for number in range(args.n):
        F.insert(number, fibo_inefficient(number))
    print(*F, sep=", ")
else:
    F=fibo_inefficient(args.n)
    print(F)
