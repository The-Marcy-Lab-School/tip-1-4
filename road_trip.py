"""
Independent check: Road Trip
Work alone: no AI, no notes.
---------------------------------------------------------------------------
PART 1: Build it
---------------------------------------------------------------------------
Write a road trip program. It should ask the user to enter the number
of `miles` they traveled and how many `gallons` of gas they used, then print
their miles per gallon. The output should look something like this:

```
How many miles did you travel? 300
How many gallons did you use? 10
You got 30.0 miles per gallon!
```

Assume the user always types whole numbers.
Guiding questions:
  - How do you ask the user for a value and store it in a variable?
  - input() always gives back a string. How do you handle that?
  - What math gives you miles per gallon?

Test it with these values:
  miles 300, gallons 10   ->  You got 30.0 miles per gallon.
  miles 120, gallons 8    ->  You got 15.0 miles per gallon.
  miles 50,  gallons 4    ->  You got 12.5 miles per gallon.
"""
# ---------------------------------------------------------------------------
# YOUR CODE
# ---------------------------------------------------------------------------



"""
---------------------------------------------------------------------------
PART 2: What if the user types something else?
---------------------------------------------------------------------------
Run your program again and try these:
  miles 300, gallons 0
  miles ten, gallons 10

What happened? Write the name of each error as a comment at the bottom (NameError, TypeError, SyntaxError, etc...).

Look into Python's `try` and `except` keywords. Use them to make your program
print a friendly message instead of crashing:
  gallons 0           ->  Gallons can't be 0.
  a non-number        ->  Please type whole numbers only.

Then answer this at the bottom: how is try / except like if / else, and how
is it different?

---------------------------------------------------------------------------
YOUR ANSWERS
---------------------------------------------------------------------------
Error when gallons is 0:


Error when miles is "ten":


try / except compared with if / else:


"""