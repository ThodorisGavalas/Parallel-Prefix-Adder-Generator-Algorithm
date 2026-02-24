library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity testbench is
	generic (
	    N : positive := 4
	  );
end entity testbench;

architecture test_prefix of testbench is
	
	component ParallelPrefixAdder is
	  generic (
	    N : positive := 4
	  );
	  port (
	    A, B : in  std_logic_vector(N-1 downto 0);
	    Cin  : in std_logic;
	    Sum  : out std_logic_vector(N-1 downto 0);
	    Cout : out std_logic);
	end component ParallelPrefixAdder;

	signal Abin,Bbin: std_logic_vector(N-1 downto 0);
	signal Sumbin: std_logic_vector(N downto 0);
	signal Cinbit: std_logic_vector(0 downto 0);
	signal equal: std_logic;
	signal Adec,Bdec,Cin,Sumdec,rightSum,error: natural;

	begin

	UUT: ParallelPrefixAdder port map
	(Abin,Bbin,Cinbit(0),Sumbin(N-1 downto 0),Sumbin(N));

	Sumdec <= to_integer(unsigned(Sumbin));
	rightSum <= Adec + Bdec + Cin;
	equal <= '1' when rightSum=Sumdec else '0';

	process
	 variable error_count: natural := 0;
	begin
	A: for A in 0 to (2**N)-1 loop
	 Adec <= A;
	 Abin <= std_logic_vector(to_unsigned(A,N));
	 B: for B in 0 to (2**N)-1 loop
	  Bdec <= B;
	  Bbin <= std_logic_vector(to_unsigned(B,N));
	  C: for C in 0 to 1 loop
	   Cin <= C;
	   Cinbit <= std_logic_vector(to_unsigned(C,1));
	   wait for 50 ps;
	   if equal = '0' then
	    error_count := error_count + 1;
		report "Error at A=" & integer'image(A) & " B=" & integer'image(B) & " Cin=" & integer'image(C);
	   end if;
	   wait for 50 ps;
	  end loop;
	 end loop;
	end loop;
	error <= error_count;
	report "Total errors: " & integer'image(error_count);
	wait;  -- Prevent continuous loop
	end process;
end architecture test_prefix;