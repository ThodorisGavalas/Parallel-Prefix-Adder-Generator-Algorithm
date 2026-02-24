def checkValidOverlap(seq,n):
    bitspan = list(range(n))
    for i in range(len(seq)):
        overlap = seq[i][1]
        if bitspan[seq[i][0]]-1+overlap >= seq[i][0]:
            return 0
        if bitspan[seq[i][0]] <= bitspan[bitspan[seq[i][0]]-1+overlap]:
            return 0
        if i > 0 :
            if seq[i][0] > seq[i-1][0] and bitspan[seq[i][0]] -1 + overlap != seq[i-1][0]:
                return 0
        bitspan[seq[i][0]] = bitspan[bitspan[seq[i][0]]-1+overlap]
    return 1 if all(b == 0 for b in bitspan) else 2

def DetermineLevels(seq,n):
    bitspan=list(range(n))
    levels = [0 for i in range(n)]
    for i in range(len(seq)):
        overlap = seq[i][1]
        levels[seq[i][0]] = max(levels[seq[i][0]],levels[bitspan[seq[i][0]]-1+overlap]) +1
        bitspan[seq[i][0]] = bitspan[bitspan[seq[i][0]]-1+overlap]
    return max(levels)

def DetermineLevels8(seq,n):
    bitspan=list(range(n))
    levels = [0 for i in range(n)]
    for i in range(len(seq)):
        overlap = seq[i][1]
        levels[seq[i][0]] = max(levels[seq[i][0]],levels[bitspan[seq[i][0]]-1+overlap]) +1
        bitspan[seq[i][0]] = bitspan[bitspan[seq[i][0]]-1+overlap]
        if levels[7] >= 4:
                return 10
    return max(levels)

def DetermineLevels16(seq,n):
    bitspan=list(range(n))
    levels = [0 for i in range(n)]
    for i in range(len(seq)):
        overlap = seq[i][1]
        levels[seq[i][0]] = max(levels[seq[i][0]],levels[bitspan[seq[i][0]]-1+overlap]) +1
        bitspan[seq[i][0]] = bitspan[bitspan[seq[i][0]]-1+overlap]
        if levels[15] >= 5:
                return 10
    return max(levels)

def DetermineLevels32(seq,n):
    bitspan=list(range(n))
    levels = [0 for i in range(n)]
    for i in range(len(seq)):
        overlap = seq[i][1]
        levels[seq[i][0]] = max(levels[seq[i][0]],levels[bitspan[seq[i][0]]-1+overlap]) +1
        bitspan[seq[i][0]] = bitspan[bitspan[seq[i][0]]-1+overlap]
        if levels[31] >= 6:
                return 10
    return max(levels)

def CalculateFanOuts(seq,n):
    bitspan=list(range(n))
    FanOuts = [[1] for i in range(n)]
    for i in range(len(seq)):
        overlap = seq[i][1]
        FanOuts[seq[i][0]].append(1)
        FanOuts[bitspan[seq[i][0]]-1+overlap][-1] = FanOuts[bitspan[seq[i][0]]-1+overlap][-1] +1
        bitspan[seq[i][0]] = bitspan[bitspan[seq[i][0]]-1+overlap]
    MaxFanOut = max(max(Position) for Position in FanOuts)
    return MaxFanOut

N = int(input("Number of bits: "))
maxOverlap = int(input(f"Maximum number of overlapping bits (up to {N-2}): "))

G = [[] for i in range(N+1)]
G[2] = [[[1,0]]]


