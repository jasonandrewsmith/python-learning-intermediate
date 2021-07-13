# Core Python - Getting Started

## Zen of Python
- Flat is better than nested
- Practicality beats purity
- There should only be one obvious way to do something
- Sparse is better than dense
  - 2 Lines between functions according to PEP8

## Scalar Types
- int
- float
- bool
- None

## int
- Always round down
- `int()` constructor can be passed floats, strings
- can write numbers in hex, octal, and binary literally
- other bases can be used with second constructor parameter

## float
- `float()` constructor can be passed ints, string, scientific notation
- all decimals are seen as this type

## bool
- `True` or `False`
- `bool()` can be passed different types and will determine result based on falsiness

## None
- essentially null
- variables can be set to it 
- checked with `is` or `==`

## While Loops
``` 
while True: 
    ...
```
```
while True:
    if True:
        break
```
- Python has no means of a do-while loop
- Interupt the repl with `ctrl+c`
  
## Collections
- str
- bytes
- list
- dict

## str
- Immutable, sequence of unicode code points
- Single or double quotes
  - Be consistent!
- String literals will be concatenated
  - "hey" "yo" is "heyyo"
- Triple quotes for multi line strings
- Raw strings do not support escape sequences
  - `r'heelo there'`
- Constructor can be passed other types for string version
- UTF-8 unicode

## bytes
- raw binary type
- `b'data'`
- There is a constructor but that's an advanced topic
- `str` -> encode -> `bytes` -> decode

## list
- sequences of objects
- mutable
- `[1,2,3]`
- access and write to an index
- add with `append()`
- can pass string to contructor to make list version of string

## dict
- fundamental to python
- access a key via `[key_name]`
- As of 3.7 keys stay in insertion order, older version have no concept of this 
  
## For Loops
- essentially a for each

## Functions and Modules
- special functions have `__name__`
- can be called "dunder"
- `__main__` means that the module is being run directly
  - If not equal to `__main__` it means that it's being imported
- Python files are modules by default

## Python Execution Model
- `def` is a statment
- Top level functions are defined when a module is imported or run
  
## Command Line Arguments
```python
import sys
sys.argv[1]
```

## docstrings
- literal strings that document functions, modules, and classes
- They must be the first statement in the blocks for these constructs
- Sphinx can be used to create HTML docs from these strings

## Comments
- Use #

## Shebang
- `#!/usr/bin/env python`
- can say if it's 2 or 3
- allows for direct execution on unix like systems
- windows can use pylauncher to achieve the same functionality

## Objects and Types
- Has as garbage collector
- Reassigning variables
  - uses references to assign variables to memory
  - can use `id()` to find the references id
  - can also use the `a is b` reference, returns a true or false
  - variables will have a reference, `=` only changes names to references, never values 
  - garbage collector scoops up unreferenced objects
- Python only has named references to objects
  - Not so much a bucket that holds a value
- objects are equivalent to themselves
  - `a == a -> True`

# Passing Arguments
- Arguments are pass by object reference
  - Means that references are copied, but not the objects themselves
  - Function parameters will keep the reference the original passed object
  - Be careful with reassignment as it will overwrite the reference
  - Can modify the original value carefully

# Return
- behaves the same as passing arguments

# Function Arguments
- can have default values
  - must be last
  - `def banner(first, second='hello'):`
  - these can be referenced by name to be more readable
```py
banner("hello there", second="Hello there again")
banner(second="Hello there again", first="hello there")
```
  - named arguments must be used after the positional arguments
  - **be careful to have defaults being function calls**
    - remember that def is called once on the initial run of the program
    - always use immutable objects (int, str, None)

# Type System
- Dynamic and strong type system
- Types are inferred
- Python typically doesn't coerce values

# Scopes
- Local -> Enclosing -> Global -> Built-in
- Scopes don't correspond to code blocks, blocks don't create scopes
- Python looks in most specific and works way up for references 
- Can run into issues if variables in local and global scopes have the same names
  - can rebind variables to the global scope with `global`

# Everything is an object
- Nearly everything is an object
- Even things like functions are objects
- Using `dir()` can show the associated attributes (often dunders)

# Tuples
- Immutable sequence of objects
- denoted by `("123", 1 , "asdf")`
- single tuple = `(123,)`
- empty = `()`
- can destructure (aka unpacking) results from functions
- tuples are used for variable swapping
  - `a, b = b, a`
- test for in/ not in with `in` and `not in`
- can make tuples from other collections with `tuple()`

# Strings 
- augmented assignment (aka +=)
  - should prefer using `join()`
  - `+` leads to many copies being created
- `';'.join('123', '456') == 123;456`
- can use `partion()`
  - splits into pre, partion, and after
  - can destructure with this into tuple
  - often don't want partition, convention for `_` to replace dummy values, many tools expect this
- `format()` has many uses, can replace from replacement fields
  - like `printf`
- fstrings are prefixed with `f` 
  - can inject python expressions with `{}`
  - `f"the value is {value}"`

# Range
- sequence representing an arithmetic progression of integers
- `range(6)` this is the constructor
- used for loop counters
- params are start, stop, step
- does not support keyword arguments
- `enumerate()` for iterating over index of values in a list

# Lists
- negative indicies allow you look from the end 
  - start at -1
  - -0 `==` 0
- slicing
  - extending indexing
  - `s[1:3]`
  - slices from everything non-inclusive
  - can use half open `s[:3]`
  - can use empty slice for shallow copying a list
    - references are from the original list anyway
  - can also use `s.copy()` or `list()` for shallow copy
- support repetition with `*`
  - copies the reference however
  - useful to duplicate a number multiple times
- `index()` returns the index of the first occuring index
- `del` removes a value from a list
- `insert()` inserts at a certain index
- can use + with another list or +=
- `reverse()` reverses in place
  - `reversed()` and `sorted()` are out of place equivalents

# Dictionaries
- constructor `dict()` can be used to create dictionaries from other types
  - shallow copying
- `keys()` and `values()` methods
- can call `items()` to retrieve tuple of key value pairs and iterate over that
```py
for k, v in something.items():
```
- pprint to pretty print

# Set
- denoted by `p = { 1,2,3 }`
- `{}` creates an empty dictionary
  - use `set()` instead
- `add() update() remove()`
- has set algebra methods
  - `union() intersection() difference() symmetric_difference()`
- other methods
  - `issubset() isdisjoint()`

# Protocols
- requirements of behavior for a certain class of objects
- does not have to be a separate piece of code