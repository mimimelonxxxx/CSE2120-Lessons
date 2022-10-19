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

### Data Structure Indexing and Calling

Frequently, calling on a single value within the data structure is needed instead of the entire structure. Therefore, there needs to be a process of identifying a single value. Each value has a positional index number associated with it. 

```python 
indexNumber = [0, 1, 2, 3, ...]
```

To reference a specific value, include the list name followed immediately with the index number in [square brackets]. 

```python 
A_LIST = ["This", "is", "a", "sentence."]
print(A_LIST[3]) # sentence. 
```

Array indexing has forward (head-to-tail) indexing and backwards (tail-to-head) indexing. Either index number will call the data value. 

```python 
A_LIST = ["This", "is", "a", "sentence."]
# index     0      1     2      3 
# index    -4     -3    -2     -1
print(A_LIST[-2]) # a
```

To reference a subset of values, you can include a start index value and an end index value separated by a colon. Note that a subset starts at the starting index value, but goes up to and **not** including the end index value. 

```python
A_LIST = ["This", "is", "a", "sentence."]
print(A_LIST[-2:2]) # []
print(A_LIST[1:3]) # ["is", "a"]
```

There are two shortcuts to creating sublists from the beginning and the end of the list. When starting a sublist from the beginning of the list, omit the first number, and when creating one from the end, omit the last number. 

```python
A_LIST = ["This", "is", "a", "sentence."]
print(A_LIST[2:]) # ["a", "sentence."]
print(A_LIST[:3]) # ["This", "is", "a"]
```

All lists also have a length property, where the total number of data values is callable using the `len(LIST)` function. 

```python
len(A_LIST) # 4 
for i in range len(A_LIST):
    print(A_LIST[i])
"""
This
is
a
sentence. 
"""
# the same as doing 
print(A_LIST[0])
print(A_LIST[1])
print(A_LIST[2])
print(A_LIST[3])
```

### Manipulating Data in Lists

Data in a dynamic list can undergo many processes. They are often summarized by the acronym CRUD (create, read, update, delete). 

### Creating Data in Arrays

#### Appending Data to the End of a List 

To add data to the tail of a list, use the `append(DATA)` dot function. 

```python
A_LIST = ["This", "is", "a", "sentence."]
A_LIST.append("Hi there!")
print(A_LIST) # ["This", "is", "a", "sentence.", "Hi there!"]
A_LIST.append("How are you?")
print(A_LIST) # ["This", "is", "a", "sentence.", "Hi there!", "How are you?"]
```

#### Inserting Data to a Specific Index Value Within a List 

To add data to a specific index position in the list, use the `index(index, DATA)` dot function. This function should be used sparingly, because it shifts the indexes of the other nodes by one. This may result in mis-addressing data. 

```python
A_LIST = ["this", "is", "a", "sentence."]
A_LIST.insert(2, "not") 
print(A_LIST) # ["this", "is", "not", "a", "sentence."]
```

### Reading Data in Arrays 

All examples are found in the introduction above. 

```python
print(A_LIST[1]) # is
```

### Updating Data in Arrays

REMEMBER that tuples cannot update a single value. Instead, the entire tuple must be re-declared with the new value. To update a single list, the list node can be assigned a new value. 

To update a specific index within an array, simply re-assign the index. This is preferable to inserting data to a specific value because the other nodes are not changed. 

```python 
A_LIST = ["this", "is", "a", "sentence."]
A_LIST[0] = "This"
print(A_LIST) # ["This", "is", "a", "sentence."]
```

### Deleting Values in Data Arrays 

Deleting data from an array will change the overall length of the array and may re-assign new index values to pre-existing values within the array. 

#### Pop Data Off an Array 

To pop a value off an array, the `pop(index)` dot function will remove the value at the index number. When using `.pop()` data is removed from the list, but not destroyed. If desired, the removed data can be stored in a new variable. 

Note: If no index value is given, `.pop()` will remove the highest index value. 

```python
A_LIST = ["This", "is", "a", "sentence."]
A_LIST.pop()
print(A_LIST) # ["This", "is", "a"]
A_LIST.pop(1)
print(A_LIST) # ["This", "a"]
VARIABLE = A_LIST.pop(0)
print(VARIABLE) # This
print(A_LIST) # ["a"]
```

#### Remove Data From an Array

To remove a value off an array, the `.remove(VALUE)` dot function will remove the first instance of the value while traversing the array from head-to-tail. 

