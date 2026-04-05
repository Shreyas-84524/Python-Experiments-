#Shreyas Rajendra Shigwan, Roll no. 90, CSE(AIML)
# Exp 5.4 - Debugging using pdb

import pdb

x = 20
y = 4

# (Breakpoint)
pdb.set_trace()

# Calculation
division = x / y

print("Division result is:", division)