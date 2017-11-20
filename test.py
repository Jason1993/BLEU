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
        print (str(n)+" Gram: "+str(res))
        n += 1
    result["c"] = clength
    result["r"] = bestmatchL
    return result

canS = "wiederaufnahme der sitzung"
refS = []
refS.append("wiederaufnahme der sitzungsperiode")
res = {}
res = getNGramVal(canS,refS)
print res