N_lists = [[] for i in range(N+1)]
for i in range(3, N+1):
    N_lists[i] = G[i-1].copy()
    for currentGraph in N_lists[i]:
        for position in range(len(currentGraph) + 1):
            for overlap in range(min(i-2,maxOverlap)+1):
                newGraph = currentGraph.copy()
                newGraph.insert(position, [i-1,overlap])
                validness = checkValidOverlap(newGraph, i)
                if validness == 1:
                    if newGraph not in G[i]:
                        if i <= 4:
                            if DetermineLevels(newGraph,i) <= 2 and len(newGraph) <= 4: #4
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 5:
                            if DetermineLevels(newGraph,i) <= 3 and len(newGraph) <= 5: #5
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 6:
                            if DetermineLevels(newGraph,i) <= 4 and len(newGraph) <= 7: #7
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 7:
                            if DetermineLevels(newGraph,i) <= 5 and len(newGraph) <= 8: #9
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 8:
                            if DetermineLevels8(newGraph,i) <= 5 and len(newGraph) <= 11: #12
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 9:
                            if DetermineLevels(newGraph,i) <= 5 and len(newGraph) <= 12: #13
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 10:
                            if DetermineLevels(newGraph,i) <= 5 and len(newGraph) <= 14: #15
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 11:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 15: #17
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 12:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 18: #20
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 13:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 19: #22
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 14:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 21: #25
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 15:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 22: #28
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 16:
                            if DetermineLevels16(newGraph,i) <= 6 and len(newGraph) <= 26: #32
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 17:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 27: #33
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 18:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 29: #35
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 19:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 30: #37
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 20:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 33: #40
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 21:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 34: #42
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 22:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 36: #45
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 23:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 38: #48
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 24:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 42: #52
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 25:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 43: #54
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 26:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 45: #57
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 27:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 47: #60
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 28:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 51: #64
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 29:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 52: #67
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 30:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 54: #71
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 31:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 56: #75
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 32:
                            if DetermineLevels32(newGraph,i) <= 6 and len(newGraph) <= 61: #80
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 33:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 62: #81
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 34:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 64: #83
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 35:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 66: #85
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 36:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 69: #88
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 37:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 71: #90
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 38:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 74: #93
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 39:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 76: #96
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 40:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 80: #100
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 41:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 82: #102
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 42:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 85: #105
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 43:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 87: #108
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 44:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 91: #112
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 45:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 93: #115
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 46:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 96: #119
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 47:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 99: #123
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 48:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 104: #128
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 49:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 106: #130
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 50:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 109: #133
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 51:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 112: #136
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 52:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 116: #140
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 53:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 119: #143
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 54:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 123: #147
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 55:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 126: #151
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 56:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 131: #156
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 57:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 134: #159
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 58:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 138: #163
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 59:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 142: #167
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 60:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 147: #172
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 61:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 151: #176
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 62:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 156: #181
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 63:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 161: #186
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 64:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) <= 167: #192
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                elif validness == 2:
                    if newGraph not in N_lists[i]:
                        if i <= 4:
                            if DetermineLevels(newGraph,i) <= 2 and len(newGraph) < 4: #4
                                N_lists[i].append(newGraph)
                        elif i == 5:
                            if DetermineLevels(newGraph,i) <= 3 and len(newGraph) < 5: #5
                                N_lists[i].append(newGraph)
                        elif i == 6:
                            if DetermineLevels(newGraph,i) <= 4 and len(newGraph) < 7: #7
                                N_lists[i].append(newGraph)
                        elif i == 7:
                            if DetermineLevels(newGraph,i) <= 5 and len(newGraph) < 8: #9
                                N_lists[i].append(newGraph)
                        elif i == 8:
                            if DetermineLevels8(newGraph,i) <= 5 and len(newGraph) < 11: #12
                                N_lists[i].append(newGraph)
                        elif i == 9:
                            if DetermineLevels(newGraph,i) <= 5 and len(newGraph) < 12: #13
                                N_lists[i].append(newGraph)
                        elif i == 10:
                            if DetermineLevels(newGraph,i) <= 5 and len(newGraph) < 14: #15
                                N_lists[i].append(newGraph)
                        elif i == 11:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 15: #17
                                N_lists[i].append(newGraph)
                        elif i == 12:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 18: #20
                                N_lists[i].append(newGraph)
                        elif i == 13:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 19: #22
                                N_lists[i].append(newGraph)
                        elif i == 14:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 21: #25
                                N_lists[i].append(newGraph)
                        elif i == 15:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 22: #28
                                N_lists[i].append(newGraph)
                        elif i == 16:
                            if DetermineLevels16(newGraph,i) <= 6 and len(newGraph) < 26: #32
                                N_lists[i].append(newGraph)
                        elif i == 17:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 27: #33
                                N_lists[i].append(newGraph)
                        elif i == 18:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 29: #35
                                N_lists[i].append(newGraph)
                        elif i == 19:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 30: #37
                                N_lists[i].append(newGraph)
                        elif i == 20:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 33: #40
                                N_lists[i].append(newGraph)
                        elif i == 21:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 34: #42
                                N_lists[i].append(newGraph)
                        elif i == 22:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 36: #45
                                N_lists[i].append(newGraph)
                        elif i == 23:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 38: #48
                                N_lists[i].append(newGraph)
                        elif i == 24:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 42: #52
                                N_lists[i].append(newGraph)
                        elif i == 25:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 43: #54
                                N_lists[i].append(newGraph)
                        elif i == 26:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 45: #57
                                N_lists[i].append(newGraph)
                        elif i == 27:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 47: #60
                                N_lists[i].append(newGraph)
                        elif i == 28:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 51: #64
                                N_lists[i].append(newGraph)
                        elif i == 29:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 52: #67
                                N_lists[i].append(newGraph)
                        elif i == 30:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 54: #71
                                N_lists[i].append(newGraph)
                        elif i == 31:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 56: #75
                                N_lists[i].append(newGraph)
                        elif i == 32:
                            if DetermineLevels32(newGraph,i) <= 6 and len(newGraph) < 61: #80
                                N_lists[i].append(newGraph)
                        elif i == 33:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 62: #81
                                N_lists[i].append(newGraph)
                        elif i == 34:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 64: #83
                                N_lists[i].append(newGraph)
                        elif i == 35:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 66: #85
                                N_lists[i].append(newGraph)
                        elif i == 36:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 69: #88
                                N_lists[i].append(newGraph)
                        elif i == 37:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 71: #90
                                N_lists[i].append(newGraph)
                        elif i == 38:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 74: #93
                                N_lists[i].append(newGraph)
                        elif i == 39:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 76: #96
                                N_lists[i].append(newGraph)
                        elif i == 40:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 80: #100
                                N_lists[i].append(newGraph)
                        elif i == 41:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 82: #102
                                N_lists[i].append(newGraph)
                        elif i == 42:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 85: #105
                                N_lists[i].append(newGraph)
                        elif i == 43:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 87: #108
                                N_lists[i].append(newGraph)
                        elif i == 44:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 91: #112
                                N_lists[i].append(newGraph)
                        elif i == 45:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 93: #115
                                N_lists[i].append(newGraph)
                        elif i == 46:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 96: #119
                                N_lists[i].append(newGraph)
                        elif i == 47:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 99: #123
                                N_lists[i].append(newGraph)
                        elif i == 48:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 104: #128
                                N_lists[i].append(newGraph)
                        elif i == 49:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 106: #130
                                N_lists[i].append(newGraph)
                        elif i == 50:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 109: #133
                                N_lists[i].append(newGraph)
                        elif i == 51:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 112: #136
                                N_lists[i].append(newGraph)
                        elif i == 52:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 116: #140
                                N_lists[i].append(newGraph)
                        elif i == 53:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 119: #143
                                N_lists[i].append(newGraph)
                        elif i == 54:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 123: #147
                                N_lists[i].append(newGraph)
                        elif i == 55:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 126: #151
                                N_lists[i].append(newGraph)
                        elif i == 56:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 131: #156
                                N_lists[i].append(newGraph)
                        elif i == 57:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 134: #159
                                N_lists[i].append(newGraph)
                        elif i == 58:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 138: #163
                                N_lists[i].append(newGraph)
                        elif i == 59:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 142: #167
                                N_lists[i].append(newGraph)
                        elif i == 60:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 147: #172
                                N_lists[i].append(newGraph)
                        elif i == 61:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 151: #176
                                N_lists[i].append(newGraph)
                        elif i == 62:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 156: #181
                                N_lists[i].append(newGraph)
                        elif i == 63:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 161: #186
                                N_lists[i].append(newGraph)
                        elif i == 64:
                            if DetermineLevels(newGraph,i) <= 6 and len(newGraph) < 167: #192
                                N_lists[i].append(newGraph)


print(f"All Prefix Graphs for {N} bits with maximum overlap of {maxOverlap} bits:")
for PrefixGraph in G[N]:
    print(PrefixGraph,f", {len(PrefixGraph)} Nodes",f", {DetermineLevels(PrefixGraph,N)} Levels",f", Maximum Fan-Out:{CalculateFanOuts(PrefixGraph,N)}")
for i in range(3,N+1):
    print(f"Total number of Prefix Graphs of {i} bits with maximum overlap of {maxOverlap} bits: {len(G[i])}")

# Find Prefix Graphs with the least levels
LeastLevels = min(DetermineLevels(PrefixGraph, N) for PrefixGraph in G[N])
FastestGraphs = [PrefixGraph for PrefixGraph in G[N] if DetermineLevels(PrefixGraph, N) == LeastLevels]

