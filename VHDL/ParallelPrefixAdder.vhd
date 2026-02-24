library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity ParallelPrefixAdder is
  generic (
    N : positive := 4
  );
  port (
    A, B : in  std_logic_vector(N-1 downto 0);
     Cin : in std_logic;
    Sum  : out std_logic_vector(N-1 downto 0);
    Cout : out std_logic);
end entity ParallelPrefixAdder;

architecture adder of ParallelPrefixAdder is 
	component PrefixGraph
		generic (
		N : positive := 4
		);
		port (
		Gin,Pin : in std_logic_vector(N-1 downto 0);
		Gout,Pout : out std_logic_vector(N-1 downto 0)
		);
	end component;
	
	signal Gin,Pin,Gout,Pout : std_logic_vector(N-1 downto 0);
	signal C : std_logic_vector(N downto 0);
	
	begin
		generate_label:
		for i in 0 to N-1 generate
			Gin(i) <= A(i) and B(i);
			Pin(i) <= A(i) xor B(i);
		end generate;
		
		PrefixGraph_1: PrefixGraph port map(Gin,Pin,Gout,Pout);
		
		C(0) <= Cin;
		
		generate1_label:
		for i in 1 to N generate
			C(i) <= Gout(i-1) or (Pout(i-1) and C(0));
		end generate;
		
		Cout <= C(N);

		generate2_label:
		for i in 0 to N-1 generate
			Sum(i) <= A(i) xor B(i) xor C(i);
		end generate;
		
end adder;