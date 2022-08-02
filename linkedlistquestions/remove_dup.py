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

customLL = linked_list.LinkedList()
customLL.generate(10, 0, 99)
# print(customLL)
removeDups(customLL)