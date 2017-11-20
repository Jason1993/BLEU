# -*- coding: utf-8 -*-
from __future__ import division
import os
import sys
import string
from math import exp,log
from os.path import isdir,isfile
def getNGramVal(canSentence,refSentence):
    result = {}
    nGramVal = {}
    candidateWord = canSentence.split(" ")
    clength = len(candidateWord)
    bestmatch = clength
    bestmatchL = 0
    if clength < 4:
        limit = clength
    else:
        limit = 5
    n = 1
    while (n < limit):
        candidateGram = {}
        for pointer in range(len(candidateWord)-n+1):
            tempGram = ""
            for x in range(n):
                tempGram = tempGram + candidateWord[pointer+x]
            if (tempGram not in candidateGram):
                candidateGram[tempGram] = 1
            else:
                candidateGram[tempGram] += 1

        maxRefCount = {}
        for curRef in refSentence:
            curRefCount = {}
            refWord = curRef.split(" ")
            refLength = len(refWord)
            if abs(clength-refLength)<bestmatch:
                bestmatch = abs(clength-refLength)
                bestmatchL = refLength
            for pointer in range(len(refWord)-n+1):
                refGram = ""
                for x in range(n):
                    refGram = refGram + refWord[pointer+x]
                if (refGram not in curRefCount):
                    curRefCount[refGram] = 1
                else:
                    curRefCount[refGram] += 1

            for temp in curRefCount:
                if (temp not in maxRefCount):
                    maxRefCount[temp] = curRefCount[temp]
                else:
                    maxRefCount[temp] = max(maxRefCount[temp],curRefCount[temp])

        finalCount = 0
        for tempWord in candidateGram:
            if (tempWord in maxRefCount):
                finalCount = finalCount + min(candidateGram[tempWord],maxRefCount[tempWord])


        res = finalCount/(len(candidateWord)-n+1)
        result[n] = finalCount
        result[n+4] = len(candidateWord)-n+1
        n += 1
    result["c"] = clength
    result["r"] = bestmatchL
    return result


canFile = []
canPath = sys.argv[1]
candidate = open(canPath,'r')
for line in candidate:
    line = line.strip()
    line = line.decode('utf-8').lower()
    canFile.append(line)

refTemp = {}
refpath = sys.argv[2]
if (isfile(refpath) == False):
    for refFile in os.listdir(refpath):
        tempFile = open(os.path.join(refpath,refFile),'r')
        curFile = []
        for line in tempFile:
            line = line.strip()
            line = line.decode('utf-8').lower()
            curFile.append(line)
        refTemp[refFile] = curFile
    refFinal = {}
    for i in range(len(canFile)):
        refFinal[i] = []
        for tempfile in refTemp:
            refFinal[i].append(refTemp[tempfile][i])
else:
    refFile = open(refpath,'r')
    refOne = []
    refFinal = {}
    for line in refFile:
        line = line.strip()
        line = line.decode('utf-8').lower()
        refOne.append(line)
    for i in range(len(refOne)):
        refFinal[i] = []
        refFinal[i].append(refOne[i])
N1 = N2 = N3 = N4 = CL = RL = n1 = n2 =n3 =n4= 0
for i in range(len(canFile)):
    tempres = {}
    tempres = getNGramVal(canFile[i],refFinal[i])
    if (1 in tempres):
        N1 += tempres[1]
    if (2 in tempres):
        N2 += tempres[2]
    if (3 in tempres):
        N3 += tempres[3]
    if (4 in tempres):
        N4 += tempres[4]
    if (5 in tempres):
        n1 += tempres[5]
    if (6 in tempres):
        n2 += tempres[6]
    if (7 in tempres):
        n3 += tempres[7]
    if (8 in tempres):
        n4 += tempres[8]
    CL += tempres["c"]
    RL += tempres["r"]

BP = 1
if (CL>RL):
    BP = 1
else:
    BP = exp(1-RL/CL)


sumN = 0

sumN += 1/4*log(N1/n1)
sumN += 1/4*log(N2/n2)
sumN += 1/4*log(N3/n3)
sumN += 1/4*log(N4/n4)

print BP*exp(sumN)

#output = open("bleu_out.txt","w")
#output.write(res)