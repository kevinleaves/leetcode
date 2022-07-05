/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */



var mergeTwoLists = function(l1, l2) {
  
    //create a result linked list
    var result = new ListNode();
    var head = result
  
    //compare heads, whichever node <, add first
    while (l1 && l2) {
      if (l1.val < l2.val) {
        result.next = new ListNode(l1.val)
        l1 = l1.next
      } else {
        result.next = new ListNode(l2.val)
        l2 = l2.next
      }
      
      result = result.next
    }
    
    
    //once both nodes are added, move onto next nodes
    //compare those nodes, add lesser to the result first
    
    if (l1)  {
      result.next = l1
    }
    if (l2) {
      result.next = l2
    }
  
    //return result head
    return head.next
};