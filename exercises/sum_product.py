"""  
Write a function that calculates the sum and product of all elements in a tuple of numbers.
"""

def sum_product(input_tuple):
  sum = 0
  product = 1

  for element in input_tuple: # O(n)
    sum = sum + element

  for element in input_tuple: # O(n)
    product = product * element

  return (sum, product)

""" 
Time Complexity: O(n)
We have to loop through each element to calculate a sum, and calculate a product of all elements.

Space Complexity:
No additional memory is allocated when making these calculations.

Overall time complexity of the function is O(n) because the loop iterates through each element in the tuple once. 
The rest of the operations have constant time complexity O(1). 
The overall space complexity is O(1) because the function uses a constant amount of additional memory to store the sum and product, regardless of the size of the input tuple.

"""

"""  
def sum_product(t):
    sum_result = 0
    product_result = 1
 
    for num in t:
        sum_result += num
        product_result *= num
 
    return sum_result, product_result
"""