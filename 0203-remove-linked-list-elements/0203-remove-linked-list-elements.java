/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
      // sentinel node pointing to the current head
      ListNode sentinel = new ListNode(0, head);
      // prev node that trails behind the current node
      ListNode prev = sentinel;
      // curr that references current head
      ListNode curr = head;
      // traverse through list using curr
      while (curr != null) {
        ListNode next = curr.next;
        // if curr value is equivalent to our target val,
        if (curr.val == val) {
          // remove references to that node
          prev.next = next;
          // prev does not change
        } else {
        // otherwise
          // move prev forward
          prev = curr;
        }
          // move curr forward2
        curr = next;
      }
      // return head of the list using our dummy head
      return sentinel.next;
    }
}