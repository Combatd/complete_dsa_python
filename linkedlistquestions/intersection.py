from linked_list import LinkedList, Node

# Time Complexity: O(A + B), where A is the length of listA and B is the length of listB
# Space Complexity: O(1)
def intersection(listA, listB):
    if listA.tail is not listB.tail:
        return False
    
    lenA = len(listA)
    lenB = len(listB)

    shorter = listA if lenA < lenB else listB
    longer = listB if lenA < lenB else listA

    diff = len(longer) - len(shorter)
    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next

    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next

    return longerNode

# Helper addition method
def addSameNode(listA, listB, value):
    tempNode = Node(value)
    listA.tail.next = tempNode
    listA.tail = tempNode
    listB.tail.next = tempNode
    listB.tail = tempNode

listA = LinkedList()
listA.generate(3, 0, 10)

listB = LinkedList()
listB.generate(4, 0, 10)

addSameNode(listA, listB, 11)
addSameNode(listA, listB, 14)

print(listA)
print(listB)

print(intersection(listA, listB))