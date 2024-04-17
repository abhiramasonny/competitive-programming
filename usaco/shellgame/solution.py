import os
read = open("shell.in")

n = int(read.readline())

# shell_at_pos[i] stores the label of the shell located at position i
# The shells can be placed arbitrarily at the start.
shell_at_pos = [i for i in range(3)] 

# counter[i] stores the number of times the shell with label i was picked
counter = [0 for _ in range(3)]


# [0,0,0]
for i in range(n):
    operation = read.readline()
    operation = operation.split()
    
    swap = int(operation[0])-1
    swapwith = int(operation[1])-1
    guess = int(operation[2]) - 1
    shell_at_pos[swap],shell_at_pos[swapwith] = shell_at_pos[swapwith],shell_at_pos[swap] 
    
    counter[int(shell_at_pos[guess])] += 1
    
read.close()

# Check if "shell.out" already exists
if not os.path.exists("shell.out"):
    # Create "shell.out" file
    with open("shell.out", "w") as f:
        f.write(str(max(counter)))
write = open("shell.out")
write.write(str(max(counter)))
write.close()
    