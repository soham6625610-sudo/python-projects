#learning python

import random


''' 
random is a Python module (a built-in library). It contains functions for generating random values.

import random tells Python: "Load the random module so I can use its functions."

A built-in library is a collection of pre-written Python code that comes already included with Python.

It is like this that :

Instead of writing everything from scratch, i can use these ready-made tools.

For Example : random
import random

The random library already contains functions like:

random.randint(1, 100)
random.choice(["A", "B", "C"])
random.random()

I don't have to write the logic for generating random numbers—Python's developers already did it.

'''

number = random.randint(1, 100)
'''
## Part 1: `random`

```python
random
```

`random` is the **module (library) name**.

This loaded the `random` library into the program.

## Part 2: `randint(1,100)`


`randint` is a **function** inside the `random` library.

Its job is:

> Return one random integer between the first and second numbers.


## Part 3: `number =`

Suppose

```python
random.randint(1,100)
```

returns

```
57
```

Now the line becomes

```python
number = 57 assigned
```

T

'''
print("Guess a number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))
    ''' int is doing string to int as i put number in string form '''
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct! You guessed it.")
        break