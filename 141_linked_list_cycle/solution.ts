/**
 * Definition for singly-linked list.
 */

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function hasCycle(head: ListNode | null): boolean {
  const TOUCHED_VAL: number = 10 ** 6; // 10**-5 <= node.val <= 10**5

  let node: ListNode = head;

  while (true) {
    if (!node) {
      break;
    }

    if (node.val === TOUCHED_VAL) {
      return true;
    }

    node.val = TOUCHED_VAL;
    node = node.next;
  }

  return false;
}
