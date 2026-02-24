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
                            if DetermineLevels(newGraph,i) <= 3 and len(newGraph) <= 7: #7
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 7:
                            if DetermineLevels(newGraph,i) <= 3 and len(newGraph) <= 9: #9
                                G[i].append(newGraph)
                                print(f"{i}-bit Graphs created :{len(G[i])}")
                        elif i == 8:
                            if DetermineLevels(newGraph,i) <= 3 and len(newGraph) <= 12: #12
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
                            if DetermineLevels(newGraph,i) <= 3 and len(newGraph) < 7: #7
                                N_lists[i].append(newGraph)
                        elif i == 7:
                            if DetermineLevels(newGraph,i) <= 3 and len(newGraph) < 9: #9
                                N_lists[i].append(newGraph)
                        elif i == 8:
                            if DetermineLevels(newGraph,i) <= 3 and len(newGraph) < 12: #12
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
