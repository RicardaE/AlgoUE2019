#!/usr/bin/env python3

from argparse import ArgumentParser
from sys import stderr
from Bio import SeqIO
from sys import stdin

#matching scores
parser = ArgumentParser()
parser.add_argument("--match", help="Enter a matching score for the alignment if it should differ from 1.", type=int, default=1)
parser.add_argument("--mismatch", help="Enter a mismatching score for the alignment if it should differ from -1.", type=int, default=-1)
parser.add_argument("--gap", help="Enter a gap score for the alignment if it should differ from -2.", type=int, default=-2)
args = parser.parse_args()

match = args.match
mismatch = args.mismatch
gap = args.gap

#Sequences von FASTA
SequenceIDs=[]
Sequences=[]
for Sequence in SeqIO.parse(stdin, "fasta"):
    SequenceIDs.append(str(Sequence.id))
    Sequences.append(str(Sequence.seq))

Sequence1 = Sequences[0]
Sequence2 = Sequences[1]
SequenceID1 = SequenceIDs[0]
SequenceID2 = SequenceIDs[1]

length1=len(Sequence1)
length2=len(Sequence2)

#0 Matrix der richtigen Dimension erstellen
MTM=[]
for item in range(length2+1):
    l=[]
    for i in range(length1+1):
        l.extend('0')
    MTM.append(l)

#Erste Reihe befüllen
x=1
for item in range(length1):
    Wert=float(MTM[0][x-1])+float(gap)
    MTM[0][x]=str(Wert)
    x+=1

#Erste Spalte befüllen
y=1
for item in range(length2):
    Wert=float(MTM[y-1][0])+float(gap)
    MTM[y][0]=str(Wert)
    y+=1

#Rest befüllen
c=1
for item in range(length1):
    r=1
    for i in range(length2):
        Match = 1
        upper=float(MTM[r-1][c])+ float(gap)
        left=float(MTM[r][c-1]) + float(gap)
        if Sequence1[c-1] == Sequence2[r-1]:
            upperleft=float(MTM[r-1][c-1]) + float(match)
        else:
            upperleft = float(MTM[r - 1][c - 1]) + float(mismatch)
            Match = 0
        m=max(upper, left, upperleft)
        MTM[r][c]=str(m)
        r+=1
    c+=1

# Rekursion
Rekursion = []
R=length2
C=length1

while R!=0 or C!=0:
    Start = float(MTM[R][C])
    gap1 = float(MTM[R-1][C])
    gap2 = float(MTM[R][C-1])
    mmatch = float(MTM[R-1][C-1])
    if Start == mmatch + match:
        Rekursion.extend('*')
        R = R - 1
        C = C - 1
        continue
    if Start == mmatch + mismatch:
        Rekursion.extend('/')
        R = R - 1
        C = C - 1
        continue
    if Start == gap1 + gap:
        Rekursion.extend('-')
        R = R -1
        continue
    if Start == gap2 + gap:
        Rekursion.extend('+')
        C = C-1
        continue

if R == 0:
    for i in range(C):
        Rekursion.extend('+')

if C == 0:
    for i in range(R):
        Rekursion.extend('-')

Rekursion.reverse()


#Print Alignment
print('CLUSTAL')
print('')
print('')
LineName=''
for letter in SequenceID1:
    LineName=LineName+' '
x=0
y=0
z=0
AlignedSeq1 = ''
AlignedSeq2 = ''
MatchLine=''
for item in Rekursion:
    if item == '*' or item == '/':
        AlignedSeq1 = AlignedSeq1 + Sequence1[x]
        AlignedSeq2 = AlignedSeq2 + Sequence2[y]
        x+=1
        y+=1
    if item == '-':
        AlignedSeq1 = AlignedSeq1 + '-'
        AlignedSeq2 = AlignedSeq2 + Sequence2[y]
        y+=1
    if item == '+':
        AlignedSeq1 = AlignedSeq1 + Sequence1[x]
        AlignedSeq2 = AlignedSeq2 + '-'
        x+=1
    if AlignedSeq1[z] == AlignedSeq2[z]:
        MatchLine = MatchLine + '*'
    else:
        MatchLine = MatchLine + ' '
    z+=1
    if len(AlignedSeq1) > 60:
        print(SequenceID1, '          ', AlignedSeq1)
        print(SequenceID2, '          ', AlignedSeq2)
        print(LineName, '          ', MatchLine)
        print('')
        print('')
        AlignedSeq1=''
        AlignedSeq2=''
        MatchLine=''
        z=0

if len(AlignedSeq1) > 0:
    print(SequenceID1, '          ', AlignedSeq1)
    print(SequenceID2, '          ', AlignedSeq2)
    print(LineName, '          ', MatchLine)



#print score to stderr
Score = float(MTM[r-1][c-1])
Score = int(Score)
stderr.write(str(Score)+"\n")