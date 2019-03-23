#!/usr/bin/env python3

import fileinput

linecount=0
matrixcount=1
down=[]
right=[]

#Einlesen INPUT
for line in fileinput.input():
    line = line.strip()
    if linecount==0:
        linecount=1
        continue
    if line == "---" and matrixcount==1:
        linecount=0
        matrixcount=2
        continue
    if line == "---" and matrixcount==2:
        break
    line=line.split("   ")
    if matrixcount==1:
        down.append(line)
    if matrixcount==2:
        right.append(line)

#0 Matrix der richtigen Dimension erstellen
MTM=[]
for array in right:
    l=[]
    for array in right:
        l.extend('0')
    MTM.append(l)

#Erste Reihe befüllen
x=1
for item in right[0]:
    wert=float(MTM[0][x-1])+float(right[0][x-1])
    MTM[0][x]=str(wert)
    x+=1


#Erste Spalte befüllen
y=1
for item in down:
    wert=float(MTM[y-1][0])+float(down[y-1][0])
    MTM[y][0]=str(wert)
    y+=1


#Rest befüllen
c=1
for item in right[0]:
    r=1
    for i in right[0]:
        upper=float(MTM[r-1][c])+ float(down[r-1][c])
        left=float(MTM[r][c-1]) + float(right[r][c-1])
        m=max(upper, left)
        MTM[r][c]=str(m)
        r+=1
    c+=1


#letzte Zahl ausgeben
size=r-1
Result=float(MTM[size][size])
print(Result)

