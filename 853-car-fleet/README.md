intuition:

take 2 arrays => combine them into 1 array but as pair.
sort them based on initial position, ascending left => right
utilize a stack to maintain order
iterate array starting from right side (largest position first)
for every pair, calculate how much time it takes to get to the target position (t = ?) and append it to stack

if left T < right T, we know left car has faster trajectory and the cars will intersect, which means the left car will slow down to the right car's speed. we pop off the faster car from the stack.

at the end we return the length of the stack.