# Among those, find the ones with the least nodes
LeastNodes = min(len(PrefixGraph) for PrefixGraph in FastestGraphs)
OptimalGraphs = [PrefixGraph for PrefixGraph in FastestGraphs if len(PrefixGraph) == LeastNodes]

print(f"\nOptimal Prefix Graphs (least levels, then least nodes):")
for PrefixGraph in OptimalGraphs:
    print(PrefixGraph,f", {len(PrefixGraph)} Nodes",f", {DetermineLevels(PrefixGraph, N)} Levels",f", Maximum Fan-Out:{CalculateFanOuts(PrefixGraph,N)}")
print(f"Number of optimal graphs: {len(OptimalGraphs)}")
print(f"Least levels: {LeastLevels}")
print(f"Least nodes among graphs with least levels: {LeastNodes}")

overlappingPGs=[]
for PG in G[N]:
    for i in range(len(PG)):
        if PG[i][1] != 0:
            overlappingPGs.append(PG)
            break

def OverlapofPG(seq):
    return max(node[1] for node in seq)

if len(overlappingPGs) == 0:
    print("\nNo Overlapping Prefix Graphs")
else:
    print(f"\nAll Overlapping Prefix Graphs for {N} bits with maximum overlap of {maxOverlap} bits:")
    for PrefixGraph in overlappingPGs:
        print(PrefixGraph,f", {len(PrefixGraph)} Nodes",f", {DetermineLevels(PrefixGraph,N)} Levels",f", Maximum Fan-Out:{CalculateFanOuts(PrefixGraph,N)}, Overlap:{OverlapofPG(PrefixGraph)}")
    print(f"\nTotal number of Overlapping Prefix Graphs of {N} bits with maximum overlap of {maxOverlap} bits: {len(overlappingPGs)}")

    # Find Overlapping Prefix Graphs with the least levels
    LeastLevels = min(DetermineLevels(PrefixGraph, N) for PrefixGraph in overlappingPGs)
    FastestGraphs = [PrefixGraph for PrefixGraph in overlappingPGs if DetermineLevels(PrefixGraph, N) == LeastLevels]

    # Among those, find the ones with the least nodes
    LeastNodes = min(len(PrefixGraph) for PrefixGraph in FastestGraphs)
    OptimalGraphs = [PrefixGraph for PrefixGraph in FastestGraphs if len(PrefixGraph) == LeastNodes]

    print(f"\nOptimal Overlapping Prefix Graphs (least levels, then least nodes):")
    for PrefixGraph in OptimalGraphs:
        print(PrefixGraph,f", {len(PrefixGraph)} Nodes",f", {DetermineLevels(PrefixGraph, N)} Levels",f", Maximum Fan-Out:{CalculateFanOuts(PrefixGraph,N)}, Overlap:{OverlapofPG(PrefixGraph)}")
    print(f"Number of optimal overlapping graphs: {len(OptimalGraphs)}")
    print(f"Least levels: {LeastLevels}")
    print(f"Least nodes among graphs with least levels: {LeastNodes}")
    MinimumOverlap = min(OverlapofPG(PG) for PG in OptimalGraphs)
    MaximumOverlap = max(OverlapofPG(PG) for PG in OptimalGraphs)
    print(f"Minimum Overlap: {MinimumOverlap} , Maximum Overlap: {MaximumOverlap} (among optimal Overlapping Prefix Graphs)")

#Program Output:
#Total number of Prefix Graphs of 3 bits with maximum overlap of 1 bits: 3
#Total number of Prefix Graphs of 4 bits with maximum overlap of 1 bits: 1
#Total number of Prefix Graphs of 5 bits with maximum overlap of 1 bits: 1
#Total number of Prefix Graphs of 6 bits with maximum overlap of 1 bits: 3
#Total number of Prefix Graphs of 7 bits with maximum overlap of 1 bits: 5
#Total number of Prefix Graphs of 8 bits with maximum overlap of 1 bits: 2
#Total number of Prefix Graphs of 9 bits with maximum overlap of 1 bits: 2
#Total number of Prefix Graphs of 10 bits with maximum overlap of 1 bits: 6
#Total number of Prefix Graphs of 11 bits with maximum overlap of 1 bits: 10
#Total number of Prefix Graphs of 12 bits with maximum overlap of 1 bits: 74
#Total number of Prefix Graphs of 13 bits with maximum overlap of 1 bits: 136
#Total number of Prefix Graphs of 14 bits with maximum overlap of 1 bits: 368
#Total number of Prefix Graphs of 15 bits with maximum overlap of 1 bits: 114
#Total number of Prefix Graphs of 16 bits with maximum overlap of 1 bits: 4
#Total number of Prefix Graphs of 17 bits with maximum overlap of 1 bits: 4
#Total number of Prefix Graphs of 18 bits with maximum overlap of 1 bits: 12
#Total number of Prefix Graphs of 19 bits with maximum overlap of 1 bits: 8
#Total number of Prefix Graphs of 20 bits with maximum overlap of 1 bits: 40
#Total number of Prefix Graphs of 21 bits with maximum overlap of 1 bits: 16
#Total number of Prefix Graphs of 22 bits with maximum overlap of 1 bits: 16
#Total number of Prefix Graphs of 23 bits with maximum overlap of 1 bits: 16
#Total number of Prefix Graphs of 24 bits with maximum overlap of 1 bits: 288
#Total number of Prefix Graphs of 25 bits with maximum overlap of 1 bits: 192
#Total number of Prefix Graphs of 26 bits with maximum overlap of 1 bits: 216
#Total number of Prefix Graphs of 27 bits with maximum overlap of 1 bits: 192
#Total number of Prefix Graphs of 28 bits with maximum overlap of 1 bits: 4624
#Total number of Prefix Graphs of 29 bits with maximum overlap of 1 bits: 3072
#Total number of Prefix Graphs of 30 bits with maximum overlap of 1 bits: 3232
#Total number of Prefix Graphs of 31 bits with maximum overlap of 1 bits: 1312
#Total number of Prefix Graphs of 32 bits with maximum overlap of 1 bits: 4
#Total number of Prefix Graphs of 33 bits with maximum overlap of 1 bits: 4
#Total number of Prefix Graphs of 34 bits with maximum overlap of 1 bits: 4
#Total number of Prefix Graphs of 35 bits with maximum overlap of 1 bits: 4
#Total number of Prefix Graphs of 36 bits with maximum overlap of 1 bits: 32
#Total number of Prefix Graphs of 37 bits with maximum overlap of 1 bits: 72
#Total number of Prefix Graphs of 38 bits with maximum overlap of 1 bits: 300
#Total number of Prefix Graphs of 39 bits with maximum overlap of 1 bits: 276
#Total number of Prefix Graphs of 40 bits with maximum overlap of 1 bits: 2112
#Total number of Prefix Graphs of 41 bits with maximum overlap of 1 bits: 2024
#Total number of Prefix Graphs of 42 bits with maximum overlap of 1 bits: 3592
#Total number of Prefix Graphs of 43 bits with maximum overlap of 1 bits: 464
#Total number of Prefix Graphs of 44 bits with maximum overlap of 1 bits: 2496
#Total number of Prefix Graphs of 45 bits with maximum overlap of 1 bits: 504
#Total number of Prefix Graphs of 46 bits with maximum overlap of 1 bits: 432
#Total number of Prefix Graphs of 47 bits with maximum overlap of 1 bits: 288
#Total number of Prefix Graphs of 48 bits with maximum overlap of 1 bits: 2096
#Total number of Prefix Graphs of 49 bits with maximum overlap of 1 bits: 800
#Total number of Prefix Graphs of 50 bits with maximum overlap of 1 bits: 272
#Total number of Prefix Graphs of 51 bits with maximum overlap of 1 bits: 8
#Total number of Prefix Graphs of 52 bits with maximum overlap of 1 bits: 56
#Total number of Prefix Graphs of 53 bits with maximum overlap of 1 bits: 72
#Total number of Prefix Graphs of 54 bits with maximum overlap of 1 bits: 152
#Total number of Prefix Graphs of 55 bits with maximum overlap of 1 bits: 56
#Total number of Prefix Graphs of 56 bits with maximum overlap of 1 bits: 272
#Total number of Prefix Graphs of 57 bits with maximum overlap of 1 bits: 56
#Total number of Prefix Graphs of 58 bits with maximum overlap of 1 bits: 40
#Total number of Prefix Graphs of 59 bits with maximum overlap of 1 bits: 8
#Total number of Prefix Graphs of 60 bits with maximum overlap of 1 bits: 24
#Total number of Prefix Graphs of 61 bits with maximum overlap of 1 bits: 16
#Total number of Prefix Graphs of 62 bits with maximum overlap of 1 bits: 16
#Total number of Prefix Graphs of 63 bits with maximum overlap of 1 bits: 8
#Total number of Prefix Graphs of 64 bits with maximum overlap of 1 bits: 8

