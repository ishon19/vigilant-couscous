/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
fun mergeInBetween(list1: ListNode?, a: Int, b: Int, list2: ListNode?): ListNode? {
    // 1. Traverse to find the node just before the removal section (at index a-1).
    var startNode = list1
    for (i in 0 until a - 1) {
        startNode = startNode?.next
    }

    // 2. From startNode, traverse to find the last node of the removal section (at index b).
    var endNode = startNode
    for (i in 0 until b - a + 1) {
        endNode = endNode?.next
    }

    // 3. Connect the first part of list1 to the head of list2.
    // The nodes from index 'a' to 'b' are now detached from the first part.
    startNode?.next = list2
    
    // 4. Traverse to the tail of list2.
    var list2Tail = list2
    while (list2Tail?.next != null) {
        list2Tail = list2Tail.next
    }

    // 5. Connect the tail of list2 to the remaining part of list1.
    list2Tail?.next = endNode?.next

    // 6. Return the original head of list1.
    return list1
}
}