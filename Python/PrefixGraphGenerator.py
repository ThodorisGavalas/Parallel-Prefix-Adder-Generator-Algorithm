def checkValidOverlap(seq,n):
    bitspan = list(range(n))  # bitspan=[0,1,...,n-1] , n is the number of bits
    #Each position of the bitspan is a bit position, the number in this position is the LSB of the propagate-generate block whose MSB is the bit position
    #The point of parallel prefix structures is to create blocks as many as the number of bits whose MSB is each bit position and LSB=0
    for i in range(len(seq)):
        overlap = seq[i][1] # seq[i][0] is a bit position
        if bitspan[seq[i][0]]-1+overlap >= seq[i][0]: # To avoid connecting a bit position in a node of a less or equally significant bit position
            return 0
        if bitspan[seq[i][0]] <= bitspan[bitspan[seq[i][0]]-1+overlap]: # To avoid creating unnecessary connections
            return 0 # Each connection must reduce the bitspan of a bit position
        if i > 0 : # seq[0][0] is a bit position and connects to seq[0]-1+overlap
            if seq[i][0] > seq[i-1][0] and bitspan[seq[i][0]] -1 + overlap != seq[i-1][0]: # seq[i][0] > seq[i-1][0] always implies a connection of this two bit positions
                return 0 # 0 means there is connection(s) of blocks with the wrong overlap or non-adjacent blocks
        bitspan[seq[i][0]] = bitspan[bitspan[seq[i][0]]-1+overlap]
        # Every bit position in seq[i][0] connects to the bit position "bitspan[seq[i][0]]-1+overlap", so it gets the bitspan of this position
    return 1 if all(b == 0 for b in bitspan) else 2 # (We know bitspan[0]=0, there can be no "[0][overlap]" in seq)
    # 1 means that the Prefix Graph works , 2 that it doesn't work for all the bit positions so it's not completed

def DetermineLevels(seq,n):
    bitspan=list(range(n))
    levels = [0 for i in range(n)] #Each position of "levels" is a bit position, the number in this position is the level of the most recent node of this bit position
    for i in range(len(seq)):
        overlap = seq[i][1]
        levels[seq[i][0]] = max(levels[seq[i][0]],levels[bitspan[seq[i][0]]-1+overlap]) +1
        #Every number "seq[i][0]" implies a connection of the more significant bit position "seq[i][0]" and the less significant bit position "bitspan[seq[i][0]]-1+overlap"
        #The node of this connection is at bit position "seq[i][0]" at a level one higher than the highest level of these two bit positions so far
        bitspan[seq[i][0]] = bitspan[bitspan[seq[i][0]]-1+overlap]
    return max(levels)

def CalculateFanOuts(seq,n):
    bitspan=list(range(n))
    FanOuts = [[1] for i in range(n)] #Each position of FanOuts represents a bit position
    #FanOuts consists of lists of which each position represents a node of this bit position
    #Before the calculation starts, in every bit position there is 1 node with only 1 output connection
    for i in range(len(seq)):
        overlap = seq[i][1]
        FanOuts[seq[i][0]].append(1)
        FanOuts[bitspan[seq[i][0]]-1+overlap][-1] = FanOuts[bitspan[seq[i][0]]-1+overlap][-1] +1
        # seq[i][0] always implies a connection of the bit positions seq[i][0] and bitspan[seq[i][0]]-1 in a node in bit position seq[i][0]
        # So, bit position seq[i][0] gets a new node with 1 output connection and bit position bitspan[seq[i][0]]-1 gets a new output connection in the most recent node
        bitspan[seq[i][0]] = bitspan[bitspan[seq[i][0]]-1+overlap]
    MaxFanOut = max(max(Position) for Position in FanOuts)
    return MaxFanOut

N = int(input("Number of bits: "))
maxOverlap = int(input(f"Maximum number of overlapping bits (up to {N-2}): "))
# The largest overlap can happen if the bit position N-1 has got bitspan(N-1)=1 and connects to the bit position N-2 which has got bitspan(N-2)=0
# Then the overlap is (N-2) - bitspan(N-1) +1 = N-2-1+1 = N-2

# Form N-1 lists Gi (from i=2 to i=N), Gi consists of the Prefix Graphs of i bits which are lists of lists of 2 numbers
G = [[] for i in range(N+1)] # G[0] and G[1] will be empty
G[2] = [[[1,0]]] # G2 consists of one list with only one list, the number "1" in position 0 and the overlap "0" in position 1

# Form N-2 lists Ni (from i=3 to i=N), Ni consists of the non-completed Prefix Graphs from which the Gi Prefix Graphs can be constructed
N_lists = [[] for i in range(N+1)]
for i in range(3, N+1): 
    N_lists[i] = G[i-1].copy() # PGs of i bits will be constructed from PGs of i-1 bits
    for currentGraph in N_lists[i]:
        for position in range(len(currentGraph) + 1):
            for overlap in range(min(i-2,maxOverlap)+1):
                newGraph = currentGraph.copy()
                newGraph.insert(position, [i-1,overlap])
                validness = checkValidOverlap(newGraph, i)
                if validness == 1:
                    if newGraph not in G[i]: #For example, if we insert "[2,0]" in "[2,0],[1,0]" in the first 2 positions we create "[2,0],[2,0],[1,0]" twice ("[2,0],[2,0],[1,0]" is a 3-bit Kogge-Stone)
                        G[i].append(newGraph)
                        print(f"{i}-bit Graphs created :{len(G[i])}") # In order to view the progess of the algorithm while it's still running
                elif validness == 2:
                    if newGraph not in N_lists[i]:
                        N_lists[i].append(newGraph) # If the PG remains not-completed for i bits , it needs more insertions of "[i-1,overlap]"

print(f"All Prefix Graphs for {N} bits with maximum overlap of {maxOverlap} bits:")
for PrefixGraph in G[N]:
    print(PrefixGraph,f", {len(PrefixGraph)} Nodes",f", {DetermineLevels(PrefixGraph,N)} Levels",f", Maximum Fan-Out:{CalculateFanOuts(PrefixGraph,N)}")
print(f"Total number of Prefix Graphs of {N} bits with maximum overlap of {maxOverlap} bits: {len(G[N])}")

# Find Prefix Graphs with the least levels
LeastLevels = min(DetermineLevels(PrefixGraph, N) for PrefixGraph in G[N])
FastestGraphs = [PrefixGraph for PrefixGraph in G[N] if DetermineLevels(PrefixGraph, N) == LeastLevels]

# Among those, find the ones with the least nodes
LeastNodes = min(len(PrefixGraph) for PrefixGraph in FastestGraphs)
OptimalGraphs = [PrefixGraph for PrefixGraph in FastestGraphs if len(PrefixGraph) == LeastNodes]

print(f"\nOptimal Prefix Graphs (least levels, then least nodes):")
for PrefixGraph in OptimalGraphs:
    print(PrefixGraph,f", {len(PrefixGraph)} Nodes",f", {DetermineLevels(PrefixGraph,N)} Levels",f", Maximum Fan-Out:{CalculateFanOuts(PrefixGraph,N)}")
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