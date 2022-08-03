import linked_list

# Time Complexity: O(n)
# Space Complexity: O(1)

def partition(ll, x):
    currentNode = ll.head
    ll.tail = ll.head

    while currentNode:
        nextNode = currentNode.next
        currentNode.next = None
        if currentNode.value < x:
            currentNode.next = ll.head
            ll.head = currentNode
        else:
            ll.tail.next = currentNode
            ll.tail = currentNode
        currentNode = nextNode
    
    if ll.tail.next is not None:
        ll.tail.next = None

customLL = linked_list.LinkedList()
customLL.generate(10, 0, 99)
print(customLL)

partition(customLL, 30)