monotonic decreasing stack

store price:span pairs

        # store price/span pairs in stack
        # before we add pair to stack we check if price < top of stack. if so add price:1 return 1
        # if price >= top of stack,
        # while iteration to pop top of stack
            # with every successful pop, increment current price's span by amt of the popped span
        # add price:span to top of stack
        # return top stack span
