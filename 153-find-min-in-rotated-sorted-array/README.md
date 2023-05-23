key: find inflection point

compare midpoint to item at the right pointer.
if midpoint < right? we know that this COULD be a valid minimum,
ex:
1 < 2? yes. at this point we still don't know if this is the inflection point because it could still be on the left side of mid
store current mid as min. and continue searching left for the min

otherwise chop off leftside

solved this one by myself