```python
A_LIST = ["This", "is", "a", "sentence."]
A_LIST.remove("a")
print(A_LIST) # ["This", "is", "sentence."]

NEW_LIST = [2, 3, 5, 7, 11, 13, 11, 17]
NEW_LIST.remove(11)
print(NEW_LIST) # [2, 3, 5, 7, 13, 11, 17]
```

### What Data is Stored in an Array? 

In python, an array can store any combination of data types; however, more structerd languages, such as Java, an array can only store one type of data. 

Furthermore, python cannot create *empty* arrays, like other languages. 

Note: IB follows traditional array limitations of only having one data type in the array. 

```python
# you can do this
ARRAY = [] # the list is full of null
# you cant just have a list of nothing 
ARRAY = # gives an error 
```

## IB Content

### Queueing 

A **queue** is a list of data items, content, etc, stored so that the information is retrievable in the order they are added to a list. It is often referred to as *LILO (Last in, Last out)*, or *FIFO (First in, First out)*. An example of a queue is waiting in line at a water fountain. 

IB Pseudocode uses the dot methods `enqueue` and `dequeue`, which cannot be used in python without first importing the queue library. 

```python 
A_LIST.enqueue(DATA) # adds items to the end of the list 
A_LIST.dequeue() # removes item from the start of the list

# the same as 
A_LIST.append(DATA)
A_LIST.pop(0)
```
### Stacking 

A **stack** is a list of data, items, comments, etc, stored in a way that the most recently stored data is the first to be retrieved. It is often reffered to as *LIFO (Last in, first out)* or *FILO (First in, last out)*. An example of a stack is a pile of books waiting to be returned to the library. The books on the top of the pile were the last ones placed on the pile, but the first ones to be returned. Another example is the undo feature found in most programs. 

IB Pseudocode uses the dot methods `pop` and `push`. `Pop` is the same as the `pop` in python; `push` is the same as the `append` in python. 

```python 
A_LIST.push(DATA) # adds item to the end of the list 
A_LIST.pop() # removes item from the end of the list 
```

## Multi-dimensional Arrays 

An array can store more than primitve data, they can store additional data structures. An array that stores additional data structures is called a multi-dimesional array. THese arrays normally only go two levels deep. Therefore, the most common multi-dimensional arrays are 2D arrays. 

There are three main multi-dimensional arrays and one IB structure: Dictionaries, Parallel arrays,  2-Dimensional arrays, and Linked Lists (IB). 

### Dictionary 

Dictionaries translate information from one data to another. it takes the key and transforms it into the value found within the dictionary. Keys tend to be primitive data types, but can return advanced data types. 

```python 
MY_INFO = {
    "first-name": "Michelle",
    "last-name": "Jiang",
    "date-created": "2022-10-11",
    "age": 16,
    "title": "Dictionary Example"
}
print(MY_INFO["first-name"]) # Michelle 
```

Dictionaries are often used to pass data between multiple programming languages within a single program. 

### Parallel Arrays 

Parallel arrays are two independent lists that share information based on their index number. Parallel arrays are not multi-dimensional arrays in teh sense of having multiple layers of data; instead, they are considered individual lists that use the index number to link data together. 

```python 
FIRST_NAME = ("Michelle", "Alice")
LAST_NAME = ("Jiang", "Wong")
print(FIRST_NAME[1], LAST_NAME[1]) # Alice Wong
```

Because data must stay aligned so that the index numbers reference the correct values, tuples are often used. 

### 2-Dimensional Arrays 
A 2-Dimensional array has a list in another list. While there are other data structures, like Objects, 2D arrays are often lists/tuples within other lists/tuples. This is like a list of lists. 2D arrays are often used to express tables (like a paralle array). 

Nodes within a sublist are identified after first identifying the note in the main list using square brackets. (NOTE: a node is a position within the list/tuple.)

```python
NUMBERS = ((1, 2), (3, 4), (5, 6))
print(len(NUMBERS)) # 3 
print(len(NUMBERS[0])) # 2
print(NUMBERS[0]) # (1, 2)
print(NUMBERS[1][0]) # 3
```

NOTE: 2-D arrays can represent tables. 

```python
NUMBERS = (
    (1, 2), 
    (3, 4), 
    (5, 6)
)
```

Each inner tuple represents a row and each index of the sub-lists represent a column. 

#### Updating and Deleting Data in 2D Arrays

Updating and deleting data in 2D arrays is similar to 1D arrays. The program can either update or delete the entire sub-array or a value within a sub-array. 

