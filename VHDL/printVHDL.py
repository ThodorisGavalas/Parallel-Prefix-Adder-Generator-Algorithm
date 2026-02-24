def printVHDLoverlap(seq,n):
    bitspan=list(range(n))
    nodes= [0 for i in range(n)] #Each position of "nodes" is a bit position, the number in this position is the number of nodes in this bit position
    components =[] 
    # "components" is a list of the operator components of the Prefix Grpaph, every component is a list consisting of 3 lists of 2 numbers
    # The first list of the 3 is the more important input signal, the second is the less important input signal and the third is the output signal
    # The first number of a singal list is the bit position and the second number is the number of the node of the signal
    for i in range(len(seq)):
        overlap=seq[i][1]
        components.append([[seq[i][0],nodes[seq[i][0]]],[bitspan[seq[i][0]]-1+overlap,nodes[bitspan[seq[i][0]]-1+overlap]],[seq[i][0],nodes[seq[i][0]]+1]])
        nodes[seq[i][0]] = nodes[seq[i][0]] + 1
        bitspan[seq[i][0]] = bitspan[bitspan[seq[i][0]]-1+overlap]
        # seq[i] implies a connection of the signal in bit position seq[i] in the most recent node and the signal in bit position bitspan[seq[i]]-1+overlap in the most recent node
        # The output of this connection is in a new node in bit position seq[i]

    InputSignals = [f"pos{i}n0" for i in range(n)]
    ComponentSignals = [f"pos{component[2][0]}n{component[2][1]}" for component in components]
    # "posinj" is the signal in bit postion i in the node j
    signals = InputSignals + ComponentSignals
    Gsignals = [f"G{signal}" for signal in signals]
    Psignals = [f"P{signal}" for signal in signals]
    GPsignals = Gsignals + Psignals
    inassignments = []
    for i in range(n):
        inassignments.append(f"Gpos{i}n0 <= Gin({i});")
        inassignments.append(f"Ppos{i}n0 <= Pin({i});")
    operators= []
    for i in range(len(components)):
        operators.append(f"operator_{i}: operator port map(Gpos{components[i][0][0]}n{components[i][0][1]},Ppos{components[i][0][0]}n{components[i][0][1]},Gpos{components[i][1][0]}n{components[i][1][1]},Ppos{components[i][1][0]}n{components[i][1][1]},Gpos{components[i][2][0]}n{components[i][2][1]},Ppos{components[i][2][0]}n{components[i][2][1]});")
    outassignments = []
    for i in range(n):
        outassignments.append(f"Gout({i}) <= Gpos{i}n{nodes[i]};")
        outassignments.append(f"Pout({i}) <= Ppos{i}n{nodes[i]};")
    vhdlcode = f"""
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
entity PrefixGraph is
    generic (
    N : positive := {n}
    );
    port (
    Gin,Pin : in std_logic_vector(N-1 downto 0);
    Gout,Pout : out std_logic_vector(N-1 downto 0));
end PrefixGraph;
architecture graph of PrefixGraph is 
    component operator
        port (
        Gb,Pb, Ga, Pa : in std_logic;
        Gs,Ps : out std_logic);
    end component;
    signal {",".join(GPsignals)}: std_logic;
    begin
{chr(10).join(inassignments)}
{chr(10).join(operators)}
{chr(10).join(outassignments)}
end graph;
"""
    print(vhdlcode)

seq = [[3,0],[1,0],[3,0],[2,0]] 
printVHDLoverlap(seq,4)