#Optimal Prefix Graphs (least levels, then least nodes):
#[[63, 0], [61, 0], [63, 0], [62, 0], [59, 0], [57, 0], [59, 0], [63, 0], [62, 0], [61, 0], [60, 0], [58, 0], [55, 0], [53, 0], [55, 0], [51, 0], [49, 0], [51, 0], [55, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [53, 0], [54, 0], [52, 0], [50, 0], [47, 0], [45, 0], [47, 0], [46, 0], [43, 0], [41, 0], [43, 0], [47, 0], [39, 0], [37, 0], [39, 0], [35, 0], [33, 0], [35, 0], [39, 0], [47, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [43, 0], [46, 0], [45, 0], [44, 0], [41, 0], [42, 0], [40, 0], [37, 0], [38, 0], [36, 0], [34, 0], [31, 0], [29, 0], [31, 0], [30, 0], [27, 0], [25, 0], [27, 0], [31, 0], [26, 0], [23, 0], [21, 0], [23, 0], [22, 0], [19, 0], [17, 0], [19, 0], [23, 0], [31, 0], [27, 0], [15, 0], [13, 0], [15, 0], [11, 0], [9, 0], [11, 0], [15, 0], [7, 0], [5, 0], [7, 0], [3, 0], [1, 0], [3, 0], [7, 0], [15, 0], [31, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [47, 0], [46, 0], [45, 0], [44, 0], [43, 0], [42, 0], [41, 0], [40, 0], [39, 0], [38, 0], [37, 0], [36, 0], [35, 0], [34, 0], [33, 0], [32, 0], [27, 0], [30, 0], [29, 0], [28, 0], [23, 0], [26, 0], [25, 0], [24, 0], [19, 0], [22, 0], [21, 0], [20, 0], [17, 0], [18, 0], [16, 0], [11, 0], [13, 0], [14, 0], [12, 0], [9, 0], [10, 0], [8, 0], [5, 0], [6, 0], [4, 0], [2, 0]] , 167 Nodes , 6 Levels , Maximum Fan-Out:33
#[[63, 0], [61, 0], [63, 0], [62, 0], [59, 0], [57, 0], [59, 0], [63, 0], [62, 0], [61, 0], [60, 0], [58, 0], [55, 0], [53, 0], [55, 0], [51, 0], [49, 0], [51, 0], [55, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [53, 0], [54, 0], [52, 0], [50, 0], [47, 0], [45, 0], [47, 0], [46, 0], [43, 0], [41, 0], [43, 0], [47, 0], [39, 0], [37, 0], [39, 0], [35, 0], [33, 0], [35, 0], [39, 0], [47, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [43, 0], [46, 0], [45, 0], [44, 0], [41, 0], [42, 0], [40, 0], [36, 0], [37, 1], [38, 0], [34, 0], [31, 0], [29, 0], [31, 0], [30, 0], [27, 0], [25, 0], [27, 0], [31, 0], [26, 0], [23, 0], [21, 0], [23, 0], [22, 0], [19, 0], [17, 0], [19, 0], [23, 0], [31, 0], [27, 0], [15, 0], [13, 0], [15, 0], [11, 0], [9, 0], [11, 0], [15, 0], [7, 0], [5, 0], [7, 0], [3, 0], [1, 0], [3, 0], [7, 0], [15, 0], [31, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [47, 0], [46, 0], [45, 0], [44, 0], [43, 0], [42, 0], [41, 0], [40, 0], [39, 0], [38, 0], [37, 0], [36, 0], [35, 0], [34, 0], [33, 0], [32, 0], [27, 0], [30, 0], [29, 0], [28, 0], [23, 0], [26, 0], [25, 0], [24, 0], [19, 0], [22, 0], [21, 0], [20, 0], [17, 0], [18, 0], [16, 0], [11, 0], [13, 0], [14, 0], [12, 0], [9, 0], [10, 0], [8, 0], [5, 0], [6, 0], [4, 0], [2, 0]] , 167 Nodes , 6 Levels , Maximum Fan-Out:33
#[[63, 0], [61, 0], [63, 0], [62, 0], [59, 0], [57, 0], [59, 0], [63, 0], [62, 0], [61, 0], [60, 0], [58, 0], [55, 0], [53, 0], [55, 0], [51, 0], [49, 0], [51, 0], [55, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [53, 0], [54, 0], [52, 0], [50, 0], [47, 0], [45, 0], [47, 0], [46, 0], [43, 0], [41, 0], [43, 0], [47, 0], [39, 0], [37, 0], [39, 0], [35, 0], [33, 0], [35, 0], [39, 0], [47, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [43, 0], [46, 0], [45, 0], [44, 0], [41, 0], [42, 0], [40, 0], [37, 0], [38, 0], [36, 0], [34, 0], [31, 0], [29, 0], [31, 0], [30, 0], [27, 0], [25, 0], [27, 0], [31, 0], [26, 0], [23, 0], [21, 0], [23, 0], [22, 0], [19, 0], [17, 0], [19, 0], [23, 0], [31, 0], [27, 0], [15, 0], [13, 0], [15, 0], [11, 0], [9, 0], [11, 0], [15, 0], [7, 0], [5, 0], [7, 0], [3, 0], [1, 0], [3, 0], [7, 0], [15, 0], [31, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [47, 0], [46, 0], [45, 0], [44, 0], [43, 0], [42, 0], [41, 0], [40, 0], [39, 0], [38, 0], [37, 0], [36, 0], [35, 0], [34, 0], [33, 0], [32, 0], [27, 0], [30, 0], [29, 0], [28, 0], [23, 0], [26, 0], [25, 0], [24, 0], [19, 0], [22, 0], [21, 0], [20, 0], [17, 0], [18, 0], [16, 0], [11, 0], [13, 0], [14, 0], [12, 0], [8, 0], [9, 1], [10, 0], [5, 0], [6, 0], [4, 0], [2, 0]] , 167 Nodes , 6 Levels , Maximum Fan-Out:33
#[[63, 0], [61, 0], [63, 0], [62, 0], [59, 0], [57, 0], [59, 0], [63, 0], [62, 0], [61, 0], [60, 0], [58, 0], [55, 0], [53, 0], [55, 0], [51, 0], [49, 0], [51, 0], [55, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [53, 0], [54, 0], [52, 0], [50, 0], [47, 0], [45, 0], [47, 0], [46, 0], [43, 0], [41, 0], [43, 0], [47, 0], [39, 0], [37, 0], [39, 0], [35, 0], [33, 0], [35, 0], [39, 0], [47, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [43, 0], [46, 0], [45, 0], [44, 0], [41, 0], [42, 0], [40, 0], [36, 0], [37, 1], [38, 0], [34, 0], [31, 0], [29, 0], [31, 0], [30, 0], [27, 0], [25, 0], [27, 0], [31, 0], [26, 0], [23, 0], [21, 0], [23, 0], [22, 0], [19, 0], [17, 0], [19, 0], [23, 0], [31, 0], [27, 0], [15, 0], [13, 0], [15, 0], [11, 0], [9, 0], [11, 0], [15, 0], [7, 0], [5, 0], [7, 0], [3, 0], [1, 0], [3, 0], [7, 0], [15, 0], [31, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [47, 0], [46, 0], [45, 0], [44, 0], [43, 0], [42, 0], [41, 0], [40, 0], [39, 0], [38, 0], [37, 0], [36, 0], [35, 0], [34, 0], [33, 0], [32, 0], [27, 0], [30, 0], [29, 0], [28, 0], [23, 0], [26, 0], [25, 0], [24, 0], [19, 0], [22, 0], [21, 0], [20, 0], [17, 0], [18, 0], [16, 0], [11, 0], [13, 0], [14, 0], [12, 0], [8, 0], [9, 1], [10, 0], [5, 0], [6, 0], [4, 0], [2, 0]] , 167 Nodes , 6 Levels , Maximum Fan-Out:33
#[[63, 0], [61, 0], [63, 0], [62, 0], [59, 0], [57, 0], [59, 0], [63, 0], [62, 0], [61, 0], [60, 0], [58, 0], [55, 0], [53, 0], [55, 0], [51, 0], [49, 0], [51, 0], [55, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [53, 0], [54, 0], [52, 0], [50, 0], [47, 0], [45, 0], [47, 0], [46, 0], [43, 0], [41, 0], [43, 0], [47, 0], [39, 0], [37, 0], [39, 0], [35, 0], [33, 0], [35, 0], [39, 0], [47, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [43, 0], [46, 0], [45, 0], [44, 0], [41, 0], [42, 0], [40, 0], [37, 0], [38, 0], [36, 0], [34, 0], [31, 0], [29, 0], [31, 0], [30, 0], [27, 0], [25, 0], [27, 0], [31, 0], [26, 0], [23, 0], [21, 0], [23, 0], [22, 0], [19, 0], [17, 0], [19, 0], [23, 0], [31, 0], [27, 0], [15, 0], [13, 0], [15, 0], [11, 0], [9, 0], [11, 0], [15, 0], [7, 0], [5, 0], [7, 0], [3, 0], [1, 0], [3, 0], [7, 0], [15, 0], [31, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [47, 0], [46, 0], [45, 0], [44, 0], [43, 0], [42, 0], [41, 0], [40, 0], [39, 0], [38, 0], [37, 0], [36, 0], [35, 0], [34, 0], [33, 0], [32, 0], [27, 0], [30, 0], [29, 0], [28, 0], [23, 0], [26, 0], [25, 0], [24, 0], [19, 0], [22, 0], [21, 0], [20, 0], [17, 0], [18, 0], [16, 0], [11, 0], [13, 0], [14, 0], [12, 0], [9, 0], [10, 0], [8, 0], [4, 0], [5, 1], [6, 0], [2, 0]] , 167 Nodes , 6 Levels , Maximum Fan-Out:33
#[[63, 0], [61, 0], [63, 0], [62, 0], [59, 0], [57, 0], [59, 0], [63, 0], [62, 0], [61, 0], [60, 0], [58, 0], [55, 0], [53, 0], [55, 0], [51, 0], [49, 0], [51, 0], [55, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [53, 0], [54, 0], [52, 0], [50, 0], [47, 0], [45, 0], [47, 0], [46, 0], [43, 0], [41, 0], [43, 0], [47, 0], [39, 0], [37, 0], [39, 0], [35, 0], [33, 0], [35, 0], [39, 0], [47, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [43, 0], [46, 0], [45, 0], [44, 0], [41, 0], [42, 0], [40, 0], [36, 0], [37, 1], [38, 0], [34, 0], [31, 0], [29, 0], [31, 0], [30, 0], [27, 0], [25, 0], [27, 0], [31, 0], [26, 0], [23, 0], [21, 0], [23, 0], [22, 0], [19, 0], [17, 0], [19, 0], [23, 0], [31, 0], [27, 0], [15, 0], [13, 0], [15, 0], [11, 0], [9, 0], [11, 0], [15, 0], [7, 0], [5, 0], [7, 0], [3, 0], [1, 0], [3, 0], [7, 0], [15, 0], [31, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [47, 0], [46, 0], [45, 0], [44, 0], [43, 0], [42, 0], [41, 0], [40, 0], [39, 0], [38, 0], [37, 0], [36, 0], [35, 0], [34, 0], [33, 0], [32, 0], [27, 0], [30, 0], [29, 0], [28, 0], [23, 0], [26, 0], [25, 0], [24, 0], [19, 0], [22, 0], [21, 0], [20, 0], [17, 0], [18, 0], [16, 0], [11, 0], [13, 0], [14, 0], [12, 0], [9, 0], [10, 0], [8, 0], [4, 0], [5, 1], [6, 0], [2, 0]] , 167 Nodes , 6 Levels , Maximum Fan-Out:33
#[[63, 0], [61, 0], [63, 0], [62, 0], [59, 0], [57, 0], [59, 0], [63, 0], [62, 0], [61, 0], [60, 0], [58, 0], [55, 0], [53, 0], [55, 0], [51, 0], [49, 0], [51, 0], [55, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [53, 0], [54, 0], [52, 0], [50, 0], [47, 0], [45, 0], [47, 0], [46, 0], [43, 0], [41, 0], [43, 0], [47, 0], [39, 0], [37, 0], [39, 0], [35, 0], [33, 0], [35, 0], [39, 0], [47, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [43, 0], [46, 0], [45, 0], [44, 0], [41, 0], [42, 0], [40, 0], [37, 0], [38, 0], [36, 0], [34, 0], [31, 0], [29, 0], [31, 0], [30, 0], [27, 0], [25, 0], [27, 0], [31, 0], [26, 0], [23, 0], [21, 0], [23, 0], [22, 0], [19, 0], [17, 0], [19, 0], [23, 0], [31, 0], [27, 0], [15, 0], [13, 0], [15, 0], [11, 0], [9, 0], [11, 0], [15, 0], [7, 0], [5, 0], [7, 0], [3, 0], [1, 0], [3, 0], [7, 0], [15, 0], [31, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [47, 0], [46, 0], [45, 0], [44, 0], [43, 0], [42, 0], [41, 0], [40, 0], [39, 0], [38, 0], [37, 0], [36, 0], [35, 0], [34, 0], [33, 0], [32, 0], [27, 0], [30, 0], [29, 0], [28, 0], [23, 0], [26, 0], [25, 0], [24, 0], [19, 0], [22, 0], [21, 0], [20, 0], [17, 0], [18, 0], [16, 0], [11, 0], [13, 0], [14, 0], [12, 0], [8, 0], [9, 1], [10, 0], [4, 0], [5, 1], [6, 0], [2, 0]] , 167 Nodes , 6 Levels , Maximum Fan-Out:33
#[[63, 0], [61, 0], [63, 0], [62, 0], [59, 0], [57, 0], [59, 0], [63, 0], [62, 0], [61, 0], [60, 0], [58, 0], [55, 0], [53, 0], [55, 0], [51, 0], [49, 0], [51, 0], [55, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [53, 0], [54, 0], [52, 0], [50, 0], [47, 0], [45, 0], [47, 0], [46, 0], [43, 0], [41, 0], [43, 0], [47, 0], [39, 0], [37, 0], [39, 0], [35, 0], [33, 0], [35, 0], [39, 0], [47, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [43, 0], [46, 0], [45, 0], [44, 0], [41, 0], [42, 0], [40, 0], [36, 0], [37, 1], [38, 0], [34, 0], [31, 0], [29, 0], [31, 0], [30, 0], [27, 0], [25, 0], [27, 0], [31, 0], [26, 0], [23, 0], [21, 0], [23, 0], [22, 0], [19, 0], [17, 0], [19, 0], [23, 0], [31, 0], [27, 0], [15, 0], [13, 0], [15, 0], [11, 0], [9, 0], [11, 0], [15, 0], [7, 0], [5, 0], [7, 0], [3, 0], [1, 0], [3, 0], [7, 0], [15, 0], [31, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [47, 0], [46, 0], [45, 0], [44, 0], [43, 0], [42, 0], [41, 0], [40, 0], [39, 0], [38, 0], [37, 0], [36, 0], [35, 0], [34, 0], [33, 0], [32, 0], [27, 0], [30, 0], [29, 0], [28, 0], [23, 0], [26, 0], [25, 0], [24, 0], [19, 0], [22, 0], [21, 0], [20, 0], [17, 0], [18, 0], [16, 0], [11, 0], [13, 0], [14, 0], [12, 0], [8, 0], [9, 1], [10, 0], [4, 0], [5, 1], [6, 0], [2, 0]] , 167 Nodes , 6 Levels , Maximum Fan-Out:33
#Number of optimal graphs: 8
#Least levels: 6
#Least nodes among graphs with least levels: 167

