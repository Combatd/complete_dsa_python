import linked_list

# Time Complexity: O(n)
# Space Complexity: O(1)

def nthToLast(ll, n):
    pointer1 = ll.head # O(1)
    pointer2 = ll.head # O(1)

    for i in range(n): # O(n)
        if pointer2 is None:
            return None
        pointer2 = pointer2.next

    while pointer2: # O(n)
        pointer1 = pointer2.next
        pointer2 = pointer2.next
    return pointer1

customLL = linked_list.LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
print(nthToLast(customLL, 3))