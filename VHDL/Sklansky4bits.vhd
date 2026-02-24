library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
entity PrefixGraph is
    generic (
    N : positive := 4
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
    signal Gpos0n0,Gpos1n0,Gpos2n0,Gpos3n0,Gpos3n1,Gpos1n1,Gpos3n2,Gpos2n1,Ppos0n0,Ppos1n0,Ppos2n0,Ppos3n0,Ppos3n1,Ppos1n1,Ppos3n2,Ppos2n1: std_logic;
    begin
Gpos0n0 <= Gin(0);
Ppos0n0 <= Pin(0);
Gpos1n0 <= Gin(1);
Ppos1n0 <= Pin(1);
Gpos2n0 <= Gin(2);
Ppos2n0 <= Pin(2);
Gpos3n0 <= Gin(3);
Ppos3n0 <= Pin(3);
operator_0: operator port map(Gpos3n0,Ppos3n0,Gpos2n0,Ppos2n0,Gpos3n1,Ppos3n1);
operator_1: operator port map(Gpos1n0,Ppos1n0,Gpos0n0,Ppos0n0,Gpos1n1,Ppos1n1);
operator_2: operator port map(Gpos3n1,Ppos3n1,Gpos1n1,Ppos1n1,Gpos3n2,Ppos3n2);
operator_3: operator port map(Gpos2n0,Ppos2n0,Gpos1n1,Ppos1n1,Gpos2n1,Ppos2n1);
Gout(0) <= Gpos0n0;
Pout(0) <= Ppos0n0;
Gout(1) <= Gpos1n1;
Pout(1) <= Ppos1n1;
Gout(2) <= Gpos2n1;
Pout(2) <= Ppos2n1;
Gout(3) <= Gpos3n2;
Pout(3) <= Ppos3n2;
end graph;