#Total number of Overlapping Prefix Graphs of 64 bits with maximum overlap of 1 bits: 7

#Optimal Overlapping Prefix Graphs (least levels, then least nodes):
#[[63, 0], [61, 0], [63, 0], [62, 0], [59, 0], [57, 0], [59, 0], [63, 0], [62, 0], [61, 0], [60, 0], [58, 0], [55, 0], [53, 0], [55, 0], [51, 0], [49, 0], [51, 0], [55, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [53, 0], [54, 0], [52, 0], [50, 0], [47, 0], [45, 0], [47, 0], [46, 0], [43, 0], [41, 0], [43, 0], [47, 0], [39, 0], [37, 0], [39, 0], [35, 0], [33, 0], [35, 0], [39, 0], [47, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [43, 0], [46, 0], [45, 0], [44, 0], [41, 0], [42, 0], [40, 0], [36, 0], [37, 1], [38, 0], [34, 0], [31, 0], [29, 0], [31, 0], [30, 0], [27, 0], [25, 0], [27, 0], [31, 0], [26, 0], [23, 0], [21, 0], [23, 0], [22, 0], [19, 0], [17, 0], [19, 0], [23, 0], [31, 0], [27, 0], [15, 0], [13, 0], [15, 0], [11, 0], [9, 0], [11, 0], [15, 0], [7, 0], [5, 0], [7, 0], [3, 0], [1, 0], [3, 0], [7, 0], [15, 0], [31, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [47, 0], [46, 0], [45, 0], [44, 0], [43, 0], [42, 0], [41, 0], [40, 0], [39, 0], [38, 0], [37, 0], [36, 0], [35, 0], [34, 0], [33, 0], [32, 0], [27, 0], [30, 0], [29, 0], [28, 0], [23, 0], [26, 0], [25, 0], [24, 0], [19, 0], [22, 0], [21, 0], [20, 0], [17, 0], [18, 0], [16, 0], [11, 0], [13, 0], [14, 0], [12, 0], [9, 0], [10, 0], [8, 0], [5, 0], [6, 0], [4, 0], [2, 0]] , 167 Nodes , 6 Levels , Maximum Fan-Out:33, Overlap:1
#[[63, 0], [61, 0], [63, 0], [62, 0], [59, 0], [57, 0], [59, 0], [63, 0], [62, 0], [61, 0], [60, 0], [58, 0], [55, 0], [53, 0], [55, 0], [51, 0], [49, 0], [51, 0], [55, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [53, 0], [54, 0], [52, 0], [50, 0], [47, 0], [45, 0], [47, 0], [46, 0], [43, 0], [41, 0], [43, 0], [47, 0], [39, 0], [37, 0], [39, 0], [35, 0], [33, 0], [35, 0], [39, 0], [47, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [43, 0], [46, 0], [45, 0], [44, 0], [41, 0], [42, 0], [40, 0], [37, 0], [38, 0], [36, 0], [34, 0], [31, 0], [29, 0], [31, 0], [30, 0], [27, 0], [25, 0], [27, 0], [31, 0], [26, 0], [23, 0], [21, 0], [23, 0], [22, 0], [19, 0], [17, 0], [19, 0], [23, 0], [31, 0], [27, 0], [15, 0], [13, 0], [15, 0], [11, 0], [9, 0], [11, 0], [15, 0], [7, 0], [5, 0], [7, 0], [3, 0], [1, 0], [3, 0], [7, 0], [15, 0], [31, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [47, 0], [46, 0], [45, 0], [44, 0], [43, 0], [42, 0], [41, 0], [40, 0], [39, 0], [38, 0], [37, 0], [36, 0], [35, 0], [34, 0], [33, 0], [32, 0], [27, 0], [30, 0], [29, 0], [28, 0], [23, 0], [26, 0], [25, 0], [24, 0], [19, 0], [22, 0], [21, 0], [20, 0], [17, 0], [18, 0], [16, 0], [11, 0], [13, 0], [14, 0], [12, 0], [8, 0], [9, 1], [10, 0], [5, 0], [6, 0], [4, 0], [2, 0]] , 167 Nodes , 6 Levels , Maximum Fan-Out:33, Overlap:1
#[[63, 0], [61, 0], [63, 0], [62, 0], [59, 0], [57, 0], [59, 0], [63, 0], [62, 0], [61, 0], [60, 0], [58, 0], [55, 0], [53, 0], [55, 0], [51, 0], [49, 0], [51, 0], [55, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [53, 0], [54, 0], [52, 0], [50, 0], [47, 0], [45, 0], [47, 0], [46, 0], [43, 0], [41, 0], [43, 0], [47, 0], [39, 0], [37, 0], [39, 0], [35, 0], [33, 0], [35, 0], [39, 0], [47, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [43, 0], [46, 0], [45, 0], [44, 0], [41, 0], [42, 0], [40, 0], [36, 0], [37, 1], [38, 0], [34, 0], [31, 0], [29, 0], [31, 0], [30, 0], [27, 0], [25, 0], [27, 0], [31, 0], [26, 0], [23, 0], [21, 0], [23, 0], [22, 0], [19, 0], [17, 0], [19, 0], [23, 0], [31, 0], [27, 0], [15, 0], [13, 0], [15, 0], [11, 0], [9, 0], [11, 0], [15, 0], [7, 0], [5, 0], [7, 0], [3, 0], [1, 0], [3, 0], [7, 0], [15, 0], [31, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [47, 0], [46, 0], [45, 0], [44, 0], [43, 0], [42, 0], [41, 0], [40, 0], [39, 0], [38, 0], [37, 0], [36, 0], [35, 0], [34, 0], [33, 0], [32, 0], [27, 0], [30, 0], [29, 0], [28, 0], [23, 0], [26, 0], [25, 0], [24, 0], [19, 0], [22, 0], [21, 0], [20, 0], [17, 0], [18, 0], [16, 0], [11, 0], [13, 0], [14, 0], [12, 0], [8, 0], [9, 1], [10, 0], [5, 0], [6, 0], [4, 0], [2, 0]] , 167 Nodes , 6 Levels , Maximum Fan-Out:33, Overlap:1
#[[63, 0], [61, 0], [63, 0], [62, 0], [59, 0], [57, 0], [59, 0], [63, 0], [62, 0], [61, 0], [60, 0], [58, 0], [55, 0], [53, 0], [55, 0], [51, 0], [49, 0], [51, 0], [55, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [53, 0], [54, 0], [52, 0], [50, 0], [47, 0], [45, 0], [47, 0], [46, 0], [43, 0], [41, 0], [43, 0], [47, 0], [39, 0], [37, 0], [39, 0], [35, 0], [33, 0], [35, 0], [39, 0], [47, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [43, 0], [46, 0], [45, 0], [44, 0], [41, 0], [42, 0], [40, 0], [37, 0], [38, 0], [36, 0], [34, 0], [31, 0], [29, 0], [31, 0], [30, 0], [27, 0], [25, 0], [27, 0], [31, 0], [26, 0], [23, 0], [21, 0], [23, 0], [22, 0], [19, 0], [17, 0], [19, 0], [23, 0], [31, 0], [27, 0], [15, 0], [13, 0], [15, 0], [11, 0], [9, 0], [11, 0], [15, 0], [7, 0], [5, 0], [7, 0], [3, 0], [1, 0], [3, 0], [7, 0], [15, 0], [31, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [47, 0], [46, 0], [45, 0], [44, 0], [43, 0], [42, 0], [41, 0], [40, 0], [39, 0], [38, 0], [37, 0], [36, 0], [35, 0], [34, 0], [33, 0], [32, 0], [27, 0], [30, 0], [29, 0], [28, 0], [23, 0], [26, 0], [25, 0], [24, 0], [19, 0], [22, 0], [21, 0], [20, 0], [17, 0], [18, 0], [16, 0], [11, 0], [13, 0], [14, 0], [12, 0], [9, 0], [10, 0], [8, 0], [4, 0], [5, 1], [6, 0], [2, 0]] , 167 Nodes , 6 Levels , Maximum Fan-Out:33, Overlap:1
#[[63, 0], [61, 0], [63, 0], [62, 0], [59, 0], [57, 0], [59, 0], [63, 0], [62, 0], [61, 0], [60, 0], [58, 0], [55, 0], [53, 0], [55, 0], [51, 0], [49, 0], [51, 0], [55, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [53, 0], [54, 0], [52, 0], [50, 0], [47, 0], [45, 0], [47, 0], [46, 0], [43, 0], [41, 0], [43, 0], [47, 0], [39, 0], [37, 0], [39, 0], [35, 0], [33, 0], [35, 0], [39, 0], [47, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [43, 0], [46, 0], [45, 0], [44, 0], [41, 0], [42, 0], [40, 0], [36, 0], [37, 1], [38, 0], [34, 0], [31, 0], [29, 0], [31, 0], [30, 0], [27, 0], [25, 0], [27, 0], [31, 0], [26, 0], [23, 0], [21, 0], [23, 0], [22, 0], [19, 0], [17, 0], [19, 0], [23, 0], [31, 0], [27, 0], [15, 0], [13, 0], [15, 0], [11, 0], [9, 0], [11, 0], [15, 0], [7, 0], [5, 0], [7, 0], [3, 0], [1, 0], [3, 0], [7, 0], [15, 0], [31, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [47, 0], [46, 0], [45, 0], [44, 0], [43, 0], [42, 0], [41, 0], [40, 0], [39, 0], [38, 0], [37, 0], [36, 0], [35, 0], [34, 0], [33, 0], [32, 0], [27, 0], [30, 0], [29, 0], [28, 0], [23, 0], [26, 0], [25, 0], [24, 0], [19, 0], [22, 0], [21, 0], [20, 0], [17, 0], [18, 0], [16, 0], [11, 0], [13, 0], [14, 0], [12, 0], [9, 0], [10, 0], [8, 0], [4, 0], [5, 1], [6, 0], [2, 0]] , 167 Nodes , 6 Levels , Maximum Fan-Out:33, Overlap:1
#[[63, 0], [61, 0], [63, 0], [62, 0], [59, 0], [57, 0], [59, 0], [63, 0], [62, 0], [61, 0], [60, 0], [58, 0], [55, 0], [53, 0], [55, 0], [51, 0], [49, 0], [51, 0], [55, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [53, 0], [54, 0], [52, 0], [50, 0], [47, 0], [45, 0], [47, 0], [46, 0], [43, 0], [41, 0], [43, 0], [47, 0], [39, 0], [37, 0], [39, 0], [35, 0], [33, 0], [35, 0], [39, 0], [47, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [43, 0], [46, 0], [45, 0], [44, 0], [41, 0], [42, 0], [40, 0], [37, 0], [38, 0], [36, 0], [34, 0], [31, 0], [29, 0], [31, 0], [30, 0], [27, 0], [25, 0], [27, 0], [31, 0], [26, 0], [23, 0], [21, 0], [23, 0], [22, 0], [19, 0], [17, 0], [19, 0], [23, 0], [31, 0], [27, 0], [15, 0], [13, 0], [15, 0], [11, 0], [9, 0], [11, 0], [15, 0], [7, 0], [5, 0], [7, 0], [3, 0], [1, 0], [3, 0], [7, 0], [15, 0], [31, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [47, 0], [46, 0], [45, 0], [44, 0], [43, 0], [42, 0], [41, 0], [40, 0], [39, 0], [38, 0], [37, 0], [36, 0], [35, 0], [34, 0], [33, 0], [32, 0], [27, 0], [30, 0], [29, 0], [28, 0], [23, 0], [26, 0], [25, 0], [24, 0], [19, 0], [22, 0], [21, 0], [20, 0], [17, 0], [18, 0], [16, 0], [11, 0], [13, 0], [14, 0], [12, 0], [8, 0], [9, 1], [10, 0], [4, 0], [5, 1], [6, 0], [2, 0]] , 167 Nodes , 6 Levels , Maximum Fan-Out:33, Overlap:1
#[[63, 0], [61, 0], [63, 0], [62, 0], [59, 0], [57, 0], [59, 0], [63, 0], [62, 0], [61, 0], [60, 0], [58, 0], [55, 0], [53, 0], [55, 0], [51, 0], [49, 0], [51, 0], [55, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [53, 0], [54, 0], [52, 0], [50, 0], [47, 0], [45, 0], [47, 0], [46, 0], [43, 0], [41, 0], [43, 0], [47, 0], [39, 0], [37, 0], [39, 0], [35, 0], [33, 0], [35, 0], [39, 0], [47, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [43, 0], [46, 0], [45, 0], [44, 0], [41, 0], [42, 0], [40, 0], [36, 0], [37, 1], [38, 0], [34, 0], [31, 0], [29, 0], [31, 0], [30, 0], [27, 0], [25, 0], [27, 0], [31, 0], [26, 0], [23, 0], [21, 0], [23, 0], [22, 0], [19, 0], [17, 0], [19, 0], [23, 0], [31, 0], [27, 0], [15, 0], [13, 0], [15, 0], [11, 0], [9, 0], [11, 0], [15, 0], [7, 0], [5, 0], [7, 0], [3, 0], [1, 0], [3, 0], [7, 0], [15, 0], [31, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [47, 0], [46, 0], [45, 0], [44, 0], [43, 0], [42, 0], [41, 0], [40, 0], [39, 0], [38, 0], [37, 0], [36, 0], [35, 0], [34, 0], [33, 0], [32, 0], [27, 0], [30, 0], [29, 0], [28, 0], [23, 0], [26, 0], [25, 0], [24, 0], [19, 0], [22, 0], [21, 0], [20, 0], [17, 0], [18, 0], [16, 0], [11, 0], [13, 0], [14, 0], [12, 0], [8, 0], [9, 1], [10, 0], [4, 0], [5, 1], [6, 0], [2, 0]] , 167 Nodes , 6 Levels , Maximum Fan-Out:33, Overlap:1
#Number of optimal overlapping graphs: 7
#Least levels: 6
#Least nodes among graphs with least levels: 167
#Minimum Overlap: 1 , Maximum Overlap: 1 (among optimal Overlapping Prefix Graphs)