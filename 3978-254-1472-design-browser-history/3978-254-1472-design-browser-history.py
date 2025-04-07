class ListNode:
  def __init__(self, val):
    self.val = val
    self.prev = None
    self.next = None


class BrowserHistory:

    def __init__(self, homepage: str):
        # self.curr will always point to our current website
        self.curr = ListNode(homepage)

    def visit(self, url: str) -> None:
        # make a new node
        new_node = ListNode(url)
        new_node.prev = self.curr
        self.curr.next = new_node
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        # find the reference to the node we should go back to
        # this reference cannot be null
        curr = self.curr
        while curr.prev and steps > 0:
          curr = curr.prev
          steps -= 1
        res = curr.val
        self.curr = curr
        return res
        

    def forward(self, steps: int) -> str:
        curr = self.curr
        while curr.next and steps > 0:
          curr = curr.next
          steps -= 1
        res = curr.val
        self.curr = curr
        return res


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)