key:

preallocate memory for res array since it's always the same length as temperature array

we CAN fill the res array out of order.
while current temp > temp at top of stack, pop and fill res array until the condition fails

otherwise we just add temps and their indices to the top of stack
