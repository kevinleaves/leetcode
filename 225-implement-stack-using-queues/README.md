in queues you have no access to the rightmost element

so the pop operation of this custom stack can never be O(1) time because you only have access to the left side which means we have to popleft N times in order to reach the rightmost element
