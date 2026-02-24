library ieee;
use ieee.std_logic_1164.all;

entity operator is
    port (
        Gb,Pb,Ga,Pa : in std_logic;
        Gs,Ps : out std_logic);
end operator;

architecture arc of operator is 
	begin
			Gs <= Gb or (Pb and Ga);
			Ps <= Pb and Pa;
end arc;