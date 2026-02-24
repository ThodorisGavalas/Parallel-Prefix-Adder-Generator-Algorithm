vsim -gui work.testbench
add wave -position insertpoint  \
sim:/testbench/Abin \
sim:/testbench/Adec
add wave -position insertpoint  \
sim:/testbench/Bbin \
sim:/testbench/Bdec
add wave -position insertpoint  \
sim:/testbench/Cinbit \
sim:/testbench/Cin
add wave -position insertpoint  \
sim:/testbench/Sumbin \
sim:/testbench/Sumdec \
sim:/testbench/rightSum
add wave -position insertpoint  \
sim:/testbench/equal
add wave -position insertpoint  \
sim:/testbench/error
run 51.2 ns 
# 0.2x4^N ns