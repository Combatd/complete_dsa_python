# What is Recursion?
* Recursion is a way of solving a problem by have a function call itself.
* Performing the same operation multiple times with different inputs
* In every step we try smaller inputs to make the problem smaller
* A base condition is needed to stop the recrusion, otherwise an infinite loop will occur.

# Why do we need Recursion?
* Recursive thinking is important in programming, and it helps you break down big problems into smaller ones, making it easier to use.
* Recursion is prominently used in data structures like trees and graphs.
* Interviews will have problems where recursion is optimal
* It is used in many algorithms (divide and conquer, greedy, dynamic programming)

## When should you choose Recursion?
* If you can divide the problem into similar subproblems
* Design an algorithm to compute nth.
* Write code to list the first n
* Implement a method to compute all
* To practice writing clean code.

# How does Recursion work?
1. A method calls itself
2. It exists from an infinite loop.

```
Methods going into stack memory

def firstMethod():
    secondMethod()
    print("I am the first method)

def secondMethod():
    thirdMethod()
    print("I am the second method)

def thirdMethod():
    fourthMethod()
    print("I am the third method)

def firstMethod():
    print("I am the fourth method)
```

```
Direct Recursion - Last in First Out

def recursiveMethod(n):
    if n < 1:
        print("n is less than 1")
    else:
        recursiveMethod(n-1)
        print(n)
```

# Recursive vs Iterative Solutions
* Any problem that can be solved recursively can be solved iteratively.
* Sometimes, converting a recursion to an iteration solution is difficult.
* Recursion repeatedly invokes the mechaism over method calls, adding a new layer to the stack memory. - time and space inefficient.
* Dealing with graph algorithms and other complex abstract data types is more efficienty to use recursion, because we know that a problem can be divided into similar sub-problems.
* Many complicated codes can be written in recursion very easily, even if iteration can be more time and space efficient in other cases.

```
def powerOfTwo(n):
    if n == 0:
        rturn 1
    else:
        power = powerOfTwo(n - 1)
        return power * 2
```
```
def powerOfTwoIt(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i = i + 1
    return power
```