# Core Python - Getting Started

# Zen of Python
- Flat is better than nested
- Practicality beats purity
- There should only be one obvious way to do something
- Sparse is better than dense
  - 2 Lines between functions according to PEP8

# Scalar Types
- int
- float
- bool
- None

# int
- Always round down
- `int()` constructor can be passed floats, strings
- can write numbers in hex, octal, and binary literally
- other bases can be used with second constructor parameter

# float
- `float()` constructor can be passed ints, string, scientific notation
- all decimals are seen as this type

# bool
- `True` or `False`
- `bool()` can be passed different types and will determine result based on falsiness

# None
- essentially null
- variables can be set to it 
- checked with `is` or `==`

# While Loops
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
  
# Collections
- str
- bytes
- list
- dict

# str
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

# bytes
- raw binary type
- `b'data'`
- There is a constructor but that's an advanced topic
- `str` -> encode -> `bytes` -> decode

# list
- sequences of objects
- mutable
- `[1,2,3]`
- access and write to an index
- add with `append()`
- can pass string to contructor to make list version of string

# dict
- fundamental to python
- access a key via `[key_name]`
- As of 3.7 keys stay in insertion order, older version have no concept of this 
  
# For Loops
- essentially a for each

# Functions and Modules
- special functions have `__name__`
- can be called "dunder"
- `__main__` means that the module is being run directly
  - If not equal to `__main__` it means that it's being imported
- Python files are modules by default

# Python Execution Model
- `def` is a statment
- Top level functions are defined when a module is imported or run
  
# Command Line Arguments
```python
import sys
sys.argv[1]
```

# docstrings
- literal strings that document functions, modules, and classes
- They must be the first statement in the blocks for these constructs
- Sphinx can be used to create HTML docs from these strings

# Comments
- Use #

# Shebang
- `#!/usr/bin/env python`
- can say if it's 2 or 3
- allows for direct execution on unix like systems
- windows can use pylauncher to achieve the same functionality

# Objects and Types
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

# Exceptions and Control Flow
- `try except` 
- Certain exceptions are never caught (syntax related errors)
- can use `pass` keyword to just continue the code execution
- `raise` will raise the exception that is being handled
  - basically `throw`
- also has support for finally block
  
# Avoid Explicit Type Checks
- Defeats purpose of dynamic typing
- Catching them or throwing them not really needed
- Usually they end up being thrown anyway

# LBYL vs EAFP
- Look before you leap vs Easier to ask for fogiveness than permission
- Python perfers EAFP
- The codes happy path is emphasized rather than being interspersed with error handling
- Basically catch exceptions rather than do checks beforehand
- Exceptions can't be easily ignored, and make it harder for problems to silently be ignored

# Platform Specific Modules
- Windows msvcrt or Unix-like tty for things like detecting a key press

# List and set comprehensions 
- Comprehensions: concise syntax for describing lists, sets, and dictionaries
  - Readable and expressive
- `[len(word) for word in words]`
  - Allows you to create a list where each item is the length of the original item in the ither list
- syntax is basically `[expr(item) for item in iterable]`
- can do the same thing with sets but with `{}`

# Dictionary Comprehensions
- Also uses curly braces but has two parameters separated by `:`

# Filtering Comprehensions
- Need to review these, can be pretty complex
- Sometimes a for loop can be more consise
- Shouldn't have side effects

# Iteration Protocols 
- `iterable`: can be passed to `iter()` to produce an `interator`
- `iterator`: can be passed to `next()` to get the next value in the sequence
- `next()` will through an exception when the end of the collection is reached

# Generator Functions 
- Iterables defined by functions, model sequences with no definite end
- Must include a yield statement
- May include blank return
```py
  def gen123():
    yield 1
    yield 2
    yield 3
  g = gen123()
  next(g) # returns 1 then 2 then 3
```
- they can be used as any other iterable
- will also throw an exception judt like any other iterable
- code inside of a generator function will stop at each yield for each call
- lazy execution allows for generation of very large sequences
- allows for returning of different values based on how many times it has been called

# Generator Expressions
- cross between generators and comprehensions
- ???

# Iteration Tools
- Python treats iteration as core idea
- Has many ways to do it
- `itertools.islice()`: performs lazy slicing of any iterator
- `itertools.count()`: open ended version of `range()`
- `any() and all()`: tell you if any/all numbers in an iterable are true
- `zip()`: zips iteration between two iterables
  - returns tuples, can be unpacked

# Classes
- Create custom types, although you can get pretty far without them 
- can use `type()` to find the class of an object
- python allows you to find the right balance of OOP and functional to solve problems with the right approach
- names have convetion of Camel case
- `pass` allows you to have a class that is minimally syntactically correct
- importing would be like `from <FILE> import <CLASS>`
- `self` is parameter used for instance functions
- `__init__()`: kinda like a constructor
  - difference is that it configures an object that already exists
  - python runtime takes care of actually creating the object
- attributes can be created at initialization just like regular variables
- attributes typically start with an underscore
  - prevents name clashes and is a convention
- in python is that everything is public
  - basically don't use things prefixed with `_`
- class invariants: truth about an object that endure for its lifetime
- getters are named after the property they retrieve

# Duck Typing
- cornerstone of python's typing system
- fitness for use is determined at use
- could have several classes that look like they would have a shared inherited class but with python you don't need to explicitly do that
- as long as behavior is consistent it will work

# Late Binding and Inheritance
- Polymorphism can be done with any classes as long as they fit due to the late binging
  - basis of collections in python actually
- often used in python for sharing implementation
- `class Boeing(Aircraft):`
- duck typing allows for a looser typing