```python
NUMBERS = [[1, 2], [3, 4], [5, 6]]
NUMBERS[0][1] = 5 # [[1, 5], [3, 4], [5, 6]]
NUMBERS[0] = [4, 5, 6] # [[4, 5, 6], [3, 4], [5, 6]]

NUMBERS.pop(1) # [3, 4] NOTE: pop uses () 
NUMBERS[0].pop(2) # 6 NOTE: manipulating sub-arrays uses []
```

NOTE: Lists inside of tuples cannot be edited at all. 

### Using For Loops with 2D Arrays 

For loops are a convenient tool for creating, updating, and reading data within a list. 

```python
# create an empty array of 7 spaces 
A_LIST = []
for i in range(7): 
    A_LIST.append(None)
    
# A_LIST = [None, None, None, None, None, None, None]
```

2D arrays require nested for loops to create. 

```python 
A_LIST = []
# creating a 2D array that represents a 3x4 table 
for i in range(3): # creates the rows
    A_LIST.append([])
    for j in range(4): # creates the columns 
        A_LIST[i].append(None)
```

## Traversing Arrays

**Traversing** an array uses a `for` loop to access each node in the array. There are two methods of traversing head-to-tail (ascending index number) through the array. 

```python
A_LIST = [1, 3, 5, 7, 11]

# Method 1: Uses an intermediate variable (often i) for the index 

for i in range(len(A_LIST)):
    print(A_LIST[i]) 

# Method 2: Uses an intermediate variable to store the data in the node 

for node in A_LIST: 
    print(node) # basically stores the data in the node as variable node 

# NOTE: Method 2 cannot update the information within the list 

# Method 2 does not store the index/position of the data within the list, while method 1 only has the position, not the data 
```

It is possible to traverse an array from tail-to-head. 

```python
for i in range(len(A_LIST)-1, -1, -1) # starts from the end, goes backwards and stops at the start
    print(A_LIST[i])
    """
    11
    7
    5
    ...
    """

# Example of tail-to-head for loop usage situation
for i in range(len(A_LIST)-1, -1, -1):
    A_LIST.pop(i)
```

Because the range of the loop is determined at the **start** of the loop, any changes to the length of the array will not change the number of iterations for the loop. Therefore, when shortening an array during a for loop, traversing tail-to-head will prevent/reduce *index out of range* errors. 

Arrays can be added together, but they can't be subtracted, multiplied, or divided. (They're not matrices in mathematics.)

```python
LIST1 = [1, 2, 3]
LIST2 = [4, 5, 6]
LISTADD = LIST1 + LIST2 # joins the lists 
print(LISTADD) # [1, 2, 3, 4, 5, 6] 
# Can be used for blackjack, so you could add the hand to the bottom of the deck to reset the deck 
```

Arrays can be assigned multiple variable names. 

```python 
LIST = [1, 2, 3, 5, 11]
NEWLIST = LIST # points to the same data structure 
NEWLIST.pop()
print(LIST) # [1, 2, 3, 5]
# Even though it was popped out of NEWLIST, it popped out of the same data structure 

# if you wanted to copy the list, you could just create an empty list and then append each item in the list or use the copy library 
```

To copy an array, the data has to be appended into a separate, empty array by traversing the array that is being copied. 

## Working with Strings 

ALL strings are lists in disguise. While you are not able to do all actions with a string, as you can with a list, it is possible to create substrings, identify individual characters, and traverse strings. 

```python 
STRING = "hello world" 
print(STRING[0]) # h 
print(STRING[0:2]) # he 
print(len(STRING)) # 11 (space counts as a character)
```

Strings can be separated into a list using the `.split()` dot function. Placing a string inside of the paranthesis will split the string using the characters in the `.split()`. 

```python 
STRING_LIST = STRING.split() # ["hello", "world"]
STRING_LIST2 = STRING.split(l) # ["he", "", "o wor", "d"] doesn't split at the space anymore 
# imagine you replaced the delimiter with a comma 
```

NOTE: when splitting a string, the characters used to identify where the split occurs is called the **delimiter**. 

It is possible to combine a list of **strings** into a string. 

```python 
STRING_LIST = ["hello", "world"]
NEWSTRING = " ".join(STRING_LIST) # format is the delimiter .join(VARIABLE)
print(NEWSTRING) # hello world 
```

NOTE: the delimiter is specific within quotations with a dot function of `.join(LIST)`. It is added in between each node of the list. Eg: the find and replace tool in documents. (splits at the word, and then rejoins with the replaced word)