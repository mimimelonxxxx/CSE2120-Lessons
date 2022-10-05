# CSE2120 - Data and Data Structures

Today is the day I find out I'm an idiot. 

Data structures are organizational, management, and formatting tools for storing large data sets. In programming, these structures are stored in variables or other data structures. There are many different types of data structures: Tuples, Lists, Arrays, Dictionaries, (IB) Queues, and Stacks. (IB)

## Types of Data Structures in Python

### Tuples 

A *tuple* is a static data structure, where the data is immutable. All data is declared when the variable is created. 

```python
# Tuple 
A_TUPLE = (1, 3, 5.0, "eleven", 13) # uses paranthesis
A_TUPLE = (1, 3, 5.0, "eleven", 17)

NAME = (firstname, lastname)
DATE = (year, month, day)

print(A_TUPLE) # output (1, 3, 5.0, "eleven", 17)
print(A_TUPLE[1]) # output 3
```

Python allows you to use multiple data types within a data structure, but other languages (such as Java) will not let you do so. 

When using data structures, each individual data node within the structure is assigned an **index number**. This index number identifies the specific location that the data is stored in the strucutre. Index numbers begin counting at **0** and increases as integers. 

(IB) - IB does not use the term "tuple" because it is a python-specific term. Instead, IB will use the term array. 

### Lists

A *list* is a one dimensional array that is a dynamic data structure, where individual nodes are mutable. 

```python
# List 
A_LIST = [1, 3, 5.0, 7, "eleven", 13]
A_LIST[5] = 17 # updates a single value in a list 
print(A_LIST) # outputs [1, 3, 5.0, 7, "eleven", 17]
print(A_LIST[4]) # outputs eleven (without quotations) 
```

Note: Despite tuples using parentheses and lists using brackets, when declaring an index value or node, the index number is always in [brackets]. 

(IB) Lists in Java, which is what IB pseudocode is based upon, calls dynamic lists "ArrayLists."  

### Static vs Dynamic Arrays 

In most cases, either a static or dynamic array can be used to store data. However, there are instances where one is preferable over the other. 

For data that should not be changed independently, static arrays are preferable. 

- Storing screen resolution 
- Storing a position on a 2D or 3D plane 
- Storing identification information of an individual 

Oftentimes, tuples are used to store information that is difficult to change. For example, your name links to your student ID. One should never be changed in a program without changing the other. 