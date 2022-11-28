/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
//   init previous variable
  var prevNode = null;
//   init current node variable for traversal
  var currNode = head;
  
//   iterate while current node isn't empty
  while (currNode !== null) {
//     store next value in a temp variable so we don't lose it
    var tempNext = currNode.next;
//     reverse the connection
    currNode.next = prevNode;
//     update prev to current
    prevNode = currNode;
//     update curr to true next
    currNode = tempNext;
  }
  
//   when you reach the end of the list, return the head (which is prev at this point)
  return prevNode;
};