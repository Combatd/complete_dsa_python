import linked_list

def removeDups(ll):
    if ll.head is None:
        return
    else:
        currentNode = ll.head
        visited = set([currentNode.value])
        while currentNode.next:
            if currentNode.next.value is visited:
                currentNode.next = currentNode.next.next
            else:
                visited.add(currentNode.next.value)
                currentNode = currentNode.next
        return ll

# Time Complexity: O(n^2) Space Complexity: O(1)
def removeDups1(ll):
    if ll.head is None: # O(1)
        return
    
    currentNode = ll.head # O(1)
    while currentNode: # O(n^2)
        runner = currentNode
        while runner.next: # O(n)
            if runner.next.value == currentNode.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        currentNode = currentNode.next
    return ll.head


customLL = linked_list.LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
# removeDups(customLL)
removeDups1(customLL)